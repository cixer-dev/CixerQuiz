from src.view_design.in_quiz.quizzes_templates.brain \
    import QuizLevelTemplate


class QuizLevelMediaTexts(QuizLevelTemplate):
    """Template representing the data and graphical structure
    of an abstract media-text quiz level."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)
        self.question_to_media_path = self.data["question"]
        self.answers = self.data["answers"]
        self.question, self.question_media_path = next(iter(
            self.question_to_media_path.items()
            )
        )
