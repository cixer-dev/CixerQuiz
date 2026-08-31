from src.view_design.custom_widgets.fields_with_path.template import \
    FieldsWithPathTemplate
from src.view_design.custom_widgets.custom_line_edits.field_for_path \
    import FieldForPath
from src.view_design.custom_widgets.file_system_buttons.\
    for_files_with_filters_code import FilesystemForFilesWithFilters


class FieldWithPathAndFilters(FieldsWithPathTemplate):
    """QGridLayout containing a file path default_field with a browse \
    button and filters."""

    def __init__(
        self,
        parent_widget,
        field_title,
        filters_code,
        predefined_text=None,
        text_placeholder=None,
    ):
        super().__init__(
            parent_widget,
            field_title
        )
        self.filters_code = filters_code
        self.predefined_text = predefined_text
        self.text_placeholder = text_placeholder
        self.field_path \
            = FieldForPath(
                self.field_title,
                self.text_placeholder,
                self.predefined_text
            )
        self.field_path.sgn_path_changed.connect(self._on_path_changed)
        self._set_default_field(self.field_path)

        self.open_filesystem_btn = FilesystemForFilesWithFilters(
            self.parent_widget,
            self.filters_code,
        )
        self.open_filesystem_btn.sgn_path_changed.connect(
            self.field_path.set_text
        )
        self.addLayout(self.field_path, 0, 0)
        self.addWidget(self.open_filesystem_btn, 0, 1)
        self._set_5_to_95_column_proportion()
