from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.pages.config_menu.brain import ConfigMenu
from src.view_design.pages.trivia_menu.brain import TriviaMenu
from src.view_design.pages.trivia_builder.brain import TriviaBuilderMenu


class PageStack(QtW.QStackedWidget):
    """Stacked widget that contain the pages accessible in the \
        navigation bar"""

    sgn_in_trivia = QtC.Signal(str)
    sgn_change_to_trivia_menu = QtC.Signal()

    def __init__(self, main_stack):
        super().__init__()
        self.main_stack = main_stack
        self.trivia_menu = TriviaMenu(self.main_stack)
        self.config_menu = ConfigMenu(self)
        self.trivia_builder = TriviaBuilderMenu(self)

        self.addWidget(self.trivia_menu)
        self.addWidget(self.config_menu)
        self.addWidget(self.trivia_builder)

        self.switch_to_trivia_menu()

    def switch_to_trivia_menu(self):
        self.setCurrentWidget(self.trivia_menu)
        self.sgn_change_to_trivia_menu.emit()

    def switch_to_config_menu(self):
        self.setCurrentWidget(self.config_menu)

    def switch_to_trivia_builder(self):
        self.setCurrentWidget(self.trivia_builder)
