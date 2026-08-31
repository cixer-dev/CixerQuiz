from src.view_design.custom_widgets.push_buttons.\
    standard_button_with_icon import StandardButtonWithIcon


class AddButton(StandardButtonWithIcon):
    """Generic QPushButton with an add icon."""

    def __init__(self):
        super().__init__(standard_icon_key="add_icon_path")
