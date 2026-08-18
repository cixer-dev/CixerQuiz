from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC


class FieldsWithPathTemplate(QtW.QGridLayout):
    """QGridLayout template containing a file path default_field."""
    sgn_path_changed = QtC.Signal(str)

    def __init__(
            self,
            parent_widget,
            field_title):
        super().__init__()
        self.parent_widget = parent_widget
        self.field_title = field_title
        self.default_field = None

    def _on_path_changed(self, path):
        self.sgn_path_changed.emit(path)

    def _set_default_field(self, default_field: QtW.QGridLayout):
        self.default_field = default_field

    def _set_5_to_95_column_proportion(self):
        self.setColumnStretch(0, 95)
        self.setColumnStretch(1, 5)
        if self.default_field:
            self.default_field.setColumnStretch(0, 6)
            self.default_field.setColumnStretch(1, 94)

    def set_20_to_80_column_proportion(self):
        self.setColumnStretch(0, 95)
        self.setColumnStretch(1, 5)
        if self.default_field:
            self.default_field.setColumnStretch(0, 21)
            self.default_field.setColumnStretch(1, 79)
