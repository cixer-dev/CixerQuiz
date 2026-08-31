from src.model.quiz_data_handlers.concrete_templates.\
    brain import DataHandlerTemplate
from src.model.quiz_data_handlers.data_extractors.\
    questions.with_media import QuestionsExtractorWithMedia
from src.model.quiz_data_handlers.data_extractors.\
    answers.without_media import AnswersWithoutMedia


class DHVideoTexts(DataHandlerTemplate):
    """
    Extract, process, and provide data for one VIDEO_TEXTS quiz level.
    """

    def __init__(self, level_path: str, duration: int) -> None:
        super().__init__(
            "VIDEO_TEXTS",
            level_path,
            duration
            )

        self.question_dh = QuestionsExtractorWithMedia(
            level_path, self.random_index
        )
        self.answers_dh = AnswersWithoutMedia(
            level_path, self.random_index
        )
        self.question = (
            self.question_dh.get_question_to_media_path()
        )
        self.answers = self.answers_dh.get_answers()
        self.correct_answer = self.answers_dh.get_correct_answer()

        self._set_question(self.question)
        self._set_answers(self.answers)
        self._set_correct_answer(self.correct_answer)
