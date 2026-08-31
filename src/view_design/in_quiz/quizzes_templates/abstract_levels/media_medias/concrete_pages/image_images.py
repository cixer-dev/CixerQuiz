from src.view_design.in_quiz.quizzes_templates.abstract_levels.\
    media_medias.brain import QuizLevelMediaMedias
from src.view_design.custom_widgets.quiz_widgets.interactive_panels.\
    media_with_medias import InteractivePanelMediaWithMedias
from src.view_design.custom_widgets.quiz_widgets.question_panel.\
    with_image import QPWithImage
from src.view_design.custom_widgets.quiz_widgets.answers_panel.\
    with_images import APWithImages


class QuizLevelImageImages(QuizLevelMediaMedias):
    """Quiz level with image-based widgets for question and answer panels."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)

        self.question_panel = QPWithImage(self.question_to_media_path)
        self.answer_panel = APWithImages(
            self.answers_to_media_path, self.correct_answer, self.question
        )
        self.interactive_panel = InteractivePanelMediaWithMedias(
            self.question_panel,
            self.answer_panel
        )
        self._build_interactive_panel()
