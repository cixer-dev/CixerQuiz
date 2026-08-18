from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.configurators.assets_paths_configurator import (
    assets_paths_formatter,
    assets_paths_writer,
)
from src.model.configurators.accepted_formats_configurator import (
    accepted_formats_formatter,
)
from src.model.data_structure_formatter import paths_formatter
from src.model.data_structure_formatter import str_formatter
from src.model.translation_handler import _, translate_to_english
from src.view_design.custom_widgets.fields_with_path.\
    fields_with_path_and_filters import FieldWithPathAndFilters
from src.view_design.custom_widgets.plaintexts.big_header \
    import BigHeaderColored


class AssetsPathsPanel(QtW.QVBoxLayout):
    """QVBoxLayout that edits asset paths and emits when \
        configuration changes."""

    sgn_assets_config_changed = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
        self.assets_paths_label \
            = BigHeaderColored(_("Asset paths config"))
        self._build_assets_paths_label()
        self.title_to_asset_path = (
            assets_paths_formatter.build_formatted_title_to_asset_path()
        )
        self.assets_paths_fields = self._build_assets_paths_fields()
        self.assets_paths_containers = (
            self._build_assets_paths_containers()
        )
        self._add_assets_paths_containers()

    def _build_assets_paths_label(self):
        self.addWidget(self.assets_paths_label)

    def _build_assets_paths_fields(self):
        assets_paths_fields = []
        for title, asset_path in self.title_to_asset_path.items():
            suffix = paths_formatter.get_suffix(asset_path)
            filters_code = (
                accepted_formats_formatter.get_qdialog_filter_pattern(
                    suffix
                )
            )
            asset_path_field = FieldWithPathAndFilters(
                self.parent_widget,
                title,
                filters_code,
                predefined_text=asset_path,
            )
            asset_path_field.sgn_path_changed.connect(
                lambda filepath, translated_title: self._on_filepath_changed(
                    translated_title,
                    filepath,
                )
            )

            assets_paths_fields.append(asset_path_field)
            asset_path_field.set_20_to_80_column_proportion()
        return assets_paths_fields

    def _build_assets_paths_containers(self):
        assets_paths_containers = []
        for asset_path_field in self.assets_paths_fields:
            asset_path_container = QtW.QWidget()
            asset_path_container.setLayout(asset_path_field)
            assets_paths_containers.append(asset_path_container)
        return assets_paths_containers

    def _add_assets_paths_containers(self):
        for asset_path_container in self.assets_paths_containers:
            self.addWidget(asset_path_container)

    def _on_filepath_changed(self, translated_title, new_filepath):
        en_title = translate_to_english(translated_title)
        filepath_key = str_formatter.title_to_snake_case(en_title)
        assets_paths_writer.set_asset_filepath(filepath_key, new_filepath)
        self.sgn_assets_config_changed.emit()

    def update_sizes(self, config_size):
        default_height = config_size.height() // 10
        default_width = config_size.width()
        self.assets_paths_label.setMinimumSize(default_width, default_height)
        for asset_path_container in self.assets_paths_containers:
            asset_path_container.setMinimumSize(default_width, default_height)
