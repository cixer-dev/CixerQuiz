from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.pages.quiz_menu.quiz_container.quick_action_grid.\
    brain import QuickActionGrid
from src.view_design.pages.quiz_menu.quiz_container.start_quiz_btn \
    import StartQuizButton
from src.view_design.pages.quiz_menu.quiz_container.quiz_name_label \
    import QuizNameLabel
from src.view_design.pages.quiz_menu.quiz_container.\
    quiz_description_plaintext import QuizDescriptionPlainText


class QuizArea(QtW.QWidget):
    """QWidget that contains the actions and information related to \
        the quiz."""

    sgn_deletion_completed = QtC.Signal()
    sgn_pin_status_changed = QtC.Signal()

    def __init__(self, quiz_filepath, quiz_info, parent_widget):
        super().__init__()
        self.quiz_filepath = quiz_filepath
        self.quiz_info = quiz_info
        self.parent_widget = parent_widget

        self.quiz_grid = QtW.QGridLayout()
        self.quick_action_grid \
            = QuickActionGrid(quiz_filepath, self.parent_widget)
        self.start_quiz_btn \
            = StartQuizButton(quiz_filepath, self.parent_widget)
        self.quiz_name_label = QuizNameLabel(quiz_info)
        self.quiz_description_plaintext \
            = QuizDescriptionPlainText(quiz_info)

        self.quick_action_grid.sgn_deletion_completed.connect(
            self._on_deletion_completed
        )
        self.quick_action_grid.sgn_pin_status_changed.connect(
            self._on_pin_status_changed
        )

        self.quiz_grid.addLayout(self.quick_action_grid, 0, 0)
        self.quiz_grid.addWidget(self.start_quiz_btn, 0, 1)

        self.informative_grid = QtW.QGridLayout()
        self.informative_grid.addWidget(self.quiz_name_label, 0, 0)
        self.informative_grid.addWidget(
            self.quiz_description_plaintext, 1, 0
        )
        self.quiz_grid.addLayout(self.informative_grid, 0, 2)

        self.setLayout(self.quiz_grid)

        self._set_column_proportion()

    def _on_deletion_completed(self):
        self.sgn_deletion_completed.emit()

    def _on_pin_status_changed(self):
        self.sgn_pin_status_changed.emit()

    def _set_column_proportion(self):
        self.quiz_grid.setColumnStretch(0, 5)
        self.quiz_grid.setColumnStretch(1, 10)
        self.quiz_grid.setColumnStretch(2, 85)
