# Introduction

A quiz is a data unit that contains all the information required by the program to visually present the levels, questions, and answers to the user. It is implemented as a directory with different files and subdirectories that perform specific functions in the quiz-display process.

The structure of a quiz will be addressed by analyzing the composition of the directory. That is, each expected directory or file in a quiz will be listed, explaining its function, structure, and examples of its content. The analysis will begin with the upper units, those closest to the quiz's root directory.

For the examples, the information included is the content of the default quiz included in the program. It is recommended that the reader follow this document in a logical order, as concepts defined or explained in the initial sections will not be unnecessarily restated in later sections to reduce repetition.

# Quiz

The internal structure of a quiz consists of a `manifest.json` file and a series of directories working as levels.

## manifest.json

The `manifest.json` file of the quiz serves to store information necessary for the quiz display.

The following is an example of the possible content of this file:

```json
{
"is_valid_quiz": true,
"num_levels": 8,
"quiz_description": "A scientific quiz with 8 levels. It covers content in chemistry, physics, and mathematics.",
"quiz_duration": 60000,
"quiz_name": "Scientific Quiz"
}
```

The `is_valid_quiz` variable defaults to `true`. Its current purpose is to prevent the quiz display logic from processing non-quiz JSON files. Future updates will include a feature to deactivate the system if errors happen during quiz creation.

The `num_levels` value is a positive integer that indicates how many levels the quiz has in total.

`quiz_description` and `quiz_name` contain information that allows the user to identify quizzes by their name or description in the game's main menu.

`quiz_duration` is a positive number indicating how many milliseconds players have to answer a question. If the user exceeds the established time, the program will handle it as a defeat by timeout.

# Level

A level is a compact data unit represented in the file system by a directory. Its name is always a natural number greater than zero that corresponds to the order of appearance of that level in the quiz.

In total, the project supports 9 level types. Each possesses a code formed by a character string that identifies it internally in the program's logic. The current codes for levels are:

- `TEXT_TEXTS`
- `TEXT_IMAGES`
- `TEXT_VIDEOS`
- `IMAGE_TEXTS`
- `IMAGE_IMAGES`
- `IMAGE_VIDEOS`
- `VIDEO_TEXTS`
- `VIDEO_IMAGES`
- `VIDEO_VIDEOS`

The naming format for level codes is not arbitrary; understanding it is relevant to the program's operation. Each code has the form:

$P$ _ $R$

Where:
$P$ is the type of information attached to the question.
$R$ is the type of information attached to each answer.

Both $P$ and $R$ must be individual nouns, without articles or adjectives. They must be written in uppercase and as briefly as possible. $P$ must be singular, as it refers to the type of a single question. Conversely, $R$ must be plural, as it refers to the type of multiple answers.

Both questions and answers may have attached files that contextualize them. When a question or answer includes multimedia files, a reference to this is made by adding the suffix "with_media". Otherwise, the suffix "without_media" is added. When this suffix is missing, the term applies generally to both questions and answers.

All question and answer types, regardless of their codes, include text. When the code assigned to $P$ or $R$ is `TEXT` or `TEXTS` respectively, it means that the information attached to $P$ or $R$ is solely text. In other words, it means that there is no multimedia file added to that question or those answers. Should a multimedia file be added to the questions or answers, the code would change to the type of file added.

Currently, the project supports two types of multimedia files: images or videos. The list of accepted formats for these file types is found in the [`config/accepted_formats.json`](config/accepted_formats.json) JSON. The limitation to certain formats arises from the limited support that exists for the widgets used in the level display performed by the PySide6 library.

Functionally, level types differ by the content within two JSON files in the level directory: `manifest.json` and `text_content.json`, in addition to the `assets` subdirectory, which is added if the level contains multimedia files attached to questions or answers.

## manifest.json Structure

The `manifest.json` contains a dictionary with two entries: `level_type_id` and `num_questions`.

The value of the `level_type_id` entry is a text string that represents an identifier associated with the level type.

`num_questions` contains an integer associated with the possible entries of questions and answers for the level.

The following shows an example of `manifest.json` content:

```json
{
    "level_type_id": "TEXT_TEXTS",
    "num_questions": 3
}
```

## text_content.json Structure

The `text_content.json` contains a general dictionary with two entries: `questions` and `answers`.

The following is an example of text_content.json in a level:

```json
{
    "answers": [
        [
            "Unique and unambiguous designation that represents its properties",
            "Arbitrary designation based on standards",
            "Mathematical equation that represents physical properties"
        ],
        [
            "Thermodynamic process in which reacting substances are converted into products",
            "Electrochemical process where one substance is converted into another",
            "Physical process where two elements combine without forming a new substance",
            "Chemical process where energy is consumed"
        ],
        [
            "Type of matter formed by atoms of the same category",
            "Substance that cannot be decomposed by a chemical reaction",
            "Substance that cannot be decomposed by a physical reaction"
        ]
    ],
    "questions": [
        "In Chemistry, the nomenclature of a substance is a...",
        "In Chemistry, reaction is understood as a...",
        "In Chemistry, chemical element is understood as a..."
    ]
}
```

In the `text_content.json` of each level, there may be multiple questions with their respective answers. That is, in a single level, there can exist n possible questions and n lists of possible answers to these questions, respectively. For simplicity, a question and its possible answers will be referred to generally as a question-answers pair.

Although a single level can have multiple question-answers pairs, when the quiz is played by the user, a single pair is selected randomly. This is achieved because in the question-answers pairs, the indices in their respective lists are identical.

