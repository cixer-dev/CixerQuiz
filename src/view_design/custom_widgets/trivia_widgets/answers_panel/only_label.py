from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.trivia_widgets.answers_panel.\
    template import APTemplate


class APOnlyLabel(APTemplate):
    """QWidget that emits signals based on the selected answer."""

    def __init__(self, answers, correct_answer, question):
        super().__init__(correct_answer, question)

        for answer_index, answer in enumerate(answers, start=1):
            answer_btn = QtW.QPushButton(answer)
            answer_btn.pressed.connect(
                lambda a=answer: self._send_answer_outcome(a)
            )
            self.container_grid.addWidget(answer_btn, answer_index, 0)
