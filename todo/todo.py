# Use this file to add in functions for your programs functionality
import uuid
import json
import os
from typing import List

def where_json(
		file_name: str) -> bool:
	return os.path.exists(file_name)

def write_json(
		data: dict,
		filename: str = 'todo.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)

def missingTodoFile():
	if where_json('todo.json'):
		pass
	else:
		todo = {
			"todo":[

			]
		}
		with open('todo.json', 'w') as todo_file:
			json.dump(todo, todo_file)

def createTodo(todo_names: List[str]):

	missingTodoFile()

	with open('todo.json') as json_file:
		data = json.load(json_file)
		temp = data['todo']

		#python object to append
		for name in todo_names:
			y = {
				"description": name,
				"completion_status": "Not Complete",
				"id": str(uuid.uuid4())
			}
			temp.append(y)
			print(f"Created TODO item(s): {name}")
		write_json(data)

# list-all Read list (All)
def readListAll():
	with open('todo.json') as json_file:
		data = json.load(json_file)
		for todo in data['todo']:
			print(todo['description'])

# list-all Read list (Substring)
def readListSubstring(substring: str):
	with open('todo.json') as json_file:
		data = json.load(json_file)
		for todo in data['todo']:
			if substring in todo['description']:
				print(todo['description'])

# list-all Read list (Complete)
def readListComplete(substring: str):
	with open('todo.json') as json_file:
		data = json.load(json_file)
		for todo in data['todo']:
			if substring in todo['description'] and todo['completion_status'] == 'Complete':
				print(todo['description'])

# list-all Read list (Not Complete)
def readListNotComplete(substring: str):
	with open('todo.json') as json_file:
		data = json.load(json_file)
		for todo in data['todo']:
			if substring in todo['description'] and todo['completion_status'] == 'Not Complete':
				print(todo['description'])

# Delete multiple todos
def deleteMultiple(todo_ids: List[str]):
	with open('todo.json') as json_file:
		data = json.load(json_file)
		temp = data["todo"]
		#python object to append
		for id in todo_ids:
			for item in temp:
				if item["id"] == id:	
					temp.remove(item)
		write_json(data)

# delete all todos
def deleteAll():
	os.unlink('todo.json')

# toggle status from not complete to complete
def toggleStatus(todo_ids: List[str]):
	with open('todo.json') as json_file:
		data = json.load(json_file)
		temp = data["todo"]
		#python object to append
		for id in todo_ids:
			for item in temp:
				if item["id"] == id:	
					if item["completion_status"] == "Not Complete":
						item["completion_status"] = "Complete"
						print(f'{item["description"]} is now marked as complete')
					else:
						item["completion_status"] = "Not Complete"
						print(f'{item["description"]} is now marked as not complete')
		write_json(data)

# update description of a todo
def updateDescription(
		todo_id: str,
		new_description: str):
	with open('todo.json') as json_file:
		data = json.load(json_file)
		temp = data["todo"]
		#python object to append
		for item in temp:
			if item["id"] == todo_id:
				print(f'TODO list item "{item["description"]}" has been updated to "{new_description}"')
				item["description"] = new_description
		write_json(data)
	
def getCommandArguments(command_list: List[str]):
	x = command_list
	x.pop(0)
	return x