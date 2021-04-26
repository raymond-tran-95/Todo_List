# Use this file to add in your tests!
import pytest

from ..todo.cli import get_cli
from ..todo.todo import createTodo, readListAll, deleteAll, readListSubstring, readListComplete, readListNotComplete, toggleStatus, deleteMultiple, getCommandArguments, updateDescription

def test_getCommandArguments():
	status = ['create','test1']
	result = getCommandArguments(status)
	assert result == ['test1']

def test_getCommandArguments_multiple_Variables():
	status = ['create','test1','test2','test3']
	result = getCommandArguments(status)
	assert result == ['test1','test2','test3']