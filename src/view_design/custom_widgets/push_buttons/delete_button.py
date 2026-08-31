from src.view_design.custom_widgets.push_buttons.\
    standard_button_with_icon import StandardButtonWithIcon


class DeleteButton(StandardButtonWithIcon):
    """Generic QPushButton for deleting operations."""

    def __init__(self):
        super().__init__(standard_icon_key="delete_icon_path")
