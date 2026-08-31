from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW

from src.view_design.custom_widgets.containers.standard \
    import StandardContainer
from src.view_design.page_design_toolkit \
    import cleaner
from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.tb_id_field import QuizIdField
from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.num_possible_questions_field \
    import NumPossibleQuestionsField
from src.view_design.pages.quiz_builder.area.levels_container.\
    level_container.level_field.text_content_container.brain \
    import TextContentFieldContainer


class LevelField(QtW.QVBoxLayout):
    """QWidget container for a single quiz level definition."""

    sgn_level_data_changed = QtC.Signal(dict)
    sng_level_field_was_rebuild = QtC.Signal()

    def __init__(self, parent_widget):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.parent_widget = parent_widget

        self.quiz_id = "TEXT_TEXTS"
        self.num_possible_questions = 1

        self.quiz_id_container = StandardContainer(self)
        self.num_possible_questions_container = StandardContainer(
            self
        )
        self.text_content_container = StandardContainer(self)

        self.quiz_id_field = self._build_id_field()
        self.num_possible_questions_field \
            = self._build_num_possible_questions_field()

        self.question_have_media \
            = self.quiz_id_field.get_questions_have_media()
        self.answers_have_media = self.quiz_id_field.get_answers_have_media()
        self.filters_code = self.quiz_id_field.get_filter_code()

        self.text_content_field = self._build_text_content_field()

        self.questions_list = []
        self.answers_list = []
        self.assets_paths_list = []

    def _build_id_field(self):
        quiz_id_field = QuizIdField(self.parent_widget)
        quiz_id_field.sgn_quiz_id_changed.connect(
            self._on_quiz_id_changed
        )
        self.quiz_id_container.setLayout(quiz_id_field)
        return quiz_id_field

    def _on_quiz_id_changed(self, new_quiz_id):
        self.quiz_id = new_quiz_id
        self.question_have_media \
            = self.quiz_id_field.get_questions_have_media()
        self.answers_have_media = self.quiz_id_field.get_answers_have_media()
        self.filters_code = self.quiz_id_field.get_filter_code()
        self._rebuilt_text_content_field()

    def _build_num_possible_questions_field(self):
        num_possible_questions_field = NumPossibleQuestionsField(
            self.num_possible_questions
        )
        num_possible_questions_field.sgn_field_content_changed.connect(
            lambda new_num_questions: self.on_quiz_num_questions_changed(
                new_num_questions
            )
        )
        self.num_possible_questions_container.setLayout(
            num_possible_questions_field
        )
        return num_possible_questions_field

    def on_quiz_num_questions_changed(self, new_num_questions):
        if not new_num_questions:
            new_num_questions = 1
        self.num_possible_questions = int(new_num_questions)
        self._rebuilt_text_content_field()

    def _rebuilt_text_content_field(self):
        cleaner.clear_container(self.text_content_container)
        self.text_content_container = StandardContainer(self)
        self.text_content_field = self._build_text_content_field()
        self._on_level_rebuilt()

    def _on_level_rebuilt(self):
        self.sng_level_field_was_rebuild.emit()

    def _build_text_content_field(self):
        text_content_field = TextContentFieldContainer(
            self.parent_widget,
            self.num_possible_questions,
            self.question_have_media,
            self.answers_have_media,
            self.filters_code
        )
        self.text_content_container.setLayout(text_content_field)
        text_content_field.sgn_question_changed.connect(
            self._on_question_changed
        )
        text_content_field.sgn_answers_changed.connect(
            self._on_answers_changed
        )
        text_content_field.sgn_text_content_container_was_rebuild.connect(
            self._on_level_rebuilt
        )
        return text_content_field

    def _on_question_changed(self, new_questions_list_content):
        self.questions_list = new_questions_list_content
        self.level_data = self._build_level_data()
        self.sgn_level_data_changed.emit(self.level_data)

    def _on_answers_changed(self, new_answers_list_content):
        self.answers_list = new_answers_list_content
        self.level_data = self._build_level_data()
        self.sgn_level_data_changed.emit(self.level_data)

    def _build_level_data(self):
        level_manifest = self._build_level_manifest()
        level_text_content = self._build_text_content()
        assets_paths_list = self.build_assets_media_paths()
        return {
            "manifest": level_manifest,
            "text_content": level_text_content,
            "assets_paths_list": assets_paths_list
        }

    def _build_level_manifest(self):
        return {
            "level_type_id": self.quiz_id,
            "num_questions": self.num_possible_questions
        }

    def _build_text_content(self):
        return {
            "questions": self.questions_list,
            "answers": self.answers_list
        }

    def build_assets_media_paths(self):
        assets_paths_list = []
        if self.question_have_media:
            for question_to_path in self.questions_list:
                question_media_path \
                    = str(next(iter(question_to_path.values())))
                assets_paths_list.append(question_media_path)
        if self.answers_have_media:
            for answer_list in self.answers_list:
                for answer_to_path in answer_list:
                    if isinstance(answer_to_path, dict):
                        answer_media_path \
                            = str(next(iter(answer_to_path.values())))
                        assets_paths_list.append(answer_media_path)
        return assets_paths_list

    def update_size(self, tb_area_size):
        default_width = tb_area_size.width()
        default_height = tb_area_size.height() // 10
        containers_with_default_size = [
            self.quiz_id_container,
            self.num_possible_questions_container
        ]
        for container in containers_with_default_size:
            container.setMaximumWidth(default_width)
            container.setFixedHeight(default_height)
        self.text_content_field.update_size(tb_area_size)
