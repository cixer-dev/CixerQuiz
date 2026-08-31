from src.view_design.in_quiz.quizzes_templates.brain import (
    QuizLevelTemplate,
)


class QuizLevelTextMedias(QuizLevelTemplate):
    """Template representing the data and graphical structure of an abstract
    text-medias quiz level."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)
        self.question = self.data["question"]
        self.answers_to_media_path = self.data["answers"]
