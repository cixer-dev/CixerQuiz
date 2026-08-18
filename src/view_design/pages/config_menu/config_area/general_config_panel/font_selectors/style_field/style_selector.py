from PySide6 import QtCore as QtC
from PySide6 import QtGui as QtG
from PySide6 import QtWidgets as QtW

from src.model.configurators.general_configurator import (
    general_reader,
    general_writer,
)


class StyleSelector(QtW.QComboBox):
    """QComboBox that lists available font styles for a family and persists \
        the selection."""

    sgn_style_changed = QtC.Signal()

    def __init__(self, parent_widget, family):
        super().__init__()

        self.parent_widget = parent_widget
        self.current_font_style \
            = general_reader.read_general_config("font_style")
        self.font_styles = QtG.QFontDatabase().styles(family)

        self.addItems(self.font_styles)
        self.setCurrentText(self.current_font_style)
        self.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding,
            QtW.QSizePolicy.Policy.Expanding
        )

        self.currentTextChanged.connect(self._on_font_styles_changed)

    def _on_font_styles_changed(self, new_font_style):
        general_writer.set_general_config("font_style", new_font_style)
        self.sgn_style_changed.emit()

    def update_style(self):
        self.current_font_style = self.font_styles[0]
        self.setCurrentText(self.current_font_style)
        self._on_font_styles_changed(self.current_font_style)
