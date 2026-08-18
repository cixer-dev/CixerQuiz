from src.model.json_wrapper import reader
from src.model.json_wrapper import writer
from src.model.configurators.standard_paths_configurator import \
    standard_path_reader


class TriviaPinner:
    """Manage pinned trivia entries stored in pinned trivias JSON."""

    def __init__(self, trivia_filepath: str) -> None:
        self.trivia_filepath = trivia_filepath
        self.pinned_trivias_list_path = (
            standard_path_reader.read_standard_path(
                "pinned_trivias_list"
            )
        )
        self.pinned_trivias_list = reader.read_json(
            self.pinned_trivias_list_path
        )
        self.is_pinned = (
            self.trivia_filepath in self.pinned_trivias_list
        )

    def toggle_pin_status(self) -> None:
        """Toggle the pin status of the trivia entry."""
        if self.is_pinned:
            self.unpin_trivia()
            self.is_pinned = False
        else:
            self.pin_trivia()
            self.is_pinned = True

    def pin_trivia(self) -> None:
        """Add the trivia entry to the pinned list."""
        new_pinned_trivias_list = [self.trivia_filepath]
        for pinned_trivia_path in self.pinned_trivias_list:
            if pinned_trivia_path != self.trivia_filepath:
                new_pinned_trivias_list.append(pinned_trivia_path)
        writer.write_json(
            self.pinned_trivias_list_path,
            new_pinned_trivias_list
        )

    def unpin_trivia(self) -> None:
        """Remove the trivia entry from the pinned list."""
        new_pinned_trivias_list = []
        for pinned_trivia_path in self.pinned_trivias_list:
            if pinned_trivia_path != self.trivia_filepath:
                new_pinned_trivias_list.append(pinned_trivia_path)
        writer.write_json(
            self.pinned_trivias_list_path,
            new_pinned_trivias_list
        )
