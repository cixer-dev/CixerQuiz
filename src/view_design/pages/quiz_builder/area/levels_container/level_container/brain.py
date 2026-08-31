from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.brain import LevelField


class LevelsContainerField(QtW.QVBoxLayout):
    """QVBoxLayout container layout that manages multiple \
        LevelField widgets."""

    sgn_levels_data_changed = QtC.Signal(list)
    sgn_level_field_was_rebuild = QtC.Signal()

    def __init__(self, parent_widget, num_levels):
        super().__init__()

        self.parent_widget = parent_widget
        self.num_levels = num_levels
        self.levels_data = []
        self.levels_fields = []

        for level_index in range(self.num_levels):
            level_field = self._build_level(level_index)
            self._append_level_to_data(level_field)

    def _build_level(self, level_index):
        level_field = LevelField(self.parent_widget)
        level_field.sgn_level_data_changed.connect(
            lambda new_level_data, idx=level_index:
            self._on_level_data_changed(
                new_level_data, idx
            )
        )
        level_field.sng_level_field_was_rebuild.connect(
            self._on_level_field_was_rebuild
        )
        return level_field

    def _append_level_to_data(self, level_field):
        self.levels_fields.append(level_field)
        self.addLayout(level_field)

    def _on_level_data_changed(self, new_level_data, index):
        self._handler_length_list(self.levels_data, index)
        self.levels_data[index] = new_level_data
        self.sgn_levels_data_changed.emit(self.levels_data)

    @staticmethod
    def _handler_length_list(array, index):
        if len(array) <= index:
            needed_list_positions = index - len(array) + 1
            array.extend([{}] * needed_list_positions)

    def _on_level_field_was_rebuild(self):
        self.sgn_level_field_was_rebuild.emit()

    def update_size(self, tb_area_size):
        if self.levels_fields:
            for level_field in self.levels_fields:
                level_field.update_size(tb_area_size)
