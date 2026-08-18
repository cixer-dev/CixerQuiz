# CixerQuiz

# Introduction
CixerQuiz is an educational trivia-based application designed to provide users with maximum freedom to create, play, and share quizzes. Each trivia game can contain an unlimited number of levels across up to 9 different question types, featuring text and multimedia resources such as images and videos to ensure an interactive experience. Additionally, CixerQuiz allows you to share your created trivias within the app and customize a significant portion of the application's internal configuration and behavior.

## Why This Project Is Useful

CixerQuiz is an app with virtually infinite flexibility, making it suitable for numerous use cases. If you are a cinephile, you could create trivias about classic movies or television series where the objective is to identify the work based on a video clip. If you are an educator or student, you could create a customized trivia to prepare for an examination and share this resource with your students or peers. You could make a personalized trivia to improve your ability to recall country flags, characteristics of historical figures, mathematical expressions, or chemical nomenclature rules.

If you are an experienced user, professional programmer, or geek, you can use this project as a reference implementation for software solutions employing a similar technical stack, referring to [`docs/tech_stack.md`](docs/tech_stack.md) for more information

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

The project documentation is available in the [`docs/`](docs/) directory. It is recommend starting with [`docs/STRUCTURE.md`](docs/STRUCTURE.md) to understand the project structure, followed by [`docs/trivia_structure.md`](docs/trivia_structure.md) to comprehend the internal structure of a trivia game.

## How to Contribute

Please refer to [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) for a guide on contribution standards and practices for this project.