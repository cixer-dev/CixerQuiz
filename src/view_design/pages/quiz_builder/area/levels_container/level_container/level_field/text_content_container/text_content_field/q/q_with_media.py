from src.model.translation_handler import _
from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.text_content_container.\
    text_content_field.q.template import QuestionField
from src.view_design.custom_widgets.fields_with_path.\
    fields_with_path_and_filters \
    import FieldWithPathAndFilters


class QuestionWithMediaField(QuestionField):
    """Question field for a question_text text default_field and an \
    associated media path."""
    def __init__(self, parent_widget, filters_code):
        super().__init__(parent_widget)
        self.filters_code = filters_code
        self.question_media_path = " "

        self.question_media_path_field = FieldWithPathAndFilters(
            self.parent_widget,
            _("Question media"),
            self.filters_code,
        )

        self.question_field.sgn_field_content_changed.connect(
            self._on_question_changed
        )
        self.question_media_path_field.sgn_path_changed.connect(
            self._on_question_path_changed
        )

        self.addLayout(self.question_field, 0, 0)
        self.addLayout(self.question_media_path_field, 0, 1)

        self._set_column_proportion()

    def _on_question_changed(self, new_question):
        self.question = new_question
        question_to_media_path = {self.question: self.question_media_path}
        self.sgn_question_content_changed.emit(question_to_media_path)

    def _on_question_path_changed(self, new_question_path):
        self.question_media_path = new_question_path
        question_to_media_path = {self.question: self.question_media_path}
        self.sgn_question_content_changed.emit(question_to_media_path)

    def _set_column_proportion(self):
        self.setColumnStretch(0, 45)
        self.setColumnStretch(1, 55)
        self.question_field.setColumnStretch(0, 22)
        self.question_field.setColumnStretch(1, 78)
