from PySide6 import QtWidgets as QtW

from src.model.data_structure_formatter import str_formatter
from src.view_design.custom_widgets.quiz_widgets.answers_panel.\
    template import APTemplate
from src.view_design.custom_widgets.quiz_widgets.image_label \
    import ImageLabel


class APWithImages(APTemplate):
    """QWidget with image-based answer buttons for multiple-choice prompts."""

    def __init__(self, answers_to_image_path, correct_answer, question):
        super().__init__(correct_answer, question)
        self.answers_to_image_path = answers_to_image_path
        self.images_paths = tuple(answers_to_image_path.values())
        self.answers_image_labels = self._build_answers_image_labels()
        self.answers_image_btns = self._build_answers_image_btns()
        self._set_row_proportions()

    def _build_answers_image_labels(self):
        answers_image_labels = []
        for answer_index, answer_image_path in enumerate(self.images_paths):
            answer_image_label = ImageLabel(answer_image_path)
            answers_image_labels.append(answer_image_label)
            self.container_grid.addWidget(answer_image_label, 0, answer_index)
        return answers_image_labels

    def _build_answers_image_btns(self):
        answer_btns = []
        for answer_index, answer in enumerate(self.answers_to_image_path):
            formatted_answer = str_formatter.split_long_string(answer, 25)
            answer_btn = QtW.QPushButton(formatted_answer)
            answer_btn.pressed.connect(
                lambda a=answer: self._send_answer_outcome(a)
            )
            answer_btns.append(answer_btn)
            self.container_grid.addWidget(answer_btn, 1, answer_index)
        return answer_btns

    def _set_row_proportions(self):
        self.container_grid.setRowStretch(0, 90)
        self.container_grid.setRowStretch(1, 10)
