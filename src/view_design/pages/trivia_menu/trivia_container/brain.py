from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.pages.trivia_menu.trivia_container.quick_action_grid.\
    brain import QuickActionGrid
from src.view_design.pages.trivia_menu.trivia_container.start_trivia_btn \
    import StartTriviaButton
from src.view_design.pages.trivia_menu.trivia_container.trivia_name_label \
    import TriviaNameLabel
from src.view_design.pages.trivia_menu.trivia_container.\
    trivia_description_plaintext import TriviaDescriptionPlainText


class TriviaArea(QtW.QWidget):
    """QWidget that contains the actions and information related to \
        the trivia."""

    sgn_deletion_completed = QtC.Signal()
    sgn_pin_status_changed = QtC.Signal()

    def __init__(self, trivia_filepath, trivia_info, parent_widget):
        super().__init__()
        self.trivia_filepath = trivia_filepath
        self.trivia_info = trivia_info
        self.parent_widget = parent_widget

        self.trivia_grid = QtW.QGridLayout()
        self.quick_action_grid \
            = QuickActionGrid(trivia_filepath, self.parent_widget)
        self.start_trivia_btn \
            = StartTriviaButton(trivia_filepath, self.parent_widget)
        self.trivia_name_label = TriviaNameLabel(trivia_info)
        self.trivia_description_plaintext \
            = TriviaDescriptionPlainText(trivia_info)

        self.quick_action_grid.sgn_deletion_completed.connect(
            self._on_deletion_completed
        )
        self.quick_action_grid.sgn_pin_status_changed.connect(
            self._on_pin_status_changed
        )

        self.trivia_grid.addLayout(self.quick_action_grid, 0, 0)
        self.trivia_grid.addWidget(self.start_trivia_btn, 0, 1)

        self.informative_grid = QtW.QGridLayout()
        self.informative_grid.addWidget(self.trivia_name_label, 0, 0)
        self.informative_grid.addWidget(
            self.trivia_description_plaintext, 1, 0
        )
        self.trivia_grid.addLayout(self.informative_grid, 0, 2)

        self.setLayout(self.trivia_grid)

        self._set_column_proportion()

    def _on_deletion_completed(self):
        self.sgn_deletion_completed.emit()

    def _on_pin_status_changed(self):
        self.sgn_pin_status_changed.emit()

    def _set_column_proportion(self):
        self.trivia_grid.setColumnStretch(0, 5)
        self.trivia_grid.setColumnStretch(1, 10)
        self.trivia_grid.setColumnStretch(2, 85)
