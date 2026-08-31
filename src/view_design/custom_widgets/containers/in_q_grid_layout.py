from PySide6 import QtWidgets as QtW


class ContainerInQGridLayout(QtW.QWidget):
    """QWidget container that inserts itself into a QGridLayout."""

    def __init__(self, grid_parent, row, column):
        super().__init__()
        self.grid_parent = grid_parent
        self.grid_parent.addWidget(self, row, column)
