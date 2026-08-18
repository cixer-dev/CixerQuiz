from PySide6 import QtWidgets as QtW
from src.view_design.custom_animations import up_down_to_up


class LevelLabel(QtW.QLabel):
    """A QLabel subclass used to display the level text."""

    def __init__(self, text: str):
        self.text = f"#{text}"  # type: ignore
        super().__init__(self.text)  # type: ignore

    def _update_size(self):
        self.widget_size = min(self.width(), self.height())
        up_down_to_up.move_up_to_down(self, travel=3)
        self.setMaximumSize(self.widget_size + 1, self.widget_size + 1)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self._update_size()
