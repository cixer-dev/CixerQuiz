

class AnswerDataExtractor:
    """Extract relevant answer data without media for a generic quiz \
        level."""

    def __init__(
        self,
        possible_answers: list[list[dict[str, str]]] | list[list[str]],
        random_index: int
            ) -> None:
        self.random_index = random_index
        self.possible_answers: list[list[dict[str, str]]] | list[list[str]] = (
            possible_answers
        )
        self.answers: list[dict[str, str]] | list[str] \
            = self._choice_random_answers()

    def _choice_random_answers(self) -> list[dict[str, str]] | list[str]:
        """Select one answer by index from the available answers."""
        return self.possible_answers[self.random_index]

    def get_answer_len(self) -> int:
        """Return the number of available answers."""
        return len(self.possible_answers)
