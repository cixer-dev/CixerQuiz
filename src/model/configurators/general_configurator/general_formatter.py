from src.model.configurators.general_configurator import general_reader


def get_lang_options() -> list[str]:
    """Return available language options from general configuration JSON."""
    languages_to_code = general_reader.read_general_config(
        "languages_to_code"
    )
    lang_options = list(languages_to_code.keys())
    return lang_options
