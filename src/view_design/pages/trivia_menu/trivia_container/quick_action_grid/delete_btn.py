from PySide6 import QtCore as QtC

from src.model import trivia_remover
from src.model.translation_handler import _
from src.view_design.custom_widgets.push_buttons.\
    standard_button_with_icon import StandardButtonWithIcon
from src.view_design.custom_widgets.error_handlers.\
    warning_with_remove_signaling import WarningWithRemoveSignaling


class DeleteButton(StandardButtonWithIcon):
    """QPushButton that deletes a trivia directory when pressed \
    using the TriviaRemover module."""
    sgn_deletion_completed = QtC.Signal()

    def __init__(self, trivia_filepath, parent_widget):
        super().__init__(standard_icon_key="delete_icon_path")
        self.trivia_filepath = trivia_filepath
        self.parent_widget = parent_widget
        self.pressed.connect(self.show_confirmation_dialog)

    def show_confirmation_dialog(self):
        warning_msg = WarningWithRemoveSignaling(
            self.parent_widget,
            message=_(
                "Are you sure you want to delete this trivia? "
                "This operation cannot be undone.")
        )
        warning_msg.sgn_ok_pressed.connect(self._on_delete_trivia)
        warning_msg.show()

    def _on_delete_trivia(self):
        try:
            trivia_remover.delete_trivia(self.trivia_filepath)
            self.sgn_deletion_completed.emit()
        except Exception as e:
            raise e
