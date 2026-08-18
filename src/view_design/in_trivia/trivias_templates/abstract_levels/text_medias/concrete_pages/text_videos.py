from src.view_design.in_trivia.trivias_templates.abstract_levels.text_medias.\
    brain import TriviaLevelTextMedias

from src.view_design.custom_widgets.trivia_widgets.answers_panel.with_videos \
    import APWithVideos
from src.view_design.custom_widgets.trivia_widgets.interactive_panels.\
    text_with_medias import InteractivePanelTextWithMedias
from src.view_design.custom_widgets.trivia_widgets.question_panel.\
    only_plaintext import QPOnlyPlaintext


class TriviaLevelTextVideos(TriviaLevelTextMedias):
    """Trivia level with text-based question panel and video-based \
        answer panel."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)

        self.question_panel = QPOnlyPlaintext(self.question)
        self.answer_panel = APWithVideos(
            self.answers_to_media_path, self.correct_answer, self.question
        )
        self.interactive_panel = InteractivePanelTextWithMedias(
            self.question_panel,
            self.answer_panel
        )

        self._build_answer_video_panel()
        self._build_answers_panel()
        self._build_interactive_panel()

    def _build_answer_video_panel(self):
        for answer_video in self.answer_panel.answers_videos:
            answer_video.is_pressed.connect(self.on_player_playing)

    def on_player_playing(self, video_path):
        for answer_panel in self.answer_panel.answers_videos:
            if answer_panel.video_path != video_path:
                answer_panel.pause_player()
