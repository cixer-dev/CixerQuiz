from src.model.trivia_data_handlers.data_extractors.questions.brain import (
    QuestionsDataExtractor,
)


class QuestionsWithoutMedia(QuestionsDataExtractor):
    """Extract question data without media for one generic trivia level."""

    def __init__(self, level_path: str, random_index: int) -> None:
        """Initialize and select a question without media."""
        super().__init__(level_path, random_index)

    def get_question(self) -> str:
        """Return the selected question."""
        return self.question  # type: ignore
