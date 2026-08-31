from src.model.configurators.accepted_formats_configurator import \
    accepted_formats_reader


def get_qdialog_filter_pattern(suffix: str) -> str | None:
    """Return the accepted format key that corresponds to a file suffix."""
    accepted_formats_content = \
        accepted_formats_reader.read_accepted_formats_content()
    accepted_formats_list = list(accepted_formats_content.values())
    unpacked_accepted_formats_list = []
    for accepted_format_list in accepted_formats_list:
        for accepted_format in accepted_format_list:
            unpacked_accepted_formats_list.append(accepted_format)

    if suffix in unpacked_accepted_formats_list:
        for accepted_format_key, accepted_formats_values in \
                accepted_formats_content.items():
            if suffix in accepted_formats_values:
                equivalent_format_key = accepted_format_key
                return equivalent_format_key
    else:
        raise KeyError(
            f"The suffix: {suffix} is not in the accepted formats list"
        )


def get_filter_to_accepted_formats(asset_key: str) -> str:
    """Return a QDialog-compatible filter string for the given asset key."""
    accepted_formats = accepted_formats_reader.read_accepted_formats(
        asset_key
    )
    formatted_filter_str = \
        get_formatted_filter_str_to_qdialog_pattern(accepted_formats)
    return formatted_filter_str


def get_formatted_filter_str_to_qdialog_pattern(
        filter_list: list[str]) -> str:
    """Format a list of suffixes into a QDialog filter string."""
    formatted_filter_list = [f"*.{suffix}" for suffix in filter_list]
    formatted_filter_str = " ".join(formatted_filter_list)
    return formatted_filter_str


def get_formatted_suffix_to_qdialog_pattern(suffix: str) -> str:
    """Return a QDialog-compatible pattern for a single suffix."""
    return f"*.{suffix}"
