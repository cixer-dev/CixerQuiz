from PySide6 import QtWidgets as QtW


def expand_layout(layout):
    """Recursively expands widgets contained in a layout."""
    layout_len = layout.count()
    for item_index in range(layout_len):
        item = layout.itemAt(item_index)
        widget = item.widget()
        sub_layout = item.layout()

        if sub_layout:
            expand_layout(sub_layout)
        elif widget:
            if is_compound_widget(widget):
                expand_widget_with_children(widget)
            else:
                expand_one_widget(widget)


def expand_one_widget(widget):
    """Set an individual widget to expanding image_size policies."""
    widget.setSizePolicy(
        QtW.QSizePolicy.Policy.Expanding,
        QtW.QSizePolicy.Policy.Expanding
    )


def expand_widget_list(widget_list):
    """Expand every widget in a list, including nested compound widgets."""
    for widget in widget_list:
        if is_compound_widget(widget):
            expand_widget_with_children(widget)
        else:
            expand_one_widget(widget)


def expand_widget_with_children(widget):
    """Expand all QWidget/QLayout children of a compound widget."""
    children_list = widget.children()
    for child in children_list:
        if isinstance(child, QtW.QWidget):
            if is_compound_widget(child):
                expand_widget_with_children(child)
            else:
                expand_one_widget(child)
        elif isinstance(child, QtW.QLayout):
            expand_layout(child)


def is_compound_widget(widget):
    """Heuristic: a widget is compound if it has any QWidget children."""
    return len(widget.children()) > 0
