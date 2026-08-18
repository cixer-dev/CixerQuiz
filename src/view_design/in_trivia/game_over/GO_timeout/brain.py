from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.page_design_toolkit import expander
from src.view_design.custom_animations import up_down_to_up
from src.view_design.custom_widgets.containers.standard \
    import StandardContainer
from src.view_design.in_trivia.game_over.loss_header import LossHeader
from src.view_design.in_trivia.game_over.go_back import GoBack
from src.view_design.in_trivia.game_over.repeat_trivia import RepeatTrivia
from src.view_design.in_trivia.game_over.GO_timeout.loss_timeout_reason \
    import LossTimeoutReasonExplanation


class GOTimeout(QtW.QWidget):
    """Timeout game-over page."""

    def __init__(self, main_stack, trivia_path):
        super().__init__()
        self.main_stack = main_stack
        self.trivia_path = trivia_path

        self.main_grid = QtW.QGridLayout()
        self.up_grid = self._build_up_grid()
        self.down_grid = self._build_down_grid()
        self.down_container = StandardContainer(layout_inside=self.down_grid)
        self.main_grid.addLayout(self.up_grid, 1, 1)
        self.main_grid.addWidget(self.down_container, 3, 1)
        self.setLayout(self.main_grid)
        self._set_rows_proportion()
        self._set_column_proportion()
        expander.expand_layout(self.main_grid)

    @staticmethod
    def _build_up_grid():
        up_grid = QtW.QGridLayout()

        loss_header = LossHeader()
        loss_header.setAlignment(QtC.Qt.AlignmentFlag.AlignCenter)
        loss_reason_explanation = LossTimeoutReasonExplanation()
        loss_reason_explanation.setAlignment(QtC.Qt.AlignmentFlag.AlignCenter)

        up_grid.addWidget(loss_header, 0, 0)
        up_grid.addWidget(loss_reason_explanation, 2, 0)

        up_grid.setRowStretch(0, 45)
        up_grid.setRowStretch(1, 10)
        up_grid.setRowStretch(2, 45)
        return up_grid

    def _build_down_grid(self):
        down_grid = QtW.QGridLayout()

        go_back_btn = GoBack()
        repeat_trivia = RepeatTrivia()

        go_back_btn.pressed.connect(self.main_stack.switch_to_trivia_menu)
        repeat_trivia.pressed.connect(
            lambda: self.main_stack.switch_to_in_trivia(self.trivia_path)
        )

        down_grid.addWidget(go_back_btn, 0, 0)
        down_grid.addWidget(repeat_trivia, 2, 0)

        down_grid.setRowStretch(0, 45)
        down_grid.setRowStretch(1, 10)
        down_grid.setRowStretch(2, 45)
        return down_grid

    def _set_rows_proportion(self):
        self.main_grid.setRowStretch(0, 5)
        self.main_grid.setRowStretch(1, 40)
        self.main_grid.setRowStretch(2, 10)
        self.main_grid.setRowStretch(3, 40)
        self.main_grid.setRowStretch(4, 5)

    def _set_column_proportion(self):
        self.main_grid.setColumnStretch(0, 30)
        self.main_grid.setColumnStretch(1, 40)
        self.main_grid.setColumnStretch(2, 30)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        up_down_to_up.move_up_to_down(self.down_container)
