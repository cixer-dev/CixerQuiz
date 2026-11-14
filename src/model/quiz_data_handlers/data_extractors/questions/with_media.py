import os

from src.model.quiz_data_handlers.data_extractors.questions.brain import (
    QuestionsDataExtractor,
)


class QuestionsExtractorWithMedia(QuestionsDataExtractor):
    """Extract question text with associated media paths \
        for one quiz level."""

    def __init__(
        self,
        quiz_path: str,
        possible_questions: list[dict[str, str]],
        random_index: int
            ) -> None:
        """Initialize the extractor and compute question-to-media paths."""
        super().__init__(possible_questions, random_index)
        self.quiz_path = quiz_path
        self.question_to_media_path = self.get_question_to_media_path()

    def get_question_to_media_path(self) -> dict[str, str]:
        """Build a mapping from question text to the corresponding \
            media path."""
        question_to_media_path: dict[str, str] = {}

        for question, media_paths_unformatted in \
                self.question.items():  # type: ignore
            media_path = os.path.join(self.quiz_path, media_paths_unformatted)
            question_to_media_path[question] = media_path

        return question_to_media_path
