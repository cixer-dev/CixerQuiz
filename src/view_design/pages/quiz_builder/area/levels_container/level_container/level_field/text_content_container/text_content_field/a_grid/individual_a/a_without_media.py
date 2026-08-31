from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.text_content_container.\
    text_content_field.a_grid.individual_a.template import AnswerField


class AnswerWithoutMediaField(AnswerField):
    """Answer field for an answer text default field without media."""

    def __init__(self, parent_widget, answer_title=None):
        super().__init__(parent_widget, answer_title)

        self.addLayout(self.answer_text_field, 0, 0)
        self.addWidget(self.add_answer_btn, 0, 1)
        self.addWidget(self.delete_answer_btn, 0, 2)
        self._set_column_proportion()

    def _set_column_proportion(self):
        self.setColumnStretch(0, 90)
        self.setColumnStretch(1, 5)
        self.setColumnStretch(2, 5)
        self.answer_text_field.setColumnStretch(0, 11)
        self.answer_text_field.setColumnStretch(1, 89)
