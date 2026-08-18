To contribute to this repository, your contribution must follow the project’s core goal: giving users the greatest possible freedom to create and share their own fully customized trivia.

When contributing to this repository, first discuss the change you want to make by opening an issue or emailing the maintainer.

# Python Code Style Guidelines

To keep the project consistent when contributing, make sure your Python code follows the guidelines below. You must provide a good reason if you need to break any of them.

1. Write your code only in English.
2. Follow PEP 8 style rules (using Flake8 is recommended).
3. Add docstrings following the PEP 257 format for standalone functions, classes, or isolated methods. Do not include docstrings that describe the contents of an isolated module.
4. Include the minimum number of comments in code possible. If you add them, keep them brief, concise, and clear.
5. Use specific type hints for function/method signatures, especially in the logic under [`src/model`](src/model).
6. Do not use Hungarian notation, magic notation, or prefixes/suffixes that indicate a variable/attribute’s data type. Use type annotations instead.
7. Import modules in this order: standard modules, third-party modules, project modules. Separate each import group with a single blank line.
8. When importing a standalone function from a module, import the module first and reference the function as `module.function_imported`.
9. Include only one class per module unless the classes inherit from each other.
10. For importing PySide6 classes from the top-level directory, use an alias in the form `as QtX`, where `X` is the first uppercase letter of the imported class. For example: `QtWidgets as QtW` or `QtCore as QtC`.
11. When importing classes that do not directly inherit from PySide6, import the PySide6 base class first, then the desired class from it. For example: `QtW.QLabel` or `QtC.Signal`.
12. Include functions or methods that do not require more than 2 arguments.
13. If a string literal will be displayed on screen, refer to it as `_(string_original)`, importing `_` first from [`src/model/translation_handler.py`](src/model/translation_handler.py). This ensures the string is translated from the currently configured English language to the user’s selected language.

# Pull Request Guidelines

1. Ensure that all modifications—including but not limited to assets and code—use terms compatible with this project’s MIT license, and that they are properly credited in [`docs/CREDITS.md`](docs/CREDITS.md).
2. Ensure that the dependencies of your contribution are explicitly listed in `pyconfig` at the root of the project and are compatible with Poetry.
3. Ensure that each repository change is accompanied by an appropriate version number increment in the README, and that the project follows the SemVer versioning scheme.
4. Merge the pull request only after it receives approval from the lead developer.