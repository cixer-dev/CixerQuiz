from src.model.translation_handler import _
from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.text_content_container.\
    text_content_field.a_grid.individual_a.template \
    import AnswerField
from src.view_design.custom_widgets.fields_with_path.\
    fields_with_path_and_filters \
    import FieldWithPathAndFilters


class AnswerWithMediaField(AnswerField):
    """Answer field for an answer text default field and an associated \
    media path."""

    def __init__(self, parent_widget, filters_code, answer_title=None):
        super().__init__(parent_widget, answer_title)
        self.filters_code = filters_code
        self.answer_media_path = ""
        self.answer_media_path_field = FieldWithPathAndFilters(
            self.parent_widget,
            _("Answer\nmedia path"),
            self.filters_code,
        )

        self.answer_media_path_field.sgn_path_changed.connect(
            self.on_answer_media_path_changed
        )

        self.addLayout(self.answer_text_field, 0, 0)
        self.addLayout(self.answer_media_path_field, 0, 1)
        self.addWidget(self.add_answer_btn, 0, 2)
        self.addWidget(self.delete_answer_btn, 0, 3)
        self._set_column_proportion()

    def on_answer_media_path_changed(self, answer_media_path):
        self.answer_media_path = answer_media_path
        self._on_changed_answer_content()

    def _on_changed_answer_content(self):
        answer_to_media_path = {self.answer_text: self.answer_media_path}
        self.sgn_answer_content_changed.emit(answer_to_media_path)

    def _set_column_proportion(self):
        self.setColumnStretch(0, 45)
        self.setColumnStretch(1, 45)
        self.setColumnStretch(2, 5)
        self.setColumnStretch(3, 5)
        self.answer_text_field.setColumnStretch(0, 22)
        self.answer_text_field.setColumnStretch(1, 78)
