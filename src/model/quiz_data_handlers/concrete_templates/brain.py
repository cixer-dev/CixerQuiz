from typing import Any
import random


class DataHandlerTemplate:
    """Extract, process and provide data for one generic quiz level."""

    def __init__(
        self,
        level_data: dict[str, dict],
        duration: int
    ) -> None:
        self.level_manifest = level_data["manifest"]
        self.level_text_content = level_data["text_content"]
        self.possible_questions = self.level_text_content["questions"]
        self.possible_answers = self.level_text_content["answers"]
        self.LEVEL_TYPE_ID = self.level_manifest["level_type_id"]
        self.duration = duration
        self.question = None
        self.answers = None
        self.correct_answer = None
        self.num_questions = self.level_manifest["num_questions"]
        self.random_index = random.randrange(self.num_questions)

    def _set_question(self, question: str | dict[str, str]):
        self.question = question

    def _set_answers(self, answers: list[str] | dict[str, str]):
        self.answers = answers

    def _set_correct_answer(self, correct_answer: str):
        self.correct_answer = correct_answer

    def get_data_for_display(self) -> dict[str, Any] | None:
        """Return display data"""
        if not self.question:
            raise AttributeError("'question' attribute must be set before \
                retrieving display data.")
        if not self.answers:
            raise AttributeError("'answers' attribute must be set before \
                retrieving display data.")
        if not self.correct_answer:
            raise AttributeError("'correct_answer' attribute must be set \
                before retrieving display data.")

        return {
            "question": self.question,
            "answers": self.answers,
            "correct_answer": self.correct_answer,
            "quiz_duration": self.duration,
        }
