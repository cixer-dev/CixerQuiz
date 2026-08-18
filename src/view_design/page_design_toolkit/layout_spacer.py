def set_vertical_space(widget_container, layout, divide_proportion=10):
    """Sets the layout's vertical spacing based on the container height\
    divided by a proportion."""
    vertical_space = _build_vertical_space(widget_container, divide_proportion)
    layout.setVerticalSpacing(vertical_space)


def _build_vertical_space(widget_container, divide_proportion):
    """Computes a vertical spacing value from the container height divided\
    by a proportion."""
    total_vertical_space = widget_container.height()
    vertical_space = total_vertical_space // divide_proportion
    return vertical_space