If a question-answers pair were to be displayed to the user, the following process would be followed:

1. The program accesses the `manifest.json` of the level
2. Extracts from `manifest.json` the value of the `num_questions` key
3. Generates a random positive number between 1 and the value of `num_questions`
4. Accesses the value of the `"questions"` and `"answers"` keys with the index of the randomly generated number

This implementation allows that with a sufficient number of possible questions and answers, the same quiz can be replayed multiple times by increasing the variety of question-answers pairs in a level.

In this example, if the random number were 2, the question would be selected:

```json
"In Chemistry, reaction is understood as a..."
```

and the possible answers would be:

```json
[
	"Thermodynamic process in which reacting substances are converted into products",
	"Electrochemical process where one substance is converted into another",
	"Physical process where two elements combine without forming a new substance",
	"Chemical process where energy is consumed"
]
```

### Questions

The value in `questions` depends on the level type. However, in general, `questions` can be:

- a list of text strings (referred to as `question` in the code with type)
- or a list of dictionaries whose keys and values are text strings (referred to as `questions with media` in the code).

`questions` cannot be implemented as a list with non-uniform elements. All its elements are strings in the case of `questions without media` or dictionaries in the case of `questions with media`.

#### Questions without Media

Questions without media are represented as a list of text strings. An example of a question internally would be represented as:

```json
"questions": [
	"In Chemistry, the nomenclature of a substance is a...",
	"In Chemistry, reaction is understood as a...",
	"In Chemistry, chemical element is understood as a..."
]
```

#### Questions with Media

Questions with media are represented internally as a list of dictionaries. In each dictionary, the key is the visible text of the question and the value is the path to the attached file that contextualizes it.

For example, a question with media would be represented internally as:

```json
"questions": [
	{
	"Who is the author of this treatise?": "assets/methode.jpg"
	},
	{
	"Who is the author of this treatise?": "assets/principia.png"
	},
	{
	"Who is the author of this book?": "assets/brief.jpg"
	}
```

### Answers

The value in `answers` also depends on the level type. In general, they can be:

- a list of lists of text strings (referred to as `answers` in the code)
- or a list of lists of dictionaries whose keys and values are text strings (referred to as `answers with media` in the code).

`answers` cannot be implemented as a list with non-uniform elements. All its elements are lists of strings in the case of `answers without media` or lists of dictionaries in the case of `answers with media`.

Although it may be verbose, there is a reason for implementing `answers` as a list nested within another list. The first list represents all possible answers that can be given to the questions. Each of these possible answers in turn must be an iterable data structure so that the user can choose from these the correct answer. That is why the elements in the first list are other lists.

#### Answers without Media

Answers without media are represented as a list of lists of text strings. An example of `answers_without_media` internally would be represented as:

```json
"answers": [
	[
		"Unique and unambiguous designation that represents its properties",
		"Arbitrary designation based on standards",
		"Mathematical equation that represents physical properties"
	],
	[
		"Thermodynamic process in which reacting substances are converted into products",
		"Electrochemical process where one substance is converted into another",
		"Physical process where two elements combine without forming a new substance",
		"Chemical process where energy is consumed"
	],
	[
		"Type of matter formed by atoms of the same category",
		"Substance that cannot be decomposed by a chemical reaction",
		"Substance that cannot be decomposed by a physical reaction"
	]
]
```

#### Answers with Media

Answers with media are represented as a list of lists of dictionaries. These dictionaries include a text entry that heads the answer and the path to a multimedia file that contextualizes the answer. An example of `answers with media` internally would be representable as:

```json
{
"answers": [
	[
		{
		"Rene Descartes": "assets/Descartes.jpg"
		},
		{
		"Trence Tao": "assets/Trence Tao.jpg"
		},
		{
		"Srinivasa Ramanujan": "assets/Ramanujan.jpg"
		}
		],
	[
		{
		"Isaac Newton": "assets/newton.jpg"
		},
		{
		"Galileo Galilei": "assets/galileo.jpg"
		},
		{
		"Gottfried Wilhelm Leibniz": "assets/Lebniz.jpeg"
		}
		],
	[
		{
		"Stephen Wiliam Hawking": "assets/hawking.jpg"
		},
		{
		"Richard Dawkings": "assets/Dawkings.jpg"
		},
		{
		"Trence Tao": "assets/Trence Tao.jpg"
		}
	]
],
"questions": [
	{
	"Who is the author of this treatise?": "assets/methode.jpg"
	},
	{
	"Who is the author of this treatise?": "assets/principia.png"
	},
	{
	"Who is the author of this book?": "assets/brief.jpg"
	}
]
}
```

## Assets

The `assets` directory serves as the repository for files attached to questions and answers with media within each level. Within it, there is no hierarchy for the files.

The implementation of this directory is necessary to allow the use of paths relative to the quiz and not to a specific machine and directory. Thus, quizzes can be exchanged from one computer to another via the internet, or moved from one directory to another according to user needs.

In quiz creation, local storage files initially included by the user through the graphical interface are used. In the final construction of the quiz directory, the program creates a copy of the local files referenced by the user for questions or answers in the `assets` directory. Then, it takes the original path of the file referenced by the user and extracts the filename and extension from it. Subsequently, the program concatenates the path `assets/` with the filename and extension, so that the final path in the quiz acquires the form: `assets/filename.extension`

When displaying files in the question or answer, the program concatenates the absolute path of the level with the path formatted by the program to obtain the absolute path of the file and display it. In this manner, if the quiz changes directory, the program will have no difficulty recreating the absolute path of each multimedia file at runtime.
