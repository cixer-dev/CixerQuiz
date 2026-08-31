from PySide6 import QtWidgets as QtW


class StandardContainer(QtW.QWidget):
    """QWidget container that adds itself to a given layout."""

    def __init__(self, layout_parent=None, layout_inside=None):
        super().__init__()
        self.grid_parent = layout_parent
        self.layout_inside = layout_inside
        if self.grid_parent:
            self.grid_parent.addWidget(self)
        if self.layout_inside:
            self.setLayout(self.layout_inside)
