import re


def snake_case_to_title(snake_case_str: str) -> str:
    """Convert a snake_case string to a title-cased string."""
    words = snake_case_str.split("_")
    field = " ".join(words)
    field = field.capitalize()
    return field


def title_to_snake_case(title: str) -> str:
    """Convert a title into snake_case."""
    normalized_title = title.strip().lower()
    words = re.findall(r"[a-z0-9]+", normalized_title)
    return "_".join(words)


def split_long_string(
    original_string: str,
    char_limit: int,
    separator: str = "\n",
) -> str:
    """Split a string that exceeds the specified character limit.

    The function replaces the nearest space before the character limit with
    the specified separator. If no space is found, it inserts the separator
    at the character limit.
    """
    if len(original_string) > char_limit:
        char_list = list(original_string)
        char_list_is_formatted = False

        for index in range(char_limit - 10, char_limit):
            char = char_list[index]

            if char == " ":
                char_list[index] = separator
                char_list_is_formatted = True
                break

        if not char_list_is_formatted:
            first_list = char_list[0:char_limit]
            first_list.append(separator)
            second_list = char_list[char_limit:-1]
            char_list = first_list + second_list

        return "".join(char_list)

    return original_string
