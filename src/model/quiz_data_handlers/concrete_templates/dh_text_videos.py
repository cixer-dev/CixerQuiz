from src.model.quiz_data_handlers.concrete_templates.brain \
    import DataHandlerTemplate
from src.model.quiz_data_handlers.data_extractors.answers.\
    with_media import AnswersWithMedia
from src.model.quiz_data_handlers.data_extractors.questions.\
    without_media import QuestionsWithoutMedia


class DHTextVideos(DataHandlerTemplate):
    """
    Extract, process, and provide data for one TEXT_VIDEOS quiz level.
    """

    def __init__(
        self,
        quiz_path: str,
        level_data: dict[str, dict],
        quiz_duration: int
    ) -> None:
        super().__init__(
            level_data,
            quiz_duration
            )
        self.quiz_path = quiz_path

        self.question_dh = QuestionsWithoutMedia(
            self.possible_questions, self.random_index
        )
        self.answers_dh = AnswersWithMedia(
            self.quiz_path,
            self.possible_answers,
            self.random_index
        )
        self.question = self.question_dh.get_question()
        self.answers = (
            self.answers_dh.get_answers_to_media_path()
        )
        self.correct_answer = self.answers_dh.get_correct_answer()

        self._set_question(self.question)
        self._set_answers(self.answers)
        self._set_correct_answer(self.correct_answer)
