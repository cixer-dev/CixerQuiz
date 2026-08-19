# CixerQuiz
CixerQuiz is an educational application designed to provide users with maximum freedom to create, play, and share trivias. Each trivia can contain an unlimited number of levels of up to 9 different question and answers types. These level types feature a diversity of resources such as images and videos to enhance the interactive experience. CixerQuiz allows sharing your created trivia within the app and customizing the application's internal configuration and behavior.

## Why This Project Is Useful

CixerQuiz is an app with virtually infinite flexibility, making it suitable for many use cases. For example, if you are a cinephile, you could create trivia about classic movies or television series where the objective is to identify the film based on a video clip. If you are an educator or student, you could create customized trivia to prepare for a test and share this resource with your students or peers. Alternatively, you could make personalized trivia to improve your ability to recall country flags, characteristics of historical figures, mathematical expressions, or chemical nomenclature rules.

If you are an experienced user, professional programmer, or technology enthusiast, you can use this project as a reference implementation for software solutions employing a similar technical stack. See [`docs/tech_stack.md`](docs/tech_stack.md) for more information.

## How to Use This Project
### Building From Source

If you want to build the project yourself, follow these steps:

1. Create a directory to store the project and open it in your terminal.

2. Clone this repository into your newly created directory:

```bash
git clone https://github.com/cixer-dev/CixerQuiz.git
```

3. Install the project dependencies using the Poetry dependency manager:

```bash
poetry install
```

Alternatively, you can manually install dependencies using the `requirements.txt` file with pip or your preferred dependency management tool:

```bash
pip install -r requirements.txt --no-deps
```

> **Warning:** When installing an exported `requirements.txt` via `pip`, always pass the `--no-deps` flag. Poetry has already resolved all dependencies, ensuring that all direct and transitive requirements are included. Re-resolution via pip is unnecessary and may cause conflicts.

> **Note:** For development purposes, it is strongly recommended to install the project using Poetry to avoid compatibility issues.

## Project Documentation

The project documentation is available in the [`docs/`](docs/) directory. It is recommended to start with [`docs/STRUCTURE.md`](docs/STRUCTURE.md), which explains the directory structure, and then [`docs/trivia_structure.md`](docs/trivia_structure.md), which explains the internal structure and functionalities of a trivia.

## How to Contribute

Please refer to [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) for a guide on contribution standards and practices for this project.