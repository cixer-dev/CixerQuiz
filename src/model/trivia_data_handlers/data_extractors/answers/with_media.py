import os
import random

from src.model.trivia_data_handlers.data_extractors.answers.brain import (
    AnswerDataExtractor,
)


class AnswersWithMedia(AnswerDataExtractor):
    """Extract relevant data about answers with media from a generic \
        trivia level."""

    def __init__(self, level_path: str, random_index: int) -> None:
        """Initialize derived answer/media mappings for this trivia level."""
        super().__init__(level_path, random_index)
        self.correct_answer = next(iter(self.answers[0]))
        self.formatted_answers = self._get_formatted_answers_to_media_path()
        self.randomized_answers_to_media_path = (
            self._get_randomized_answers_to_media_path()
        )

    def _get_formatted_answers_to_media_path(self) -> dict[str, str]:
        """Build absolute media paths for each answer."""
        answers_to_media_path: dict[str, str] = {}
        for answer_to_media_path in self.answers:
            for answer, media_path_unformatted \
                    in answer_to_media_path.items():  # type: ignore
                media_path = os.path.join(
                    self.level_path,
                    media_path_unformatted,
                )
                answers_to_media_path[answer] = media_path
        return answers_to_media_path

    def _get_randomized_answers_to_media_path(self) -> dict[str, str]:
        """Shuffle answers while keeping their media paths."""
        answer_to_media_path_answers = list(self.formatted_answers.keys())
        random.shuffle(answer_to_media_path_answers)
        shuffled_answers_to_media_path: dict[str, str] = {}
        for answer in answer_to_media_path_answers:
            shuffled_answers_to_media_path[answer] \
                = self.formatted_answers[answer]
        return shuffled_answers_to_media_path

    def get_answers_to_media_path(self) -> dict[str, str]:
        """Return the randomized mapping from answers to media paths."""
        return self.randomized_answers_to_media_path

    def get_correct_answer(self) -> str:
        """Return the correct answer text."""
        return self.correct_answer

    def get_answer_len(self) -> int:
        """Return the number of randomized answers."""
        return len(self.randomized_answers_to_media_path)
