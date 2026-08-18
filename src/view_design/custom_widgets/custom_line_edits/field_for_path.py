from PySide6 import QtCore as QtC

from src.view_design.custom_widgets.custom_line_edits.simple_field \
    import SimpleField


class FieldForPath(SimpleField):
    """Field widget for path selection with change signal emission."""

    sgn_path_changed = QtC.Signal(str)

    def __init__(
        self,
        field_title,
        placeholder_value=None,
        default_value=None
            ):
        super().__init__(
            field_title,
            placeholder_value,
            default_value)
        self.setColumnStretch(0, 5)
        self.setColumnStretch(1, 95)
        self._rebuild_field_line()

    def _rebuild_field_line(self):
        self.field_line.setReadOnly(True)
        self.sgn_field_content_changed.connect(self._on_path_changed)

    def _on_path_changed(self, path):
        self.sgn_path_changed.emit(path)
