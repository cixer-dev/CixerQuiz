from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class TriviaIdField(QtW.QGridLayout):
    """QGridLayout that contain the visual structure and data of the trivia \
        id default field"""

    sgn_trivia_id_changed = QtC.Signal(str)

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
        self.trivias_front_to_trivia_id = {
            _("Question and answers only have texts"): "TEXT_TEXTS",
            _("Question only has text and the answers have images"):
                "TEXT_IMAGES",
            _("Question only has text and the answers have videos"):
                "TEXT_VIDEOS",
            _("Question has an image and the answers only have text"):
                "IMAGE_TEXTS",
            _("Question and answers have images"):
                "IMAGE_IMAGES",
            _("Question has an image and the answers have videos"):
                "IMAGE_VIDEOS",
            _("Question has a video and the answers only have text"):
                "VIDEO_TEXTS",
            _("Questions have videos and the answers have images"):
                "VIDEO_IMAGES",
            _("Question and answers have videos"):
                "VIDEO_VIDEOS",
        }

        self.selected_trivia_front \
            = _("Question and answers only have texts")
        self.selected_trivia_id = self._build_selected_trivia_code()
        self.questions_have_media = self._determine_questions_have_media(
            self.selected_trivia_id
        )
        self.answers_have_media = self._determine_answers_have_media(
            self.selected_trivia_id
        )
        self.filters_code = self._build_filter_code(self.selected_trivia_id)

        self.trivia_id_label = QtW.QLabel(_("Trivia type") + ":")
        self.trivia_id_box = self._build_trivia_id_box()
        self.addWidget(self.trivia_id_label, 0, 0)
        self.addWidget(self.trivia_id_box, 0, 1)
        self._set_column_proportion()

    def _build_selected_trivia_code(self):
        return self.trivias_front_to_trivia_id[self.selected_trivia_front]

    @staticmethod
    def _determine_questions_have_media(selected_trivia_id):
        trivia_codes_and_questions_status = {
            "TEXT_TEXTS": False,
            "TEXT_IMAGES": False,
            "TEXT_VIDEOS": False,
            "IMAGE_TEXTS": True,
            "IMAGE_IMAGES": True,
            "IMAGE_VIDEOS": True,
            "VIDEO_TEXTS": True,
            "VIDEO_IMAGES": True,
            "VIDEO_VIDEOS": True,
        }
        return trivia_codes_and_questions_status[selected_trivia_id]

    @staticmethod
    def _determine_answers_have_media(selected_trivia_id):
        trivia_codes_and_answers_status = {
            "TEXT_TEXTS": False,
            "TEXT_IMAGES": True,
            "TEXT_VIDEOS": True,
            "IMAGE_TEXTS": False,
            "IMAGE_IMAGES": True,
            "IMAGE_VIDEOS": True,
            "VIDEO_TEXTS": False,
            "VIDEO_IMAGES": True,
            "VIDEO_VIDEOS": True,
        }
        return trivia_codes_and_answers_status[selected_trivia_id]

    @staticmethod
    def _build_filter_code(selected_trivia_id):
        trivia_codes_to_filter_media_status = {
            "TEXT_TEXTS": (None, None),
            "TEXT_IMAGES": (None, "IMAGE"),
            "TEXT_VIDEOS": (None, "VIDEO"),
            "IMAGE_TEXTS": ("IMAGE", None),
            "IMAGE_IMAGES": ("IMAGE", "IMAGE"),
            "IMAGE_VIDEOS": ("IMAGE", "VIDEO"),
            "VIDEO_TEXTS": ("VIDEO", None),
            "VIDEO_IMAGES": ("VIDEO", "IMAGE"),
            "VIDEO_VIDEOS": ("VIDEO", "VIDEO"),
        }
        return trivia_codes_to_filter_media_status[selected_trivia_id]

    def _build_trivia_id_box(self):
        trivias_id = list(self.trivias_front_to_trivia_id.keys())
        trivia_id_box = QtW.QComboBox()
        trivia_id_box.addItems(trivias_id)
        trivia_id_box.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding, QtW.QSizePolicy.Policy.Expanding
        )
        trivia_id_box.currentTextChanged.connect(self._on_trivia_id_changed)
        return trivia_id_box

    def _on_trivia_id_changed(self, new_trivia_id):
        self.selected_trivia_front = new_trivia_id
        self.selected_trivia_id = self._build_selected_trivia_code()
        self.questions_have_media = self._determine_questions_have_media(
            self.selected_trivia_id
        )
        self.answers_have_media = self._determine_answers_have_media(
            self.selected_trivia_id
        )
        self.filters_code = self._build_filter_code(self.selected_trivia_id)
        self.sgn_trivia_id_changed.emit(self.selected_trivia_id)

    def _set_column_proportion(self):
        self.setColumnStretch(0, 10)
        self.setColumnStretch(1, 90)

    def get_filter_code(self):
        return self.filters_code

    def get_questions_have_media(self):
        return self.questions_have_media

    def get_answers_have_media(self):
        return self.answers_have_media
