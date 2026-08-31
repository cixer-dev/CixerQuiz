from PySide6 import QtWidgets as QtW, QtCore as QtC, QtGui as QtG


class ImageLabel(QtW.QLabel):
    """QLabel that displays and scales images maintaining aspect ratio."""

    def __init__(self, image_path: str):
        super().__init__()
        self.image_path = image_path
        self.image_pixmap = QtG.QPixmap(self.image_path)
        self.setAlignment(QtC.Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("background-color: black;")

    def _update_image_size(self):
        scaled_image_size = self.size()
        scaled_image = self.image_pixmap.scaled(
            scaled_image_size,
            QtC.Qt.AspectRatioMode.KeepAspectRatio,
            QtC.Qt.TransformationMode.SmoothTransformation,
        )
        self.setPixmap(scaled_image)

    def resizeEvent(self, event: QtG.QResizeEvent):
        super().resizeEvent(event)
        self._update_image_size()
