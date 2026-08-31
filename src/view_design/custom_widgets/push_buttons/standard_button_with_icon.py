from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC
from PySide6 import QtGui as QtG

from src.model.configurators.assets_paths_configurator \
    import assets_paths_reader


class StandardButtonWithIcon(QtW.QPushButton):
    """Generic QPushButton with a standard icon."""

    def __init__(
            self,
            standard_icon_key: str,
            icon_percent: None | float = None
            ):
        super().__init__("")
        self.icon_size_percent = self._get_icon_percent(icon_percent)
        self.icon_path: str \
            = assets_paths_reader.read_asset_path(standard_icon_key)
        self.icon = QtG.QIcon(self.icon_path)  # type: ignore
        self.setIcon(self.icon)  # type: ignore

    @staticmethod
    def _get_icon_percent(icon_percent: None | float) -> float:
        if icon_percent:
            return icon_percent
        else:
            return 0.7

    def _update_icon_size(self):
        self.minor_side = min(self.width(), self.height())
        self.minimum_size = int(self.minor_side * self.icon_size_percent)
        self.setIconSize(QtC.QSize(self.minimum_size, self.minimum_size))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_icon_size()
