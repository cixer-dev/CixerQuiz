from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _
from src.model.configurators.standard_paths_configurator \
    import standard_paths_formatter, standard_paths_writer
from src.model.data_structure_formatter import paths_formatter
from src.model.data_structure_inspector import paths_inspector
from src.view_design.custom_widgets.plaintexts.big_header \
    import BigHeaderColored
from src.view_design.custom_widgets.fields_with_path. \
    fields_with_directory_path import FieldWithDirectoryPath
from src.view_design.custom_widgets.fields_with_path. \
    fields_with_path_and_suffix_warning import FieldWithPathAndSuffixWarning


class StandardPathsPanel(QtW.QVBoxLayout):
    """QVBoxLayout for configuring standard filesystem paths."""

    sgn_standard_config_changed = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget

        self.standard_paths_label \
            = BigHeaderColored(_("Standard paths config"))
        self._build_standard_paths_label()
        self.title_to_standard_path = (
            standard_paths_formatter.get_formatted_title_to_standard_path()
        )
        self.standard_paths_fields = self._build_standard_paths_fields()
        self.standard_paths_containers \
            = self._build_standard_paths_containers()
        self._add_standard_paths_containers()

    def _build_standard_paths_label(self):
        self.addWidget(self.standard_paths_label)

    def _build_standard_paths_fields(self):
        standard_paths_fields = []

        for title, standard_path in self.title_to_standard_path.items():
            if paths_inspector.is_file(standard_path):
                suffix = paths_formatter.get_suffix(standard_path)
                standard_path_field = FieldWithPathAndSuffixWarning(
                    self.parent_widget,
                    title,
                    suffix,
                    predefined_text=standard_path,
                )
            else:
                standard_path_field = FieldWithDirectoryPath(
                    self.parent_widget,
                    title,
                    predefined_text=standard_path,
                )

            standard_path_field.sgn_path_changed.connect(
                lambda new_path, current_title=title: self._on_path_changed(
                    current_title,
                    new_path,
                )
            )

            standard_path_field.set_20_to_80_column_proportion()
            standard_paths_fields.append(standard_path_field)

        return standard_paths_fields

    def _on_filepath_changed(self, title, new_filepath):
        standard_paths_writer.set_standard_filepath_from_title(
            title,
            new_filepath,
        )
        self.sgn_standard_config_changed.emit()

    def _on_dirpath_changed(self, title, new_dirpath):
        standard_paths_writer.set_standard_filepath_from_title(
            title,
            new_dirpath,
        )
        self.sgn_standard_config_changed.emit()

    def _build_standard_paths_containers(self):
        standard_paths_containers = []

        for standard_path_field in self.standard_paths_fields:
            standard_path_container = QtW.QWidget()
            standard_path_container.setLayout(standard_path_field)
            standard_paths_containers.append(standard_path_container)

        return standard_paths_containers

    def _add_standard_paths_containers(self):
        for standard_path_container in self.standard_paths_containers:
            self.addWidget(standard_path_container)

    @staticmethod
    def _on_path_changed(title, filepath):
        standard_paths_writer.set_standard_filepath_from_title(title, filepath)

    def update_sizes(self, config_size):
        default_height = config_size.height() // 10
        default_width = config_size.width()
        self.standard_paths_label.setMinimumSize(default_width, default_height)

        for standard_path_container in self.standard_paths_containers:
            standard_path_container.setMinimumSize(
                default_width,
                default_height
            )
