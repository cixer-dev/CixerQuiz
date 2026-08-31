from PySide6 import QtWidgets as QtW


def clear_layout(layout: QtW.QLayout):
    """Recursively removes and deletes all widgets and nested layouts in a \
        layout."""
    while layout.count():
        item = layout.takeAt(0)
        if item:
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()
                continue
            child_layout = item.layout()
            if child_layout:
                clear_layout(child_layout)
                child_layout.setParent(None)
                child_layout.deleteLater()


def clear_container(container: QtW.QWidget):
    """Deletes a container widget."""
    container.setParent(None)
    container.deleteLater()
