from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW


class FieldWithSpinBox(QtW.QGridLayout):
    """Field widget with spinbox input for numeric values."""

    sgn_field_content_changed = QtC.Signal(str)

    def __init__(self,
                 field_content,
                 default_value=None):
        super().__init__()
        self.field_content = field_content
        self.default_value = default_value

        self.field_label = QtW.QLabel(f"{field_content}:")
        self.field_line = self._build_field_line()

        self.addWidget(self.field_label, 0, 0)
        self.addWidget(self.field_line, 0, 1)

    def _build_field_line(self):
        field_spin_box = QtW.QSpinBox()
        field_spin_box.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding,
            QtW.QSizePolicy.Policy.Expanding
        )
        field_spin_box.textChanged.connect(self._emit_field_changed_signal)
        if self.default_value:
            field_spin_box.setValue(int(self.default_value))
        else:
            raise ValueError(
                f"Default value {self.default_value} is an integer"
            )
        return field_spin_box

    def _emit_field_changed_signal(self, field_content):
        self.sgn_field_content_changed.emit(field_content)

    def set_value(self, new_text):
        self.field_line.setValue(new_text)
