from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.pages.quiz_menu.quiz_container.quick_action_grid.\
    delete_btn import DeleteButton
from src.view_design.pages.quiz_menu.quiz_container.quick_action_grid.\
    pin_or_unpin_btn import PinOrUnpinButton


class QuickActionGrid(QtW.QGridLayout):
    """QGridLayout that contains quick actions related to the quiz."""

    sgn_deletion_completed = QtC.Signal()
    sgn_pin_status_changed = QtC.Signal()

    def __init__(self, quiz_filepath, parent_widget):
        super().__init__()
        self.quiz_filepath = quiz_filepath
        self.parent_widget = parent_widget

        self.pin_or_unpin_quiz_btn \
            = PinOrUnpinButton(self.quiz_filepath, self.parent_widget)
        self.delete_quiz_btn \
            = DeleteButton(self.quiz_filepath, self.parent_widget)

        self.pin_or_unpin_quiz_btn.sgn_pin_status_changed.connect(
            self.sgn_pin_status_changed.emit
            )
        self.delete_quiz_btn.sgn_deletion_completed.connect(
            self._on_deletion_completed
            )

        self.addWidget(self.pin_or_unpin_quiz_btn, 0, 0)
        self.addWidget(self.delete_quiz_btn, 1, 0)

    def _on_deletion_completed(self):
        self.sgn_deletion_completed.emit()
