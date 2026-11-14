

class QuestionsDataExtractor:
    """Extract and provide one random question from the level JSON payload."""

    def __init__(
        self,
        possible_questions: list[dict[str, str]] | list[str],
        random_index: int
            ) -> None:
        """Initialize the extractor using the provided level path and index."""
        self.possible_questions = possible_questions
        self.random_index = random_index
        self.question = self._choice_random_question()

    def _choice_random_question(self) -> dict[str, str] | str:
        """Select the question at the configured index."""
        question = self.possible_questions[self.random_index]
        return question
