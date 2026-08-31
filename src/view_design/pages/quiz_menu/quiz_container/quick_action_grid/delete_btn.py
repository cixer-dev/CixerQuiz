from PySide6 import QtCore as QtC

from src.model import quiz_remover
from src.model.translation_handler import _
from src.view_design.custom_widgets.push_buttons.\
    standard_button_with_icon import StandardButtonWithIcon
from src.view_design.custom_widgets.error_handlers.\
    warning_with_remove_signaling import WarningWithRemoveSignaling


class DeleteButton(StandardButtonWithIcon):
    """QPushButton that deletes a quiz directory when pressed \
    using the QuizRemover module."""
    sgn_deletion_completed = QtC.Signal()

    def __init__(self, quiz_filepath, parent_widget):
        super().__init__(standard_icon_key="delete_icon_path")
        self.quiz_filepath = quiz_filepath
        self.parent_widget = parent_widget
        self.pressed.connect(self.show_confirmation_dialog)

    def show_confirmation_dialog(self):
        warning_msg = WarningWithRemoveSignaling(
            self.parent_widget,
            message=_(
                "Are you sure you want to delete this quiz? "
                "This operation cannot be undone.")
        )
        warning_msg.sgn_ok_pressed.connect(self._on_delete_quiz)
        warning_msg.show()

    def _on_delete_quiz(self):
        try:
            quiz_remover.delete_quiz(self.quiz_filepath)
            self.sgn_deletion_completed.emit()
        except Exception as e:
            raise e
