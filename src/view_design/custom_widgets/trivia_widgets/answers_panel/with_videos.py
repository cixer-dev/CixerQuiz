from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.trivia_widgets.answers_panel.\
    template import APTemplate
from src.view_design.custom_widgets.trivia_widgets.interactive_video \
    import InteractiveVideo


class APWithVideos(APTemplate):
    """QWidget with interactive video answers and correctness signals."""

    def __init__(self, answers_to_video_path, correct_answer, question):
        super().__init__(correct_answer, question)
        self.answers_to_video_path = answers_to_video_path
        self.video_paths = list(self.answers_to_video_path.values())
        self.answers_videos = self._build_answers_videos()
        self.answer_btns = self._build_answer_btns()

        self.container_grid.setRowStretch(0, 80)
        self.container_grid.setRowStretch(1, 20)

    def _build_answers_videos(self):
        answers_videos = []
        for video_index, video_path in enumerate(self.video_paths):
            answer_video = InteractiveVideo(video_path)
            answer_video.is_pressed.connect(self.on_player_pressed)
            self.container_grid.addWidget(answer_video, 0, video_index)
            answers_videos.append(answer_video)
        return answers_videos

    def _build_answer_btns(self):
        answer_btns = []
        for answer_index, answer in enumerate(self.answers_to_video_path):
            answer_btn = QtW.QPushButton(answer)
            answer_btn.pressed.connect(
                lambda a=answer: self._send_answer_outcome(a)
            )
            self.container_grid.addWidget(answer_btn, 1, answer_index)
            answer_btns.append(answer_btn)
        return answer_btns

    def on_player_pressed(self, video_widget):
        for answer_video in self.answers_videos:
            if answer_video != video_widget:
                answer_video.pause_player()
