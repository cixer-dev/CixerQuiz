from src.view_design.in_trivia.trivias_templates.abstract_levels.media_medias.\
    brain import TriviaLevelMediaMedias

from src.view_design.custom_widgets.trivia_widgets.answers_panel.with_videos \
    import APWithVideos
from src.view_design.custom_widgets.trivia_widgets.interactive_panels.\
    media_with_medias import InteractivePanelMediaWithMedias
from src.view_design.custom_widgets.trivia_widgets.question_panel.with_video \
    import QPWithVideo


class TriviaLevelVideoVideos(TriviaLevelMediaMedias):
    """Trivia level with video-based widgets for question and answer panels."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)

        self.question_panel = QPWithVideo(self.question_to_media_path)
        self.answer_panel = APWithVideos(
            self.answers_to_media_path,
            self.correct_answer,
            self.question
            )
        self.interactive_panel = InteractivePanelMediaWithMedias(
            self.question_panel,
            self.answer_panel
        )
        self._build_interactive_panel()
