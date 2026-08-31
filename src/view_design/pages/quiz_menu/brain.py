from PySide6 import QtCore as QtC

from src.view_design.custom_widgets.scrollable_containers.vlayout import \
    QScrollAreaWithVLayout
from src.model.root_dir_quiz_extractor.brain import RootDirQuizExtractor
from src.view_design.pages.quiz_menu.quiz_container.brain \
    import QuizArea
from src.model.configurators.quiz_pinner_handler import QuizPinner
from src.view_design.page_design_toolkit import (
    cleaner, expander)


class QuizMenu(QScrollAreaWithVLayout):
    """QScrollAreaWithVLayout that builds and contains all individual quiz
    areas using the RootDir Quiz Extractor."""

    def __init__(self, parent_widget):
        super().__init__()

        self.parent_widget = parent_widget
        self.root_dir_quiz_extractor = RootDirQuizExtractor()
        self.quizzes_filepath_to_info \
            = self.root_dir_quiz_extractor.get_quizzes_filepaths_to_info()
        self.quizzes_area = self._build_quiz_area_layout()
        expander.expand_layout(self.container_layout)

    def _build_quiz_area_layout(self):
        quizzes_area = []
        for filepath, quiz_info in self.quizzes_filepath_to_info.items():
            quiz_area = self._build_quiz_area(filepath, quiz_info)
            self.container_layout.setAlignment(QtC.Qt.AlignmentFlag.AlignTop)
            self.container_layout.addWidget(
                quiz_area,
                alignment=QtC.Qt.AlignmentFlag.AlignTop
            )
            quizzes_area.append(quiz_area)
        return quizzes_area

    def _build_quiz_area(self, quiz_filepath, quiz_info):
        quiz_area \
            = QuizArea(quiz_filepath, quiz_info, self.parent_widget)

        quiz_area.sgn_deletion_completed.connect(
            lambda path=quiz_filepath:
                self._on_deletion_completed(path)
        )
        quiz_area.sgn_pin_status_changed.connect(self._update_quiz_items)
        return quiz_area

    def _on_deletion_completed(self, quiz_filepath):
        quiz_pinner_handler = QuizPinner(quiz_filepath)
        if quiz_pinner_handler.is_pinned:
            quiz_pinner_handler.unpin_quiz()
        self._update_quiz_items()

    def _update_quiz_items(self):
        cleaner.clear_layout(self.container_layout)
        self.root_dir_quiz_extractor = RootDirQuizExtractor()
        self.root_dir_quiz_extractor.get_valid_quizzes()
        self.quizzes_filepath_to_info \
            = self.root_dir_quiz_extractor.get_quizzes_filepaths_to_info()
        self.quizzes_area = self._build_quiz_area_layout()
        expander.expand_layout(self.container_layout)
        self._update_quiz_items_size()

    def _update_quiz_items_size(self):
        default_height = int(self.height() // 6)
        default_width = int(self.width())
        for quiz_area in self.quizzes_area:
            quiz_area.setFixedSize(default_width, default_height)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_quiz_items_size()
