from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC

from src.view_design.custom_animations import up_down_to_up
from src.view_design.page_design_toolkit import layout_spacer


class APTemplate(QtW.QWidget):
    """QWidget that emits signals based on the selected answer."""

    sgn_pressed_answer_is_correct = QtC.Signal()
    sgn_pressed_answer_is_incorrect = QtC.Signal(dict)

    def __init__(self, correct_answer, question_text):
        super().__init__()
        self.correct_answer = correct_answer
        self.question_text = question_text
        self.container_grid = QtW.QGridLayout()
        self.setLayout(self.container_grid)
        up_down_to_up.move_up_to_down(self)
        layout_spacer.set_vertical_space(self, self.container_grid)

    def _send_answer_outcome(self, answer_btn_text):
        if answer_btn_text == self.correct_answer:
            self.sgn_pressed_answer_is_correct.emit()
            return

        self.sgn_pressed_answer_is_incorrect.emit(
            {
                "correct_answer": self.correct_answer,
                "question_text": self.question_text
            }
        )

    def resizeEvent(self, event):
        super().resizeEvent(event)
        up_down_to_up.move_up_to_down(self)
        layout_spacer.set_vertical_space(self, self.container_grid)
