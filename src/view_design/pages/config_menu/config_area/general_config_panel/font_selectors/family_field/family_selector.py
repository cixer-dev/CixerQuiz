from PySide6 import QtCore as QtC
from PySide6 import QtGui as QtG
from PySide6 import QtWidgets as QtW

from src.model.configurators.general_configurator import (
    general_reader,
    general_writer,
)


class FamilySelector(QtW.QComboBox):
    """QComboBox that lists available font families and persists the \
        selected one."""

    sgn_family_changed = QtC.Signal(str)

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget

        font_db = QtG.QFontDatabase()
        self.font_families = font_db.families()
        self.family_selected \
            = general_reader.read_general_config("font_family")

        self.setEditable(True)
        self.addItems(self.font_families)
        self.setItemText(0, self.family_selected)
        self.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding,
            QtW.QSizePolicy.Policy.Expanding
        )
        self.currentIndexChanged.connect(self._on_font_family_changed)

    def _on_font_family_changed(self, font_index):
        self.family_selected = self.font_families[font_index]
        general_writer.set_general_config("font_family", self.family_selected)
        self.sgn_family_changed.emit(self.family_selected)

    def get_selected_family(self):
        return self.family_selected
