from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.configurators.audio_configurator import (
    audio_config_formatter,
    audio_config_writer,
)
from src.model.translation_handler import translate_to_english, _
from src.model.data_structure_formatter import str_formatter
from src.view_design.custom_widgets.field_with_slider import FieldWithSlider
from src.view_design.custom_widgets.plaintexts.big_header \
    import BigHeaderColored


class AudioPanel(QtW.QVBoxLayout):
    """QVBoxLayout that edits audio volumes and emits when \
        configuration changes."""

    sgn_audio_config_changed = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
        self.audio_panel_label = BigHeaderColored(_("Audio config"))
        self._build_audio_config_label()
        self.volume_key_to_value = (
            audio_config_formatter.get_formatted_volume_key_to_value()
        )
        self.volume_sliders = self._build_volume_sliders()
        self._add_volume_sliders_to_panel()
        self._build_column_proportion()

    def _build_audio_config_label(self):
        self.addWidget(self.audio_panel_label)

    def _build_volume_sliders(self):
        volume_sliders = []
        for volume_key_title, volume_value in self.volume_key_to_value.items():
            volume_slider = FieldWithSlider(volume_key_title, volume_value)
            volume_slider.sgn_value_was_changed.connect(
                lambda value, key_title=volume_key_title:
                    self._on_volume_sliders_changed(
                        key_title,
                        value,
                    )
                )
            volume_sliders.append(volume_slider)
        return volume_sliders

    def _add_volume_sliders_to_panel(self):
        for volume_slider in self.volume_sliders:
            self.addWidget(volume_slider)

    def _build_column_proportion(self):
        for volume_slider in self.volume_sliders:
            volume_slider.set_column_stretch(0, 20)
            volume_slider.set_column_stretch(1, 80)

    def _on_volume_sliders_changed(self, volume_key_title, volume_value):
        en_volume_key_title \
            = translate_to_english(volume_key_title)
        volume_key_snake_case = str_formatter.title_to_snake_case(
            en_volume_key_title
        )
        volume_in_float_format = volume_value / 100
        audio_config_writer.set_volume(
            volume_key_snake_case,
            volume_in_float_format
        )
        self.sgn_audio_config_changed.emit()

    def update_sizes(self, config_size):
        default_height = config_size.height() // 10
        default_width = config_size.width()
        self.audio_panel_label.setMinimumSize(default_width, default_height)
        for volume_slider in self.volume_sliders:
            volume_slider.setMinimumSize(default_width, default_height)
