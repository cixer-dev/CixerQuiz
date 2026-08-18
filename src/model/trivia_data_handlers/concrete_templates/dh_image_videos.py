from src.model.trivia_data_handlers.concrete_templates.brain \
    import DataHandlerTemplate
from src.model.trivia_data_handlers.data_extractors.answers.\
    with_media import AnswersWithMedia
from src.model.trivia_data_handlers.data_extractors.questions.\
    with_media import QuestionsExtractorWithMedia


class DHImageVideos(DataHandlerTemplate):
    """
    Extract, process, and provide data for one IMAGE_VIDEOS trivia level.
    """

    def __init__(self, level_path: str, duration: int) -> None:
        super().__init__(
            "IMAGE_VIDEOS",
            level_path,
            duration
            )

        self.question_dh = QuestionsExtractorWithMedia(
            level_path, self.random_index
        )
        self.answers_dh = AnswersWithMedia(level_path, self.random_index)
        self.question = (
            self.question_dh.get_question_to_media_path()
        )
        self.answers = (
            self.answers_dh.get_answers_to_media_path()
        )
        self.correct_answer = self.answers_dh.get_correct_answer()

        self._set_question(self.question)
        self._set_answers(self.answers)
        self._set_correct_answer(self.correct_answer)
