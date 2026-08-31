from src.model.json_wrapper import reader
from src.model.json_wrapper import writer
from src.model.configurators.standard_paths_configurator import \
    standard_path_reader


class QuizPinner:
    """Manage pinned quiz entries stored in pinned quizzes JSON."""

    def __init__(self, quiz_filepath: str) -> None:
        self.quiz_filepath = quiz_filepath
        self.pinned_quizzes_list_path = (
            standard_path_reader.read_standard_path(
                "pinned_quizzes_list"
            )
        )
        self.pinned_quizzes_list = reader.read_json(
            self.pinned_quizzes_list_path
        )
        self.is_pinned = (
            self.quiz_filepath in self.pinned_quizzes_list
        )

    def toggle_pin_status(self) -> None:
        """Toggle the pin status of the quiz entry."""
        if self.is_pinned:
            self.unpin_quiz()
            self.is_pinned = False
        else:
            self.pin_quiz()
            self.is_pinned = True

    def pin_quiz(self) -> None:
        """Add the quiz entry to the pinned list."""
        new_pinned_quizzes_list = [self.quiz_filepath]
        for pinned_quiz_path in self.pinned_quizzes_list:
            if pinned_quiz_path != self.quiz_filepath:
                new_pinned_quizzes_list.append(pinned_quiz_path)
        writer.write_json(
            self.pinned_quizzes_list_path,
            new_pinned_quizzes_list
        )

    def unpin_quiz(self) -> None:
        """Remove the quiz entry from the pinned list."""
        new_pinned_quizzes_list = []
        for pinned_quiz_path in self.pinned_quizzes_list:
            if pinned_quiz_path != self.quiz_filepath:
                new_pinned_quizzes_list.append(pinned_quiz_path)
        writer.write_json(
            self.pinned_quizzes_list_path,
            new_pinned_quizzes_list
        )
