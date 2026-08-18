import os

from src.model.trivia_data_handlers.data_extractors.questions.brain import (
    QuestionsDataExtractor,
)


class QuestionsExtractorWithMedia(QuestionsDataExtractor):
    """Extract question text with associated media paths \
        for one trivia level."""

    def __init__(self, level_path: str, random_index: int) -> None:
        """Initialize the extractor and compute question-to-media paths."""
        super().__init__(level_path, random_index)
        self.question_to_media_path = self.get_question_to_media_path()

    def get_question_to_media_path(self) -> dict[str, str]:
        """Build a mapping from question text to the corresponding \
            media path."""
        question_to_media_path: dict[str, str] = {}

        for question, media_paths_unformatted in \
                self.question.items():  # type: ignore
            media_path = os.path.join(self.level_path, media_paths_unformatted)
            question_to_media_path[question] = media_path

        return question_to_media_path
