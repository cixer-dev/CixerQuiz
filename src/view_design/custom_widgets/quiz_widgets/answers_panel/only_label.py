from PySide6 import QtWidgets as QtW

from src.model.data_structure_formatter import str_formatter
from src.view_design.custom_widgets.quiz_widgets.answers_panel.\
    template import APTemplate


class APOnlyLabel(APTemplate):
    """QWidget that emits signals based on the selected answer."""

    def __init__(self, answers, correct_answer, question):
        super().__init__(correct_answer, question)

        for answer_index, answer in enumerate(answers, start=1):
            formatted_answer = str_formatter.split_long_string(
                    answer,
                    35
                )
            answer_btn = QtW.QPushButton(formatted_answer)
            answer_btn.pressed.connect(
                lambda a=answer: self._send_answer_outcome(a)
            )
            self.container_grid.addWidget(answer_btn, answer_index, 0)
