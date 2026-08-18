from PySide6 import QtCore as QtC

from src.view_design.custom_widgets.scrollable_containers.vlayout import \
    QScrollAreaWithVLayout
from src.model.root_dir_trivia_extractor.brain import RootDirTriviaExtractor
from src.view_design.pages.trivia_menu.trivia_container.brain \
    import TriviaArea
from src.model.configurators.trivia_pinner_handler import TriviaPinner
from src.view_design.page_design_toolkit import (
    cleaner, expander)


class TriviaMenu(QScrollAreaWithVLayout):
    """QScrollAreaWithVLayout that builds and contains all individual trivia
    areas using the RootDir Trivia Extractor."""

    def __init__(self, parent_widget):
        super().__init__()

        self.parent_widget = parent_widget
        self.root_dir_trivia_extractor = RootDirTriviaExtractor()
        self.trivias_filepath_to_info \
            = self.root_dir_trivia_extractor.get_trivias_filepaths_to_info()
        self.trivias_area = self._build_trivia_area_layout()
        expander.expand_layout(self.container_layout)

    def _build_trivia_area_layout(self):
        trivias_area = []
        for filepath, trivia_info in self.trivias_filepath_to_info.items():
            trivia_area = self._build_trivia_area(filepath, trivia_info)
            self.container_layout.setAlignment(QtC.Qt.AlignmentFlag.AlignTop)
            self.container_layout.addWidget(
                trivia_area,
                alignment=QtC.Qt.AlignmentFlag.AlignTop
            )
            trivias_area.append(trivia_area)
        return trivias_area

    def _build_trivia_area(self, trivia_filepath, trivia_info):
        trivia_area \
            = TriviaArea(trivia_filepath, trivia_info, self.parent_widget)

        trivia_area.sgn_deletion_completed.connect(
            lambda path=trivia_filepath:
                self._on_deletion_completed(path)
        )
        trivia_area.sgn_pin_status_changed.connect(self._update_trivia_items)
        return trivia_area

    def _on_deletion_completed(self, trivia_filepath):
        trivia_pinner_handler = TriviaPinner(trivia_filepath)
        if trivia_pinner_handler.is_pinned:
            trivia_pinner_handler.unpin_trivia()
        self._update_trivia_items()

    def _update_trivia_items(self):
        cleaner.clear_layout(self.container_layout)
        self.root_dir_trivia_extractor = RootDirTriviaExtractor()
        self.root_dir_trivia_extractor.get_valid_trivias()
        self.trivias_filepath_to_info \
            = self.root_dir_trivia_extractor.get_trivias_filepaths_to_info()
        self.trivias_area = self._build_trivia_area_layout()
        expander.expand_layout(self.container_layout)
        self._update_trivia_items_size()

    def _update_trivia_items_size(self):
        default_height = int(self.height() // 6)
        default_width = int(self.width())
        for trivia_area in self.trivias_area:
            trivia_area.setFixedSize(default_width, default_height)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_trivia_items_size()
