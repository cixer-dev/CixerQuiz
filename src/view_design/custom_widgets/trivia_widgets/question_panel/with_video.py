from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.trivia_widgets.interactive_video import (
    InteractiveVideo,
)
from src.view_design.custom_widgets.trivia_widgets.question_panel.\
    only_plaintext import QPOnlyPlaintext


class QPWithVideo(QtW.QWidget):
    """A grid layout that displays a question_text and an associated video."""

    def __init__(self, question_to_video_path):
        super().__init__()
        for question, video_path in question_to_video_path.items():
            self.question = question
            self.video_path = video_path

        self.grid_container = QtW.QGridLayout()
        question_label = QPOnlyPlaintext(self.question)
        self.question_video = InteractiveVideo(self.video_path)
        self.play_question_video()

        self.grid_container.addWidget(question_label, 0, 0)
        self.grid_container.addWidget(self.question_video, 1, 0)

        self.grid_container.setRowStretch(0, 30)
        self.grid_container.setRowStretch(1, 70)
        self.setLayout(self.grid_container)

    def play_question_video(self):
        self.question_video.play_player()
