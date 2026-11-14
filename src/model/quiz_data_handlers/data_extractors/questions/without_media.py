from src.model.quiz_data_handlers.data_extractors.questions.brain import (
    QuestionsDataExtractor,
)


class QuestionsWithoutMedia(QuestionsDataExtractor):
    """Extract question data without media for one generic quiz level."""

    def __init__(
        self,
        possible_questions: list[str],
        random_index: int
            ) -> None:
        """Initialize and select a question without media."""
        super().__init__(possible_questions, random_index)

    def get_question(self) -> str:
        """Return the selected question."""
        return self.question  # type: ignore
