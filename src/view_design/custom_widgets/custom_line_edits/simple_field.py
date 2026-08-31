from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW


class SimpleField(QtW.QGridLayout):
    """QGridLayout with text input and change signal."""

    sgn_field_content_changed = QtC.Signal(str)

    def __init__(self,
                 field_content,
                 placeholder=None,
                 default_value=None):
        super().__init__()
        self.text_placeholder = placeholder
        self.field_content = field_content
        self.default_value = default_value

        self.field_label = QtW.QLabel(f"{field_content}: ")
        self.field_line = self._build_field_line()

        self.addWidget(self.field_label, 0, 0)
        self.addWidget(self.field_line, 0, 1)

        self.setColumnStretch(0, 5)
        self.setColumnStretch(1, 95)

    def _build_field_line(self):
        field_line = QtW.QLineEdit()
        field_line.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding,
            QtW.QSizePolicy.Policy.Expanding
        )
        field_line.textChanged.connect(self._emit_field_changed_signal)
        if self.text_placeholder:
            field_line.setPlaceholderText(self.text_placeholder)
        if self.default_value:
            self.default_value = str(self.default_value)
            field_line.setText(self.default_value)
        return field_line

    def _emit_field_changed_signal(self, field_content):
        self.sgn_field_content_changed.emit(field_content)

    def set_text(self, new_text):
        self.field_line.setText(new_text)
