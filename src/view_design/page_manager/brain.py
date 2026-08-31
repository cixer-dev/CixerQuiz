from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.audio_widgets.ambient_sound_player\
    import AmbientSoundPlayer
from src.view_design.page_manager.root_widget.brain import RootWidget
from src.view_design.in_quiz.brain import InQuiz
from src.view_design.custom_animations.transition.brain import SceneTransition
from src.model.translation_handler import _


class MainStack(QtW.QStackedWidget):
    """Main stacked widget of the app"""
    def __init__(self):
        super().__init__()
        self.ambient_sound_player = AmbientSoundPlayer()

        self.root_widget = RootWidget(self)
        self.root_widget.sgn_in_quiz.connect(self.switch_to_in_quiz)

        self.addWidget(self.root_widget)
        self.setCurrentWidget(self.root_widget)

        self.show()

    def switch_to_in_quiz(self, quiz_filepath):
        in_quiz = InQuiz(self, quiz_filepath)
        self.addWidget(in_quiz)
        transition = SceneTransition(
            parent_stack=self,
            duration=7000,
            optional_msg=_("The quiz is loading. Please wait a moment...")
        )
        transition.sgn_timeout.connect(
            lambda: self.setCurrentWidget(in_quiz)
        )

    def switch_to_quiz_menu(self):
        self.setCurrentWidget(self.root_widget)
        self.root_widget.switch_to_quiz_menu()

    def switch_to_root_dir(self):
        self.setCurrentWidget(self.root_widget)
