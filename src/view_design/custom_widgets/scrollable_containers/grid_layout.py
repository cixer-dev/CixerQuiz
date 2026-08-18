from PySide6 import QtWidgets as QtW


class QScrollAreaWithGridLayout(QtW.QScrollArea):
    """QScrollArea with an internal QWidget using a grid layout."""

    def __init__(self):
        super().__init__()
        self.setWidgetResizable(True)
        self.widget_container = QtW.QWidget()
        self.container_grid = QtW.QGridLayout()
        self.widget_container.setLayout(self.container_grid)
        self.setWidget(self.widget_container)
