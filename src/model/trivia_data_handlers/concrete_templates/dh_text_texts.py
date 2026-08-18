from src.model.trivia_data_handlers.concrete_templates.brain \
    import DataHandlerTemplate
from src.model.trivia_data_handlers.data_extractors.answers.\
    without_media import AnswersWithoutMedia
from src.model.trivia_data_handlers.data_extractors.questions.\
    without_media import QuestionsWithoutMedia


class DHTextTexts(DataHandlerTemplate):
    """
    Extract, process, and provide data for one TEXT_TEXTS trivia level.
    """

    def __init__(self, level_path: str, duration: int) -> None:
        super().__init__(
            "TEXT_TEXTS",
            level_path,
            duration
            )

        self.question_dh = QuestionsWithoutMedia(
            level_path, self.random_index
        )
        self.answers_dh = AnswersWithoutMedia(
            level_path, self.random_index
        )
        self.question = self.question_dh.get_question()
        self.answers = self.answers_dh.get_answers()
        self.correct_answer = self.answers_dh.get_correct_answer()

        self._set_question(self.question)
        self._set_answers(self.answers)
        self._set_correct_answer(self.correct_answer)
