# Use this file to add in functions for your programs functionality
import uuid
import json
import os
from typing import List

class TodoList:
	
	def __init__(
			self,
			store:str='todo.json') -> None:
		missingTodoFile()
		self.store = store
		with open(self.store) as f:
			self.data = json.load(f)

	# list-all Read list (All)
	def readListAll(self):
		for todo in self.data['todo']:
			print(todo['description'])

	# list-all Read list (Substring)
	def readListSubstring(
			self,
			substring: str):
		for todo in self.data['todo']:
			if substring in todo['description']:
				print(todo['description'])
	
	# list-all Read list (Complete)
	def readListComplete(
			self,
			substring: str):
		for todo in self.data['todo']:
			if substring in todo['description'] and todo['completion_status'] == 'Complete':
				print(todo['description'])
	
	# list-all Read list (Not Complete)
	def readListNotComplete(
			self,
			substring: str):
		for todo in self.data['todo']:
			if substring in todo['description'] and todo['completion_status'] == 'Not Complete':
				print(todo['description'])

	# Delete multiple todos
	def deleteMultiple(
			self,
			todo_ids: List[str]):
		temp = self.data["todo"]
		#python object to delete
		for id in todo_ids:
			for item in temp:
				if item["id"] == id:	
					temp.remove(item)
		write_json(self.data)
	
	# delete all todos
	def deleteAll(
			self,
			filename:str='todo.json'):
		os.unlink(filename)

	# toggle status from not complete to complete
	def toggleStatus(
		self,
		todo_ids: List[str]):
			temp = self.data["todo"]
			#python object to append
			for id in todo_ids:
				for item in temp:
					if item["id"] == id:	
						if item["completion_status"] == "Not Complete":
							item["completion_status"] = "Complete"
							#print(f'{item["description"]} is now marked as complete')
						else:
							item["completion_status"] = "Not Complete"
							#print(f'{item["description"]} is now marked as not complete')
			write_json(self.data)
	
	# update description of a todo
	def updateDescription(
			self,
			todo_id: str,
			new_description: str):
		temp = self.data["todo"]
		#python object to append
		for item in temp:
			if item["id"] == todo_id:
				#print(f'TODO list item "{item["description"]}" has been updated to "{new_description}"')
				item["description"] = new_description
		write_json(self.data)

	# Create TODO item(s)
	def createTodo(self, todo_names: List[str]):
		temp = self.data["todo"]
		for name in todo_names:
			y = {
				"description": name,
				"completion_status": "Not Complete",
				"id": str(uuid.uuid4())
			}
			temp.append(y)
			#print(f"Created TODO item(s): {name}")
		write_json(self.data)

# Check location of todo.json exists
def where_json(
		file_name: str) -> bool:
	return os.path.exists(file_name)

# Write to todo.json method
def write_json(
		data: dict,
		filename: str = 'todo.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)

# Check for missing todo.json file
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

# Gets CLI arguments following the command
def getCommandArguments(command_list: List[str]):
	x = command_list
	x.pop(0)
	return x