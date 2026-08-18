from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW


from src.view_design.custom_widgets.audio_widgets.sound_effects_player \
    import SoundEffectsPlayer


class GlobalFilter(QtC.QObject):
    """An event filter that plays a sound effect when QPushButtons are \
    pressed and toggles fullscreen on F11."""

    def __init__(self, app: QtW.QApplication):
        super().__init__()
        self.app = app
        self.sound_effects_player = SoundEffectsPlayer()

    def eventFilter(self, obj, event):
        if (
                event.type() == QtC.QEvent.Type.MouseButtonPress
                and isinstance(obj, QtW.QPushButton)
        ):
            self.sound_effects_player.play_sound_effect(
                "push_button_sound_effect"
            )
        if event.type() == QtC.QEvent.Type.KeyPress:
            if event.key() == QtC.Qt.Key.Key_F11:
                main_window = self.app.activeWindow()
                if main_window:
                    if main_window.isFullScreen():
                        main_window.showNormal()
                    else:
                        main_window.showFullScreen()
        return super().eventFilter(obj, event)
