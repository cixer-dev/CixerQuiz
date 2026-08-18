from src.view_design.in_trivia.trivias_templates.abstract_levels.\
    media_medias.brain import TriviaLevelMediaMedias

from src.view_design.custom_widgets.trivia_widgets.interactive_panels.\
    media_with_medias import InteractivePanelMediaWithMedias
from src.view_design.custom_widgets.trivia_widgets.question_panel.\
    with_video import QPWithVideo
from src.view_design.custom_widgets.trivia_widgets.answers_panel.\
    with_images import APWithImages


class TriviaLevelVideoImages(TriviaLevelMediaMedias):
    """Trivia level with video-based question panel and image-based \
        answer panel."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)
        self.question_panel = QPWithVideo(self.question_to_media_path)
        self.answer_panel = APWithImages(
            self.answers_to_media_path, self.correct_answer, self.question
        )
        self.interactive_panel = InteractivePanelMediaWithMedias(
            self.question_panel,
            self.answer_panel
        )
        self.question_panel.play_question_video()
