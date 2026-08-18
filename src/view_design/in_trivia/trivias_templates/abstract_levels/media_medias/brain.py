from src.view_design.in_trivia.trivias_templates.brain \
    import TriviaLevelTemplate


class TriviaLevelMediaMedias(TriviaLevelTemplate):
    """Template representing the data and graphical structure of \
        abstract media trivia levels."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)
        self.question_to_media_path = self.data["question"]
        self.answers_to_media_path = self.data["answers"]
        self.question, self.question_media_path = next(iter(
            self.question_to_media_path.items()
            )
        )
