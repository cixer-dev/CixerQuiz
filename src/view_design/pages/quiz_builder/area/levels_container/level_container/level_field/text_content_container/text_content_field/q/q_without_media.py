from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.text_content_container.\
    text_content_field.q.template import QuestionField


class QuestionWithoutMediaField(QuestionField):
    """Question field for a question_text text default_field without media."""

    def __init__(self, parent_widget):
        super().__init__(parent_widget)
        self.question_field.sgn_field_content_changed.connect(
            self._on_question_changed
        )
        self.addLayout(self.question_field, 0, 0)
        self._set_column_proportion()

    def _on_question_changed(self, new_question):
        self.question = new_question
        question_to_media_path = {self.question: None}
        self.sgn_question_content_changed.emit(question_to_media_path)

    def _set_column_proportion(self):
        self.setColumnStretch(0, 100)
        self.question_field.setColumnStretch(0, 10)
        self.question_field.setColumnStretch(1, 90)
