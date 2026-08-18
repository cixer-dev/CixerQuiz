from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class BuilderActionBar(QtW.QGridLayout):
    """QGridLayout that contains navigation and action buttons."""

    sgn_confirmed_selection = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget

        self.confirm_selection_btn = QtW.QPushButton(_("Create trivia"))
        self.confirm_selection_btn.setObjectName("action_btn")
        self.confirm_selection_btn.pressed.connect(
            self._on_confirmed_selection
        )

        self.addWidget(self.confirm_selection_btn, 0, 1)
        self._set_column_proportion()

    def _on_confirmed_selection(self):
        self.sgn_confirmed_selection.emit()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 40)
        self.setColumnStretch(1, 20)
        self.setColumnStretch(2, 40)

    def get_confirmed_selection(self):
        return self.sgn_confirmed_selection
