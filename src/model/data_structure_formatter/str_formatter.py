def snake_case_to_title(snake_case_str: str) -> str:
    """Convert a snake_case string to a title-cased string."""
    words = snake_case_str.split("_")
    field = " ".join(words)
    field = field.capitalize()
    return field


def title_to_snake_case(title: str) -> str:
    """Convert a title or phrase to snake_case."""
    words = title.strip().split()
    words = [word.lower() for word in words]
    return "_".join(words)
