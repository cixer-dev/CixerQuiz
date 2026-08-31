from PySide6 import QtCore as QtC

from src.model.translation_handler import _
from src.view_design.custom_widgets.containers.standard \
    import StandardContainer
from src.view_design.custom_widgets.scrollable_containers.vlayout \
    import QScrollAreaWithVLayout
from src.view_design.page_design_toolkit import cleaner, expander
from src.view_design.pages.quiz_builder.area.description_field \
    import DescriptionField
from src.view_design.pages.quiz_builder.area.duration_field \
    import DurationField
from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.brain import LevelsContainerField
from src.view_design.pages.quiz_builder.area.name_field \
    import NameField
from src.view_design.pages.quiz_builder.area.num_levels_field \
    import NumLevelsField


class QuizBuilderArea(QScrollAreaWithVLayout):
    """QScrollAreaWithVLayout that aggregates quiz fields and emits \
        manifest/levels changes."""

    sgn_total_size_changed = QtC.Signal(object)
    sgn_levels_data_changed = QtC.Signal(list)
    sgn_manifest_data_changed = QtC.Signal(dict)

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget

        self.name = _("New quiz")
        self.description = ""
        self.duration = 60
        self.num_levels = 1

        self.container_layout.setAlignment(
            QtC.Qt.AlignmentFlag.AlignTop | QtC.Qt.AlignmentFlag.AlignLeft
        )
        self.name_field_container = StandardContainer(
            self.container_layout
        )
        self.description_field_container = StandardContainer(
            self.container_layout
        )
        self.duration_field_container = StandardContainer(
            self.container_layout
        )
        self.num_levels_container = StandardContainer(
            self.container_layout
        )
        self.levels_field_container = StandardContainer(
            self.container_layout
        )

        self.name_field = self._build_name_field()
        self.description_field = self._build_description_field()
        self.duration_field = self._build_duration_field()
        self.num_levels_field = self._build_num_levels_field()
        self.levels_field = self._build_levels_field()

        self.update_fields_size()
        expander.expand_layout(self.container_layout)

    def _build_name_field(self):
        name_field = NameField(self.name)
        name_field.sgn_field_content_changed.connect(self._on_name_changed)
        self.name_field_container.setLayout(name_field)
        return name_field

    def _build_description_field(self):
        description_field = DescriptionField(self.description)
        description_field.sgn_field_content_changed.connect(
            self._on_description_changed
        )
        self.description_field_container.setLayout(description_field)
        return description_field

    def _build_duration_field(self):
        duration_field = DurationField(self.duration)
        duration_field.sgn_field_content_changed.connect(
            self._on_duration_changed
        )
        self.duration_field_container.setLayout(duration_field)
        return duration_field

    def _build_num_levels_field(self):
        num_levels_field = NumLevelsField(self.num_levels)
        num_levels_field.sgn_field_content_changed.connect(
            self._on_num_levels_changed
        )
        self.num_levels_container.setLayout(num_levels_field)
        return num_levels_field

    def _build_levels_field(self):
        levels_field = LevelsContainerField(
            self.parent_widget,
            self.num_levels
        )
        self.levels_field_container.setLayout(levels_field)
        self._build_levels_field_connections(levels_field)
        self.update_fields_size()
        return levels_field

    def _build_levels_field_connections(self, levels_field):
        self.sgn_total_size_changed.connect(levels_field.update_size)
        levels_field.sgn_levels_data_changed.connect(
            self._on_levels_data_changed
        )
        levels_field.sgn_level_field_was_rebuild.connect(
            self.update_fields_size
        )

    def _on_num_levels_changed(self, num_levels):
        if not num_levels:
            num_levels = 1
        self.num_levels = int(num_levels)
        self._rebuild_levels_field()
        self._on_manifest_changed()

    def _rebuild_levels_field(self):
        self._rebuilt_levels_field_container()
        self.levels_field = self._build_levels_field()

    def _rebuilt_levels_field_container(self):
        cleaner.clear_container(self.levels_field_container)
        self.levels_field_container = StandardContainer(self.container_layout)

    def _on_name_changed(self, new_name):
        self.name = new_name
        self._on_manifest_changed()

    def _on_description_changed(self, new_description):
        self.description = new_description
        self._on_manifest_changed()

    def _on_duration_changed(self, new_duration):
        if not new_duration:
            self.duration = 60
        else:
            self.duration = new_duration
            self._on_manifest_changed()

    def _on_manifest_changed(self):
        self.quiz_manifest = {
            "is_valid_quiz": True,
            "num_levels": self.num_levels,
            "quiz_name": self.name,
            "quiz_description": self.description,
            "quiz_duration": int(self.duration) * 1000,
        }
        self.sgn_manifest_data_changed.emit(self.quiz_manifest)

    def _on_levels_data_changed(self, new_levels_data):
        self.levels_data = new_levels_data
        self.sgn_levels_data_changed.emit(self.levels_data)

    def update_fields_size(self):
        tb_area_size = self.size()
        default_width = tb_area_size.width()
        default_height = tb_area_size.height() // 10
        containers_with_default_size = [
            self.description_field_container,
            self.duration_field_container,
            self.name_field_container,
            self.num_levels_container,
        ]
        for container in containers_with_default_size:
            container.setMaximumWidth(default_width)
            container.setFixedHeight(default_height)
        self.sgn_total_size_changed.emit(tb_area_size)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_fields_size()
