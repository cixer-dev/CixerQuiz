from src.view_design.in_trivia.trivias_templates.abstract_levels.text_medias.\
    brain import TriviaLevelTextMedias

from src.view_design.custom_widgets.trivia_widgets.answers_panel.with_images \
    import APWithImages
from src.view_design.custom_widgets.trivia_widgets.interactive_panels.\
    text_with_medias import InteractivePanelTextWithMedias
from src.view_design.custom_widgets.trivia_widgets.question_panel.\
    only_plaintext import QPOnlyPlaintext


class TriviaLevelTextImages(TriviaLevelTextMedias):
    """Trivia level with text-based question panel and image-based \
        answer panel."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)

        self.question_panel = QPOnlyPlaintext(self.question)
        self.answer_panel = APWithImages(
            self.answers_to_media_path, self.correct_answer, self.question
        )
        self.interactive_panel = InteractivePanelTextWithMedias(
            self.question_panel,
            self.answer_panel
        )
        self._build_interactive_panel()
