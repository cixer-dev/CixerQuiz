from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.page_design_toolkit import expander
from src.view_design.custom_animations import up_down_to_up
from src.view_design.in_trivia.victory_screen.victory_label import VictoryLabel
from src.view_design.in_trivia.victory_screen.victory_msg import VictoryMsg
from src.view_design.in_trivia.game_over.go_back import GoBack


class VictoryScreen(QtW.QWidget):
    """Victory screen that shows a title, victory message, and a main \
        menu button."""

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
        self.container_grid = QtW.QGridLayout()
        self.label_title = self.build_title()
        self.label_victory_message = self.build_victory_message()
        self.go_back = self.build_go_main_menu_btn()
        self.set_column_proportion()
        self.set_row_proportion()

        self.setLayout(self.container_grid)
        expander.expand_layout(self.container_grid)

    def build_title(self):
        title_label = VictoryLabel()
        title_label.setAlignment(QtC.Qt.AlignmentFlag.AlignCenter)
        self.container_grid.addWidget(title_label, 1, 1)
        return title_label

    def build_victory_message(self):
        victory_message = VictoryMsg()
        victory_message.setAlignment(QtC.Qt.AlignmentFlag.AlignCenter)
        self.container_grid.addWidget(victory_message, 3, 1)
        return victory_message

    def build_go_main_menu_btn(self):
        go_back_menu = GoBack()
        self.container_grid.addWidget(go_back_menu, 5, 1)
        go_back_menu.pressed.connect(self.parent_widget.switch_to_trivia_menu)
        return go_back_menu

    def set_column_proportion(self):
        self.container_grid.setColumnStretch(0, 30)
        self.container_grid.setColumnStretch(1, 40)
        self.container_grid.setColumnStretch(2, 30)

    def set_row_proportion(self):
        self.container_grid.setRowStretch(0, 5)
        self.container_grid.setRowStretch(1, 10)
        self.container_grid.setRowStretch(2, 5)
        self.container_grid.setRowStretch(3, 15)
        self.container_grid.setRowStretch(4, 5)
        self.container_grid.setRowStretch(5, 10)
        self.container_grid.setRowStretch(6, 5)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        up_down_to_up.move_up_to_down(self.go_back)
