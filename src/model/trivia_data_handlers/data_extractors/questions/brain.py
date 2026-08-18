import os

from src.model.json_wrapper import reader


class QuestionsDataExtractor:
    """Extract and provide one random question from the level JSON payload."""

    def __init__(self, level_path: str, random_index: int) -> None:
        """Initialize the extractor using the provided level path and index."""
        self.level_path = level_path
        self.random_index = random_index
        self.text_content_filepath \
            = os.path.join(level_path, "text_content.json")
        self.possible_questions: list[dict[str, str]] | list[str] \
            = reader.read_json_key(
            self.text_content_filepath, "questions"
        )
        self.question = self._choice_random_question()

    def _choice_random_question(self) -> dict[str, str] | str:
        """Select the question at the configured index."""
        question = self.possible_questions[self.random_index]
        return question
