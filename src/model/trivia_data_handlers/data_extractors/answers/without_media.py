import random

from src.model.trivia_data_handlers.data_extractors.answers.brain import \
    AnswerDataExtractor


class AnswersWithoutMedia(AnswerDataExtractor):
    """
    Extract relevant data about answers without media from a generic \
        trivia level.
    """
    def __init__(self, level_path: str, random_index: int) -> None:
        super().__init__(level_path, random_index)
        self.correct_answer = self.answers[0]
        self.randomized_answers = self._get_randomized_answers()

    def _get_randomized_answers(self) -> list[str]:
        randomized_answers = self.answers.copy()
        random.shuffle(randomized_answers)
        return randomized_answers  # type: ignore

    def get_answers(self) -> list:
        return self.randomized_answers

    def get_correct_answer(self) -> str:
        return self.correct_answer  # type: ignore
