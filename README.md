# CixerQuiz

CixerQuiz is an educational application designed to give users maximum freedom to create, play, and share quizzes. Each quiz can contain an unlimited number of levels and supports up to nine different question-and-answer types. These level types offer a variety of resources, such as images and videos, to enhance the interactive experience. CixerQuiz allows users to share the quizzes they create within the app and customize the application's internal configuration and behavior.

## Why This Project Is Useful

CixerQuiz is an app with virtually unlimited flexibility, making it suitable for a wide range of use cases. For example, if you are a cinephile, you could create quizzes about classic movies or television series in which the objective is to identify a film based on a video clip. If you are an educator or a student, you could create customized quizzes to prepare for a test and share them with your students or peers. Alternatively, you could create personalized quizzes to improve your ability to recall country flags, identify characteristics of historical figures, solve mathematical expressions, or apply the rules of chemical nomenclature.

If you are an experienced user, professional programmer, or technology enthusiast, you can use this project as a reference implementation for software solutions that employ a similar technical stack. See [`docs/tech_stack.md`](docs/tech_stack.md) for more information.

## How to Get This Project

### Downloading the Release

If you want to use this application without manually installing it or managing its dependencies, you can download the release ZIP archive for your system from the [`releases`](https://github.com/cixer-dev/CixerQuiz/releases) section. Follow these steps:

1. Locate and download a ZIP archive compatible with your operating system and architecture from the [`releases`](https://github.com/cixer-dev/CixerQuiz/releases) section.

2. Extract the ZIP file into an empty folder.

3. In the extracted folder, locate the executable appropriate for your system. On Windows, the executable is a file named `CixerQuiz.exe`. On Linux, it is a Bash script named `launcher.sh`, which runs the `CixerQuiz` executable.

4. Once you have located the executable, run it. If you encounter any startup problems, try running the executable as an administrator or reporting the issue in the project's GitHub repository.

> **Warning:** You can move the project folder to any location on your system. However, moving individual directories or files, such as the executable or the configuration directory, to another location may cause the app to stop working.

### Building from Source

If you want to build the project yourself, follow these steps:

1. Create a directory in which to store the project and open it in your terminal.

2. Clone this repository into the newly created directory:

```bash
git clone https://github.com/cixer-dev/CixerQuiz.git
```

3. Install the Poetry dependency manager if you do not already have it. Consult the recommendations for your platform in the [official Poetry documentation](https://python-poetry.org/docs/).

4. Install the project dependencies in a virtual environment using Poetry and the following command:

```bash
poetry install
```

Alternatively, you can install the dependencies manually, without Poetry, using the [`requirements.txt`](requirements.txt) file with `pip` or your preferred dependency-management tool:

```bash
pip install -r requirements.txt --no-deps
```

> **Warning:** When installing an exported `requirements.txt` file with `pip`, always pass the `--no-deps` flag. Poetry has already resolved all dependencies, ensuring that all direct and transitive requirements are included. Re-resolving dependencies with `pip` is unnecessary and may cause conflicts.

> **Note:** For development purposes, it is strongly recommended that you install the project using Poetry to avoid compatibility issues.

## Project Documentation

The project documentation is available in the [`docs/`](docs/) directory. It is recommended that you begin with [`docs/STRUCTURE.md`](docs/STRUCTURE.md), which explains the directory structure, and then continue with [`docs/quiz_structure.md`](docs/quiz_structure.md), which explains the internal structure and functionality of a quiz.

## How to Contribute

Please refer to [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) for a guide to the contribution standards and practices for this project.