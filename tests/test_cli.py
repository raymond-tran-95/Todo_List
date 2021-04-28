# Use this file to add in your tests!
import pytest
import CliRunner

from ..todo.cli import get_cli
from ..todo.todo import getCommandArguments, TodoList
from pathlib import Path

test_file = Path(__file__).parent / "test_data_read_list.json"


def test_getCommandArguments():
    status = ["create", "test1"]
    result = getCommandArguments(status)
    assert result == ["test1"]


def test_getCommandArguments_multiple_Variables():
    status = ["create", "test1", "test2", "test3"]
    result = getCommandArguments(status)
    assert result == ["test1", "test2", "test3"]


def test_readListAll(capsys):
    todo = TodoList(test_file)
    todo.readListAll()

    captured = capsys.readouterr()
    assert captured.out == "test1\ntest2\ntest3\ntest4\n"


def test_readListSubstring(capsys):
    todo = TodoList(test_file)
    todo.readListSubstring("1")

    captured = capsys.readouterr()
    assert captured.out == "test1\n"


def test_readListComplete(capsys):
    todo = TodoList(test_file)
    todo.readListComplete("test")

    captured = capsys.readouterr()
    assert captured.out == "test1\ntest2\n"


def test_readListNotComplete(capsys):
    todo = TodoList(test_file)
    todo.readListNotComplete("test")

    captured = capsys.readouterr()
    assert captured.out == "test3\ntest4\n"


def test_toggle(capsys):
    todo = TodoList(test_file)
    todo.toggleStatus(["b8fc1fa4-6cc4-44c0-92a9-d7b3f84f9c01", "b7e58d20-0f25-4dcc-b4a5-2803a9ec8a61"])
    todo.readListNotComplete("test")

    captured = capsys.readouterr()
    assert captured.out == "test1\ntest2\ntest3\ntest4\n"


def test_create_multiple(capsys):
    todo = TodoList(test_file)
    todo.createTodo(["Walk the dogs", "Feed the fish"])

    todo.readListAll()

    captured = capsys.readouterr()
    assert captured.out == "test1\ntest2\ntest3\ntest4\nWalk the dogs\nFeed the fish\n"


def test_create_single(capsys):
    todo = TodoList(test_file)
    todo.createTodo(["Walk the dogs"])

    todo.readListAll()

    captured = capsys.readouterr()
    assert captured.out == "test1\ntest2\ntest3\ntest4\nWalk the dogs\n"


def test_delete_single(capsys):
    todo = TodoList(test_file)
    todo.deleteMultiple(["b8fc1fa4-6cc4-44c0-92a9-d7b3f84f9c01"])
    todo.readListAll()

    captured = capsys.readouterr()
    assert captured.out == "test2\ntest3\ntest4\n"


def test_delete_multiple(capsys):
    todo = TodoList(test_file)
    todo.deleteMultiple(["b8fc1fa4-6cc4-44c0-92a9-d7b3f84f9c01", "b7e58d20-0f25-4dcc-b4a5-2803a9ec8a61"])
    todo.readListAll()

    captured = capsys.readouterr()
    assert captured.out == "test3\ntest4\n"


def test_update(capsys):
    todo = TodoList(test_file)
    todo.updateDescription("b8fc1fa4-6cc4-44c0-92a9-d7b3f84f9c01", "new_description")
    todo.readListAll()

    captured = capsys.readouterr()
    assert captured.out == "new_description\ntest2\ntest3\ntest4\n"
