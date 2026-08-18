from src.view_design.in_trivia.trivias_templates.brain \
    import TriviaLevelTemplate


class TriviaLevelMediaTexts(TriviaLevelTemplate):
    """Template representing the data and graphical structure
    of an abstract media-text trivia level."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)
        self.question_to_media_path = self.data["question"]
        self.answers = self.data["answers"]
        self.question, self.question_media_path = next(iter(
            self.question_to_media_path.items()
            )
        )
