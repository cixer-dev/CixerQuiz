from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.view_design.page_design_toolkit import cleaner, expander
from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.text_content_container.text_content_field.\
    a_grid.a_grid_with_media import AnswerGridWithMediaField
from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.text_content_container.\
    text_content_field.a_grid.a_grid_without_media \
    import AnswerGridWithoutMediaField
from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.text_content_container.text_content_field\
        .q.q_with_media import QuestionWithMediaField
from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.text_content_container.text_content_field\
        .q.q_without_media import QuestionWithoutMediaField


class TextContentField(QtW.QVBoxLayout):
    """QVBoxLayout combining a question_text default_field and an answers \
        default_field."""

    sgn_question_content_changed = QtC.Signal(dict)
    sgn_answer_content_changed = QtC.Signal(list)
    sgn_text_content_field_was_rebuild = QtC.Signal()

    def __init__(
        self,
        parent_widget,
        question_have_media,
        answers_have_media,
        filters_code,
    ):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.parent_widget = parent_widget
        self.question_have_media = question_have_media
        self.answers_have_media = answers_have_media
        self.filters_code = filters_code

        self.question = None
        self.answers_list = None
        self.assets_paths_list = []

        self.question_field_container = QtW.QWidget()
        self.answers_field_container = QtW.QWidget()

        self.question_field = self._build_question_field()
        self.answers_field = self._build_answers_field(num_answers=2)

        self.build_answer_field_connections()
        self.build_question_field_connections()

        self.addWidget(self.question_field_container)
        self.addLayout(self.answers_field)

        expander.expand_layout(self)

    def _build_question_field(self):
        if self.question_have_media:
            question_field = QuestionWithMediaField(
                self.parent_widget,
                self.filters_code[0],
            )
        else:
            question_field = QuestionWithoutMediaField(self.parent_widget)

        self.question_field_container.setLayout(question_field)
        return question_field

    def _build_answers_field(self, num_answers):
        if self.answers_have_media:
            return AnswerGridWithMediaField(
                self.parent_widget,
                num_answers,
                self.filters_code[1],
            )
        return AnswerGridWithoutMediaField(self.parent_widget, num_answers)

    def build_question_field_connections(self):
        self.question_field.sgn_question_content_changed.connect(
            self._on_question_content_changed
        )

    def build_answer_field_connections(self):
        self.answers_field.sgn_num_answers_changed.connect(
            self._on_num_answers_changed_signal
        )
        self.answers_field.sgn_answer_content_changed.connect(
            self._on_answer_content_changed
        )

    def _on_num_answers_changed_signal(self, num_answers):
        cleaner.clear_layout(self.answers_field)
        self.answers_field = self._build_answers_field(num_answers)
        self.build_answer_field_connections()
        self.addLayout(self.answers_field)

        self.sgn_text_content_field_was_rebuild.emit()
        expander.expand_layout(self)

    def _on_question_content_changed(self, new_question_content):
        self.question = new_question_content
        self.sgn_question_content_changed.emit(self.question)

    def _on_answer_content_changed(self, new_answers_content):
        self.answers_list = new_answers_content
        self.sgn_answer_content_changed.emit(self.answers_list)

    def update_containers_size(self, tb_area_size):
        self.update_question_container_size(tb_area_size)
        self.update_answers_size(tb_area_size)

    def update_question_container_size(self, tb_area_size):
        question_container_width = tb_area_size.width()
        question_container_height = tb_area_size.height() // 10
        self.question_field_container.setMaximumWidth(question_container_width)
        self.question_field_container.setFixedHeight(question_container_height)

    def update_answers_size(self, tb_area_size):
        self.answers_field.update_answers_size(tb_area_size)
