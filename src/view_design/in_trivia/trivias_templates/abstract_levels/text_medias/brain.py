from src.view_design.in_trivia.trivias_templates.brain import (
    TriviaLevelTemplate,
)


class TriviaLevelTextMedias(TriviaLevelTemplate):
    """Template representing the data and graphical structure of an abstract
    text-medias trivia level."""

    def __init__(self, data_for_display):
        super().__init__(data_for_display)
        self.question = self.data["question"]
        self.answers_to_media_path = self.data["answers"]
