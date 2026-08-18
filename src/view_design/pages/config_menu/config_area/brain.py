from PySide6 import QtCore as QtC

from src.view_design.custom_widgets.scrollable_containers.vlayout \
    import QScrollAreaWithVLayout
from src.view_design.pages.config_menu.config_area.assets_paths_panel.brain \
    import AssetsPathsPanel
from src.view_design.pages.config_menu.config_area.audio_panel.brain \
    import AudioPanel
from src.view_design.pages.config_menu.config_area.general_config_panel.brain \
    import GeneralPanel
from src.view_design.pages.config_menu.config_area.standard_paths_panel.brain \
    import StandardsPathsPanel


class ConfigArea(QScrollAreaWithVLayout):
    """QScrollAreaWithVLayout container holding configuration panels \
        and propagating image_size updates."""

    sgn_size_was_updated = QtC.Signal(object)
    sgn_config_changed = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget

        general_panel = GeneralPanel(self.parent_widget)
        standard_paths_panel = StandardsPathsPanel(self.parent_widget)
        assets_paths_panel = AssetsPathsPanel(self.parent_widget)
        audio_panel = AudioPanel(self.parent_widget)

        self.sgn_size_was_updated.connect(general_panel.update_sizes)
        self.sgn_size_was_updated.connect(standard_paths_panel.update_sizes)
        self.sgn_size_was_updated.connect(assets_paths_panel.update_sizes)
        self.sgn_size_was_updated.connect(audio_panel.update_sizes)

        general_panel.sgn_general_config_changed.connect(
            self.sgn_config_changed.emit
        )
        standard_paths_panel.sgn_standard_config_changed.connect(
            self.sgn_config_changed.emit
        )
        assets_paths_panel.sgn_assets_config_changed.connect(
            self.sgn_config_changed.emit
        )
        audio_panel.sgn_audio_config_changed.connect(
            self.sgn_config_changed.emit
        )

        general_panel.sgn_general_panel_was_changed.connect(
            self._on_general_panel_was_changed
        )

        self.container_layout.addLayout(general_panel)
        self.container_layout.addLayout(standard_paths_panel)
        self.container_layout.addLayout(assets_paths_panel)
        self.container_layout.addLayout(audio_panel)

    def _on_general_panel_was_changed(self):
        self.update_sizes()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.update_sizes()

    def update_sizes(self):
        self.sgn_size_was_updated.emit(self.size() * 0.95)
