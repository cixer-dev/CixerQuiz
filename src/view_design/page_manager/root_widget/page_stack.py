from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.pages.config_menu.brain import ConfigMenu
from src.view_design.pages.quiz_menu.brain import QuizMenu
from src.view_design.pages.quiz_builder.brain import QuizBuilderMenu


class PageStack(QtW.QStackedWidget):
    """Stacked widget that contain the pages accessible in the \
        navigation bar"""

    sgn_in_quiz = QtC.Signal(str)
    sgn_change_to_quiz_menu = QtC.Signal()

    def __init__(self, main_stack):
        super().__init__()
        self.main_stack = main_stack
        self.quiz_menu = QuizMenu(self.main_stack)
        self.config_menu = ConfigMenu(self)
        self.quiz_builder = QuizBuilderMenu(self)

        self.addWidget(self.quiz_menu)
        self.addWidget(self.config_menu)
        self.addWidget(self.quiz_builder)

        self.switch_to_quiz_menu()

    def switch_to_quiz_menu(self):
        self.setCurrentWidget(self.quiz_menu)
        self.sgn_change_to_quiz_menu.emit()

    def switch_to_config_menu(self):
        self.setCurrentWidget(self.config_menu)

    def switch_to_quiz_builder(self):
        self.setCurrentWidget(self.quiz_builder)
