from src.model.translation_handler import _
from src.view_design.pages.trivia_builder.area.levels_container.\
    level_container.level_field.text_content_container.\
    text_content_field.a_grid.template import AnswerGridField
from src.view_design.pages.trivia_builder.area.levels_container.\
    level_container.level_field.text_content_container.\
    text_content_field.a_grid.individual_a.a_with_media \
    import AnswerWithMediaField


class AnswerGridWithMediaField(AnswerGridField):
    """AnswerGridField for managing multiple answers with media."""

    def __init__(self, parent_widget, num_answers, filters_code):
        super().__init__(parent_widget, num_answers)
        self.filters_code = filters_code
        self.answers_assets_paths = []
        for answer_index in range(self.num_answers):
            answer_field = self._build_answer_field(answer_index)
            self._build_answer_field_connections(answer_field, answer_index)
            self._append_answer_in_container(answer_field, answer_index)

    def _build_answer_field(self, answer_index):
        if answer_index == 0:
            answer_field = AnswerWithMediaField(
                self.parent_widget,
                self.filters_code,
                _("Correct\nanswer")
            )
        else:
            answer_field = AnswerWithMediaField(
                self.parent_widget,
                self.filters_code
            )
        return answer_field
