from src.view_design.in_trivia.trivias_templates.abstract_levels.media_texts.\
    brain import TriviaLevelMediaTexts

from src.view_design.custom_widgets.trivia_widgets.answers_panel.only_label \
    import APOnlyLabel
from src.view_design.custom_widgets.trivia_widgets.interactive_panels.\
    media_with_texts import InteractivePanelMediaWithTexts
from src.view_design.custom_widgets.trivia_widgets.question_panel.with_video \
    import QPWithVideo


class TriviaLevelVideoTexts(TriviaLevelMediaTexts):
    """Trivia level with video-based question panel and text-based \
        answer panel."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)

        self.question_panel = QPWithVideo(self.question_to_media_path)
        self.answer_panel = APOnlyLabel(
            self.answers, self.correct_answer, self.question
        )
        self.interactive_panel = InteractivePanelMediaWithTexts(
            self.question_panel,
            self.answer_panel
        )
        self._build_interactive_panel()
