from src.view_design.in_quiz.quizzes_templates.brain \
    import QuizLevelTemplate


class QuizLevelMediaMedias(QuizLevelTemplate):
    """Template representing the data and graphical structure of \
        abstract media quiz levels."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)
        self.question_to_media_path = self.data["question"]
        self.answers_to_media_path = self.data["answers"]
        self.question, self.question_media_path = next(iter(
            self.question_to_media_path.items()
            )
        )
