from PySide6 import QtWidgets as QtW

from src.view_design.in_trivia.trivias_templates.abstract_levels.text_texts.\
    brain import TriviaLevelsTextTexts
from src.view_design.in_trivia.trivias_templates.abstract_levels.text_medias.\
    concrete_pages.text_images import TriviaLevelTextImages
from src.view_design.in_trivia.trivias_templates.abstract_levels.media_texts.\
    concrete_pages.image_texts import TriviaLevelImageTexts
from src.view_design.in_trivia.trivias_templates.abstract_levels.media_medias.\
    concrete_pages.image_images import TriviaLevelImageImages
from src.view_design.in_trivia.trivias_templates.abstract_levels.media_texts.\
    concrete_pages.video_texts import TriviaLevelVideoTexts
from src.view_design.in_trivia.trivias_templates.abstract_levels.text_medias.\
    concrete_pages.text_videos import TriviaLevelTextVideos
from src.view_design.in_trivia.trivias_templates.abstract_levels.media_medias.\
    concrete_pages.video_videos import TriviaLevelVideoVideos
from src.view_design.in_trivia.trivias_templates.abstract_levels.media_medias.\
    concrete_pages.video_images import TriviaLevelVideoImages
from src.view_design.in_trivia.trivias_templates.abstract_levels.media_medias.\
    concrete_pages.image_videos import TriviaLevelImageVideos
from src.view_design.in_trivia.game_over.GO_incorrect_answer.brain import (
    GOIncorrectAnswer,
)
from src.view_design.in_trivia.game_over.GO_timeout.brain import GOTimeout
from src.view_design.in_trivia.victory_screen.brain import VictoryScreen
from src.model.trivia_data_handlers.brain import TriviaDataHandler
from src.view_design.custom_animations.transition.brain import SceneTransition

from src.model.translation_handler import _


class InTrivia(QtW.QStackedWidget):
    """Stacked trivia widget that builds and navigates level pages."""

    def __init__(self, main_stack, trivia_path):
        super().__init__()
        self.main_stack = main_stack
        self.trivia_path = trivia_path
        self.LEVEL_TYPE_ID_TO_PANEL_CLASS = {
            "TEXT_TEXTS": TriviaLevelsTextTexts,
            "TEXT_IMAGES": TriviaLevelTextImages,
            "TEXT_VIDEOS": TriviaLevelTextVideos,
            "IMAGE_TEXTS": TriviaLevelImageTexts,
            "IMAGE_IMAGES": TriviaLevelImageImages,
            "IMAGE_VIDEOS": TriviaLevelImageVideos,
            "VIDEO_TEXTS": TriviaLevelVideoTexts,
            "VIDEO_IMAGES": TriviaLevelVideoImages,
            "VIDEO_VIDEOS": TriviaLevelVideoVideos
        }
        self.trivia_data_handler = TriviaDataHandler(trivia_path)
        self.dh_levels = self.trivia_data_handler.get_dh_levels()
        self._append_levels_to_trivia()
        self.num_levels = len(self.dh_levels)
        self.actual_level = 0
        self.setCurrentIndex(0)

    def _append_levels_to_trivia(self):
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
        data_for_display["trivia_path"] = self.trivia_path
        game_over_for_incorrect_answer \
            = GOIncorrectAnswer(self.main_stack, data_for_display)
        self.addWidget(game_over_for_incorrect_answer)
        self.setCurrentWidget(game_over_for_incorrect_answer)

    def _switch_to_game_over_for_timeout(self):
        game_over_for_timeout = GOTimeout(self.main_stack, self.trivia_path)
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
