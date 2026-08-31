from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC
from PySide6 import QtGui as QtG

from src.model.configurators.assets_paths_configurator \
    import assets_paths_reader
from src.model.configurators.quiz_pinner_handler \
    import QuizPinner


class PinOrUnpinButton(QtW.QPushButton):
    """QPushButton that toggles the pinned quiz status using the \
    QuizPinner backend."""

    sgn_pin_status_changed = QtC.Signal()

    def __init__(self, quiz_filepath, parent_widget):
        super().__init__("")
        self.quiz_filepath = quiz_filepath
        self.parent_widget = parent_widget
        self.setCheckable(True)
        self.quiz_pinner_handler = QuizPinner(self.quiz_filepath)
        self.setChecked(self.quiz_pinner_handler.is_pinned)
        self.toggled.connect(self._on_button_toggled)
        self.icon_size_percent = 0.7
        self.icon_on_path \
            = assets_paths_reader.read_asset_path("pinned_icon_path")
        self.icon_off_path \
            = assets_paths_reader.read_asset_path("unpin_icon_path")
        self.icon_on = QtG.QIcon(self.icon_on_path)
        self.icon_off = QtG.QIcon(self.icon_off_path)
        self._update_icon_button()

    def _on_button_toggled(self, checked):
        self.quiz_pinner_handler.toggle_pin_status()
        self._update_icon_button()
        self.sgn_pin_status_changed.emit()

    def _update_icon_button(self):
        if self.isChecked():
            self.setIcon(self.icon_on)
        else:
            self.setIcon(self.icon_off)

    def _update_icon_size(self):
        self.minimum_side = min(self.width(), self.height())
        self.minimum_size = int(self.minimum_side * self.icon_size_percent)
        self.setIconSize(QtC.QSize(self.minimum_size, self.minimum_size))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_icon_size()
