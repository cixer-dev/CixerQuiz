from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.text_content_container.\
    text_content_field.brain import TextContentField


class TextContentFieldContainer(QtW.QVBoxLayout):
    """QVBoxLayout layout holding multiple text content fields."""

    sgn_question_changed = QtC.Signal(list)
    sgn_answers_changed = QtC.Signal(list)
    sgn_text_content_container_was_rebuild = QtC.Signal()

    def __init__(
        self,
        parent_widget,
        num_possible_questions,
        question_have_media,
        answers_have_media,
        filters_code,
    ):
        super().__init__()
        self.parent_widget = parent_widget
        self.num_possible_questions = num_possible_questions
        self.question_have_media = question_have_media
        self.answers_have_media = answers_have_media
        self.filters_code = filters_code

        self.questions_list = []
        self.answers_list = []

        self.text_content_fields = self._build_text_content_fields()

    def _build_text_content_fields(self):
        text_content_fields = []
        for text_content_field_index in range(self.num_possible_questions):
            text_content_field = self._build_text_content_field(
                text_content_field_index
            )
            text_content_fields.append(text_content_field)
            self.addLayout(text_content_field)
        return text_content_fields

    def _build_text_content_field(self, text_content_field_index):
        text_content_field = TextContentField(
            self.parent_widget,
            self.question_have_media,
            self.answers_have_media,
            self.filters_code,
        )
        text_content_field.sgn_question_content_changed.connect(
            lambda new_question_content, idx=text_content_field_index:
            self._on_question_content_changed(
                new_question_content,
                idx,
            )
        )
        text_content_field.sgn_answer_content_changed.connect(
            lambda new_answer_content, idx=text_content_field_index:
            self._on_answers_content_changed(
                new_answer_content,
                idx,
            )
        )
        text_content_field.sgn_text_content_field_was_rebuild.connect(
            self._on_text_content_field_was_rebuild
        )
        return text_content_field

    def _on_question_content_changed(self, new_question_content, index):
        self._handler_length_list(self.questions_list, index)
        self.questions_list[index] = new_question_content
        self._format_question_list()
        self.sgn_question_changed.emit(self.questions_list)

    @staticmethod
    def _handler_length_list(array, index):
        if len(array) <= index:
            needed_list_positions = index - len(array) + 1
            array.extend([{}] * needed_list_positions)

    def _format_question_list(self):
        for question_index in range(len(self.questions_list)):
            question = self.questions_list[question_index]
            if isinstance(question, dict):
                question_key = next(iter(question.keys()))
                question_path = next(iter(question.values()))
                if question_path is None:
                    self.questions_list[question_index] = question_key

    def _on_answers_content_changed(self, new_answer_content, index):
        self._handler_length_list(self.answers_list, index)
        self.answers_list[index] = new_answer_content
        self.sgn_answers_changed.emit(self.answers_list)

    def _on_text_content_field_was_rebuild(self):
        self.sgn_text_content_container_was_rebuild.emit()

    def update_size(self, tb_area_size):
        for text_content_field in self.text_content_fields:
            text_content_field.update_containers_size(tb_area_size)
