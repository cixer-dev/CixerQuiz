import os


def delete_quiz(quiz_path: str) -> None:
    """Remove quiz directory and all files and subdirectories."""
    for root, dirs, files in os.walk(quiz_path, topdown=False):
        for filename in files:
            filepath = os.path.join(root, filename)
            os.remove(filepath)
        for name in dirs:
            dirpath = os.path.join(root, name)
            os.rmdir(dirpath)
    os.rmdir(quiz_path)
