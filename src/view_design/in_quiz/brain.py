from PySide6 import QtWidgets as QtW

from src.view_design.in_quiz.quizzes_templates.abstract_levels.text_texts.\
    brain import QuizLevelsTextTexts
from src.view_design.in_quiz.quizzes_templates.abstract_levels.text_medias.\
    concrete_pages.text_images import QuizLevelTextImages
from src.view_design.in_quiz.quizzes_templates.abstract_levels.media_texts.\
    concrete_pages.image_texts import QuizLevelImageTexts
from src.view_design.in_quiz.quizzes_templates.abstract_levels.media_medias.\
    concrete_pages.image_images import QuizLevelImageImages
from src.view_design.in_quiz.quizzes_templates.abstract_levels.media_texts.\
    concrete_pages.video_texts import QuizLevelVideoTexts
from src.view_design.in_quiz.quizzes_templates.abstract_levels.text_medias.\
    concrete_pages.text_videos import QuizLevelTextVideos
from src.view_design.in_quiz.quizzes_templates.abstract_levels.media_medias.\
    concrete_pages.video_videos import QuizLevelVideoVideos
from src.view_design.in_quiz.quizzes_templates.abstract_levels.media_medias.\
    concrete_pages.video_images import QuizLevelVideoImages
from src.view_design.in_quiz.quizzes_templates.abstract_levels.media_medias.\
    concrete_pages.image_videos import QuizLevelImageVideos
from src.view_design.in_quiz.game_over.GO_incorrect_answer.brain import (
    GOIncorrectAnswer,
)
from src.view_design.in_quiz.game_over.GO_timeout.brain import GOTimeout
from src.view_design.in_quiz.victory_screen.brain import VictoryScreen
from src.model.quiz_data_handlers.brain import QuizDataHandler
from src.view_design.custom_animations.transition.brain import SceneTransition

from src.model.translation_handler import _


class InQuiz(QtW.QStackedWidget):
    """Stacked quiz widget that builds and navigates level pages."""

    def __init__(self, main_stack, quiz_path):
        super().__init__()
        self.main_stack = main_stack
        self.quiz_path = quiz_path
        self.LEVEL_TYPE_ID_TO_PANEL_CLASS = {
            "TEXT_TEXTS": QuizLevelsTextTexts,
            "TEXT_IMAGES": QuizLevelTextImages,
            "TEXT_VIDEOS": QuizLevelTextVideos,
            "IMAGE_TEXTS": QuizLevelImageTexts,
            "IMAGE_IMAGES": QuizLevelImageImages,
            "IMAGE_VIDEOS": QuizLevelImageVideos,
            "VIDEO_TEXTS": QuizLevelVideoTexts,
            "VIDEO_IMAGES": QuizLevelVideoImages,
            "VIDEO_VIDEOS": QuizLevelVideoVideos
        }
        self.quiz_data_handler = QuizDataHandler(quiz_path)
        self.dh_levels = self.quiz_data_handler.get_dh_levels()
        self._append_levels_to_quiz()
        self.num_levels = len(self.dh_levels)
        self.actual_level = 0
        self.setCurrentIndex(0)

    def _append_levels_to_quiz(self):
        for dh_level in self.dh_levels:
            data_for_display = dh_level.get_data_for_display()
            if data_for_display:
                data_for_display["actual_level"] \
                    = self.dh_levels.index(dh_level) + 1
            level_type_id = dh_level.LEVEL_TYPE_ID
            page = self._build_page(level_type_id, data_for_display)
            self.addWidget(page)

    def _build_page(self, level_type_id, data_for_display):
        level_page_class = self.LEVEL_TYPE_ID_TO_PANEL_CLASS[level_type_id]
        page = level_page_class(data_for_display)
        if self._verify_page_has_all_signals(page):
            page.sgn_timeout.connect(self._switch_to_game_over_for_timeout)
            page.sgn_pressed_answer_is_correct.connect(self._on_level_up)
            page.sgn_pressed_answer_is_incorrect.connect(
                self._switch_to_game_over_for_incorrect_answer
            )
        return page

    def _verify_page_has_all_signals(self, page):
        if self._verify_page_has_answers_signals(page) and \
                self._verify_page_has_timeout_signal(page):
            return True

    @staticmethod
    def _verify_page_has_answers_signals(page):
        if hasattr(page, "sgn_pressed_answer_is_correct") and \
                hasattr(page, "sgn_pressed_answer_is_incorrect"):
            return True
        else:
            raise RuntimeError(
                "Page of type", type(page), "do not has answers signals"
                )

    @staticmethod
    def _verify_page_has_timeout_signal(page):
        if hasattr(page, "sgn_timeout"):
            return True
        else:
            raise RuntimeError(
                "Page of type", type(page), "do not has timeout signal"
                )

    def _switch_to_game_over_for_incorrect_answer(self, data_for_display):
        data_for_display["quiz_path"] = self.quiz_path
        game_over_for_incorrect_answer \
            = GOIncorrectAnswer(self.main_stack, data_for_display)
        self.addWidget(game_over_for_incorrect_answer)
        self.setCurrentWidget(game_over_for_incorrect_answer)

    def _switch_to_game_over_for_timeout(self):
        game_over_for_timeout = GOTimeout(self.main_stack, self.quiz_path)
        self.addWidget(game_over_for_timeout)
        self.setCurrentWidget(game_over_for_timeout)

    def _on_level_up(self):
        if self.actual_level != self.num_levels - 1:
            self.actual_level += 1
            self.transition = SceneTransition(
                parent_stack=self,
                duration=5000,
                optional_msg=_(
                    "That answer is correct! Advancing to the next level..."
                )
            )
            self.transition.sgn_timeout.connect(
                lambda:
                    self.setCurrentIndex(self.actual_level)
                )
        else:
            self._switch_to_victory_screen()

    def _switch_to_victory_screen(self):
        victory_screen = VictoryScreen(self.main_stack)
        self.addWidget(victory_screen)
        self.setCurrentWidget(victory_screen)
