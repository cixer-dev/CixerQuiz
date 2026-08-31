import gettext

from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.configurators.general_configurator import \
    general_reader


def _(original_string: str) -> str:
    """Translate string to the current language."""
    translations_dir = standard_path_reader.read_standard_path(
        "translations_dir"
    )
    app_domain = general_reader.read_general_config("app_domain")
    current_lang_code = general_reader.read_general_config(
        "current_language_code"
    )

    if current_lang_code == "en":
        return original_string

    translator = gettext.translation(
        domain=app_domain,
        localedir=translations_dir,
        languages=[current_lang_code]
    )

    translated = translator.gettext(original_string)
    if translated == original_string:
        raise KeyError(
            f"Missing translation for '{original_string}' in "
            f"language '{current_lang_code}'"
        )
    return translated


def translate_to_english(translated_string: str) -> str:
    """Translate string from current language back to English."""
    translations_dir = standard_path_reader.read_standard_path(
        "translations_dir"
    )
    app_domain = general_reader.read_general_config("app_domain")
    current_lang_code = general_reader.read_general_config(
        "current_language_code"
    )
    if current_lang_code == "en":
        return translated_string

    translator = gettext.translation(
        domain=app_domain,
        localedir=translations_dir,
        languages=[current_lang_code]
    )

    catalog = getattr(translator, "_catalog", {})
    translated_to_english = {
        translated: en_string
        for en_string, translated in catalog.items()
    }

    try:
        en_string = translated_to_english[translated_string]
    except KeyError as exc:
        raise KeyError(
            f"No English (msgid) found for translated string "
            f"'{translated_string}' in language '{current_lang_code}'"
        ) from exc
    return en_string
