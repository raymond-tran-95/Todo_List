# Application - 📝 Todo list

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/ghandic/PyCap-TODO-CRUD)
![coverage](https://img.shields.io/badge/coverage-0%25-red)

This commandline program is a basic implementation for a todo list application using Python 3.6+ that allows you to build and maintain a TODO list.


## Usage

To use the program with pipenv simply enter a pipenv shell by running `pipenv shell` or prefix `pipenv run` before any Python command

### Program options

| Description                                          | Usage                                                                                                 |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Create a todo                                        | `python todo.py create "Take the washing out"`                                                   |
| Create multiple TODOs                                | `python todo.py create "Take the washing out" "Walk the dog"`                                         |
| Read (list) all TODOs                                | `python todo.py list-all`                                                                             |
| Read (list) all TODOs that contain a given substring | `python todo.py list-all --substring "dog"`                                                           |
| Read (list) all TODOs that are complete              | `python todo.py list-all --complete "dog"`                                                            |
| Read (list) all TODOs that are not complete          | `python todo.py list --no-complete "dog"`                                                             |
| Toggle the state of a TODO                            | `python todo.py toggle "f7f6d502-dc35-40d2-b348-287a714b6978"`                                        |
| Update the description of a TODO                          | `python todo.py update "f7f6d502-dc35-40d2-b348-287a714b6978" "Walk all the dogs"`                    |
| Delete a TODO                                      | `python todo.py delete "f7f6d502-dc35-40d2-b348-287a714b6978"`                                        |
| Delete multiple TODOs                                | `python todo.py delete "f7f6d502-dc35-40d2-b348-287a714b6978" "2be6199a-abec-42c8-8744-255cbb152d9c"` |
| Delete all TODOs                                     | `python todo.py delete-all`                                                                           |

## Pros, cons and next steps

### Pros

- All CLI functions work as intended!

### Cons

- Only works on a single TODO list

### Next steps

- Test Classes for CLI input and reading the created JSON file
- Expand functionality to create additional TODO lists
- Error Handling

## License

This project is licensed under the terms of the MIT license.
