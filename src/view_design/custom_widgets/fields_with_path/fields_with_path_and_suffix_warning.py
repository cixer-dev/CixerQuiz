from src.view_design.custom_widgets.fields_with_path.template \
    import FieldsWithPathTemplate
from src.view_design.custom_widgets.custom_line_edits.field_for_path import (
    FieldForPath,
)
from src.view_design.custom_widgets.file_system_buttons.\
    for_files_with_suffix_warnings import FilesystemForFilesWithSuffixWarning


class FieldWithPathAndSuffixWarning(FieldsWithPathTemplate):
    """QGridLayout containing a file path default_field constrained \
    by a suffix."""

    def __init__(
        self,
        parent_widget,
        field_content,
        suffix,
        predefined_text=None,
        placeholder=None,
    ):
        super().__init__(
            parent_widget,
            field_content
        )
        self.suffix = suffix
        self.predefined_text = predefined_text
        self.placeholder = placeholder

        self.field_path = FieldForPath(
            self.field_title,
            self.placeholder,
            self.predefined_text,
        )
        self._set_default_field(self.field_path)

        self.open_filesystem_btn = FilesystemForFilesWithSuffixWarning(
            self.parent_widget,
            self.suffix,
        )
        self.open_filesystem_btn.sgn_path_changed.connect(
            self.field_path.set_text
        )

        self.addLayout(self.field_path, 0, 0)
        self.addWidget(self.open_filesystem_btn, 0, 1)
        self._set_5_to_95_column_proportion()
