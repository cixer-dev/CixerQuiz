from PySide6 import QtWidgets as QtW
from PySide6 import QtGui as QtG
from PySide6 import QtCore as QtC

from src.model.configurators.assets_paths_configurator \
    import assets_paths_reader


class BrandingWidget(QtW.QWidget):
    """QWidget that contains the game logo"""
    def __init__(self, parent=None):
        super().__init__(parent)

        logo_path = assets_paths_reader.read_asset_path("complete_game_logo")
        self.original_pixmap = QtG.QPixmap(logo_path)

        self.container_layout = QtW.QVBoxLayout(self)
        self.complete_game_logo_label = QtW.QLabel()
        self.complete_game_logo_label.setAlignment(
            QtC.Qt.AlignmentFlag.AlignCenter
        )

        self.container_layout.addWidget(self.complete_game_logo_label)
        self._rescale()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._rescale()

    def _rescale(self):
        scaled = self.original_pixmap.scaled(
            self.size(),
            QtC.Qt.AspectRatioMode.KeepAspectRatio,
            QtC.Qt.TransformationMode.SmoothTransformation
        )
        self.complete_game_logo_label.setPixmap(scaled)
