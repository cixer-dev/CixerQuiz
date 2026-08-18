from typing import Any
import os
import random

from src.model.json_wrapper import reader


class DataHandlerTemplate:
    """Extract, process and provide data for one generic trivia level."""

    def __init__(
        self,
        level_type_id: str,
        level_path: str,
        duration: int
    ) -> None:
        self.LEVEL_TYPE_ID = level_type_id
        self.level_path = level_path
        self.duration = duration
        self.question = None
        self.answers = None
        self.correct_answer = None

        self.manifest_path = os.path.join(self.level_path, "manifest.json")
        self.num_questions = reader.read_json_key(
            self.manifest_path, "num_questions"
        )
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
            "trivia_duration": self.duration,
        }
