from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW


class FieldWithSlider(QtW.QWidget):
    """A labeled horizontal QSlider that emits integer value changes."""

    sgn_value_was_changed = QtC.Signal(int)

    def __init__(self, title, default_value=0):
        super().__init__()

        self.title = title
        self.default_value = default_value

        self.container_grid = QtW.QGridLayout(self)

        self.title_label = QtW.QLabel(title)
        self.slider = QtW.QSlider(QtC.Qt.Orientation.Horizontal, self)
        self.slider.setRange(0, 100)
        self.slider.setValue(self.default_value)
        self.slider.valueChanged.connect(self._on_value_changed)

        self.container_grid.addWidget(self.title_label, 0, 0)
        self.container_grid.addWidget(self.slider, 0, 1)

    def set_column_stretch(self, column_position, stretch):
        self.container_grid.setColumnStretch(column_position, stretch)

    def _on_value_changed(self, slider_value):
        self.sgn_value_was_changed.emit(slider_value)
