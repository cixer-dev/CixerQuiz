from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class QuizIdField(QtW.QGridLayout):
    """QGridLayout that contain the visual structure and data of the quiz \
        id default field"""

    sgn_quiz_id_changed = QtC.Signal(str)

    def __init__(self, parent_widget):
        super().__init__()
        self.parent_widget = parent_widget
        self.quizzes_front_to_quiz_id = {
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

        self.selected_quiz_front \
            = _("Question and answers only have texts")
        self.selected_quiz_id = self._build_selected_quiz_code()
        self.questions_have_media = self._determine_questions_have_media(
            self.selected_quiz_id
        )
        self.answers_have_media = self._determine_answers_have_media(
            self.selected_quiz_id
        )
        self.filters_code = self._build_filter_code(self.selected_quiz_id)

        self.quiz_id_label = QtW.QLabel(_("Quiz type") + ":")
        self.quiz_id_box = self._build_quiz_id_box()
        self.addWidget(self.quiz_id_label, 0, 0)
        self.addWidget(self.quiz_id_box, 0, 1)
        self._set_column_proportion()

    def _build_selected_quiz_code(self):
        return self.quizzes_front_to_quiz_id[self.selected_quiz_front]

    @staticmethod
    def _determine_questions_have_media(selected_quiz_id):
        quiz_codes_and_questions_status = {
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
        return quiz_codes_and_questions_status[selected_quiz_id]

    @staticmethod
    def _determine_answers_have_media(selected_quiz_id):
        quiz_codes_and_answers_status = {
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
        return quiz_codes_and_answers_status[selected_quiz_id]

    @staticmethod
    def _build_filter_code(selected_quiz_id):
        quiz_codes_to_filter_media_status = {
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
        return quiz_codes_to_filter_media_status[selected_quiz_id]

    def _build_quiz_id_box(self):
        quizzes_id = list(self.quizzes_front_to_quiz_id.keys())
        quiz_id_box = QtW.QComboBox()
        quiz_id_box.addItems(quizzes_id)
        quiz_id_box.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding, QtW.QSizePolicy.Policy.Expanding
        )
        quiz_id_box.currentTextChanged.connect(self._on_quiz_id_changed)
        return quiz_id_box

    def _on_quiz_id_changed(self, new_quiz_id):
        self.selected_quiz_front = new_quiz_id
        self.selected_quiz_id = self._build_selected_quiz_code()
        self.questions_have_media = self._determine_questions_have_media(
            self.selected_quiz_id
        )
        self.answers_have_media = self._determine_answers_have_media(
            self.selected_quiz_id
        )
        self.filters_code = self._build_filter_code(self.selected_quiz_id)
        self.sgn_quiz_id_changed.emit(self.selected_quiz_id)

    def _set_column_proportion(self):
        self.setColumnStretch(0, 10)
        self.setColumnStretch(1, 90)

    def get_filter_code(self):
        return self.filters_code

    def get_questions_have_media(self):
        return self.questions_have_media

    def get_answers_have_media(self):
        return self.answers_have_media
