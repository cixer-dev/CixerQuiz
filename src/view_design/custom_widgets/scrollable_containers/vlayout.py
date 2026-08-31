from PySide6 import QtWidgets as QtW
from PySide6 import QtCore


class QScrollAreaWithVLayout(QtW.QScrollArea):
    """QScrollArea with QVBoxLayout without horizontal scrolling.
    Content automatically adapts to the available width."""

    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.widget_container = QtW.QWidget()
        self.widget_container.setObjectName("WithLargeTrianglesBackground")
        self.container_layout = QtW.QVBoxLayout()
        self.widget_container.setLayout(self.container_layout)
        self.setWidget(self.widget_container)
