from src.view_design.custom_widgets.fields_with_path.template \
    import FieldsWithPathTemplate
from src.view_design.custom_widgets.custom_line_edits.field_for_path import (
    FieldForPath,
)
from src.view_design.custom_widgets.file_system_buttons.for_directory import (
    FilesystemButtonForDirectory,
)


class FieldWithDirectoryPath(FieldsWithPathTemplate):
    """QGridLayout containing a directory path default_field with a \
    browse button."""

    def __init__(
        self,
        parent_widget,
        field_title,
        predefined_text=None,
        placeholder=None,
    ):
        super().__init__(
            parent_widget,
            field_title
        )
        self.predefined_text = predefined_text
        self.placeholder = placeholder

        self.dirpath_field = FieldForPath(
            self.field_title,
            self.placeholder,
            self.predefined_text,
        )
        self.dirpath_field.sgn_path_changed.connect(self._on_path_changed)
        self._set_default_field(self.dirpath_field)

        self.open_filesystem_btn \
            = FilesystemButtonForDirectory(self.parent_widget)
        self.open_filesystem_btn.sgn_path_changed.connect(
            self.dirpath_field.set_text
        )

        self.addLayout(self.dirpath_field, 0, 0)
        self.addWidget(self.open_filesystem_btn, 0, 1)
        self._set_5_to_95_column_proportion()
