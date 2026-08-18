from src.view_design.in_trivia.trivias_templates.abstract_levels.media_texts.\
    brain import TriviaLevelMediaTexts

from src.view_design.custom_widgets.trivia_widgets.answers_panel.only_label \
    import APOnlyLabel
from src.view_design.custom_widgets.trivia_widgets.interactive_panels.\
    media_with_texts import InteractivePanelMediaWithTexts
from src.view_design.custom_widgets.trivia_widgets.question_panel.with_image \
    import QPWithImage


class TriviaLevelImageTexts(TriviaLevelMediaTexts):
    """Trivia level with image-based question panel and text-based \
        answer panel."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)

        self.question_panel = QPWithImage(self.question_to_media_path)
        self.answer_panel = APOnlyLabel(
            self.answers, self.correct_answer, self.question
        )
        self.row_question_proportion = 60
        self.interactive_panel = InteractivePanelMediaWithTexts(
            self.question_panel,
            self.answer_panel
        )
        self._build_interactive_panel()
