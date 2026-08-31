from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.page_design_toolkit import expander
from src.view_design.page_manager.root_widget.page_stack import PageStack
from src.view_design.page_manager.root_widget.nav_bar.brain import NavBar


class RootWidget(QtW.QWidget):
    """QWidget that contains the main stacked widget and the navigation\
        bar."""

    sgn_in_quiz = QtC.Signal(str)

    def __init__(self, main_stack):
        super().__init__()
        self.main_stack = main_stack

        self.container_grid = QtW.QGridLayout()
        self.page_stack = PageStack(self.main_stack)
        self.page_stack.sgn_in_quiz.connect(self.sgn_in_quiz.emit)

        self.nav_bar = NavBar(self.page_stack)
        self.page_stack.sgn_change_to_quiz_menu.connect(
            self.nav_bar.press_on_quiz_menu_btn
        )

        self.container_grid.addWidget(self.nav_bar, 0, 0)
        self.container_grid.addWidget(self.page_stack, 0, 1)

        expander.expand_layout(self.container_grid)
        self.setLayout(self.container_grid)
        self._set_column_proportion()

    def _set_column_proportion(self):
        self.container_grid.setColumnStretch(0, 20)
        self.container_grid.setColumnStretch(1, 80)

    def switch_to_quiz_menu(self):
        self.page_stack.switch_to_quiz_menu()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.nav_bar.update_btns_size(
            self.width() * 0.2, self.height())
