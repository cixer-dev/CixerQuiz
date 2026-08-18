from src.view_design.custom_widgets.push_buttons.\
    standard_button_with_icon import StandardButtonWithIcon


class StartTriviaButton(StandardButtonWithIcon):
    """QPushButton that starts the in-game trivia when pressed."""

    def __init__(self, trivia_filepath, parent_widget):
        super().__init__(standard_icon_key="start_icon_path")
        self.parent_widget = parent_widget
        self.pressed.connect(
            lambda:
                self.parent_widget.switch_to_in_trivia(trivia_filepath)
            )
