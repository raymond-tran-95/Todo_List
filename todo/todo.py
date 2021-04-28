# Use this file to add in functions for your programs functionality
import uuid
import json
import os
from typing import List

class TodoList:
	
	def __init__(
		
		# Check for the file "todo.json" and opens the file for reading if it exists. If it does not exist, create the "todo.json" file.
		
			self,
			store:str='todo.json') -> None:
		missingTodoFile()
		self.store = store
		with open(self.store) as f:
			self.data = json.load(f)

	# list-all Read list (All)
	def readListAll(self):
		'''
		Reads all TODO descriptions in the TodoList object
		'''
		for todo in self.data['todo']:
			print(todo['description'])

	# list-all Read list (Substring)
	def readListSubstring(
			self,
			substring: str):
		'''
		Read all TODO descriptions which contain the "substring" value
		
		Keyword Arguments:
		
		substring: The substring argument  passed through the CLI command:
		python todo.py list-all --substring 'substring'
		'''
		for todo in self.data['todo']:
			if substring in todo['description']:
				print(todo['description'])
	
	# list-all Read list (Complete)
	def readListComplete(
			self,
			substring: str):
		'''
		Read all TODO descriptions which contain a "substring" value and are marked as complete
		
		Keyword Arguments:
		
		substring: The substring argument  passed through the CLI command:
		python todo.py list-all --complete 'substring'
		'''
		for todo in self.data['todo']:
			if substring in todo['description'] and todo['completion_status'] == 'Complete':
				print(todo['description'])
	
	# list-all Read list (Not Complete)
	def readListNotComplete(
			self,
			substring: str):
		'''
		Read all TODO descriptions which contain a "substring" value and are marked as not complete
		
		Keyword Arguments:
		
		substring: The substring argument  passed through the CLI command:
		python todo.py list-all --no-complete 'substring'
		'''
		for todo in self.data['todo']:
			if substring in todo['description'] and todo['completion_status'] == 'Not Complete':
				print(todo['description'])

	# Delete multiple todos
	def deleteMultiple(
			self,
			todo_ids: List[str]):
		'''
		Delete TODO items based on their "id".
		
		Keyword Arguments:
		
		todo_ids: List of TODO ids that are passed through the CLI command: 
		python todo.py delete 'todo_id_1' 'todo_id_2' 'todo_id_3'
		'''
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
		'''
		Delete ALL TODO items in the filename provided or "todo.json" by default.
		
		Keyword Arguments:
		
		filename: File name of the TODO list. Default is "todo.json"
		'''
		os.unlink(filename)

	# toggle status from not complete to complete
	def toggleStatus(
			self,
			todo_ids: List[str]):
		'''
		Toggle the completion status of TODO items based on their "id"
		
		Keyword Arguments:
		
		todo_ids: List of TODO ids that are passed through the CLI command: 
		python todo.py toggle 'todo_id_1' 'todo_id_2' 'todo_id_3'
		'''
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
		'''
		Update the completion status of TODO items based on their "id" to the new description provided
		
		Keyword Arguments:
		
		todo_id: A single TODO item "id" that is passed through the CLI command
		new_description: A TODO item "description" that is passed through the CLI command
		python todo.py update 'todo_id_1''new_description'
		'''
		temp = self.data["todo"]
		#python object to append
		for item in temp:
			if item["id"] == todo_id:
				#print(f'TODO list item "{item["description"]}" has been updated to "{new_description}"')
				item["description"] = new_description
		write_json(self.data)

	# Create TODO item(s)
	def createTodo(
			self,
			todo_names: List[str]):
		'''
		Create TODO items with "descriptions" as the names passed through CLI.
		
		Keyword Arguments:
		
		todo_names: List of TODO ids that are passed through the CLI command: 
		python todo.py create 'todo_id_1' 'todo_id_2' 'todo_id_3'
		'''
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
	'''
	Check the path to the file name exists. This function is used to create the "todo.json" file in the instance the file has not already been created
	
	Keyword Arguments:
	
	file_name: The filename the TODO list items are stored in
	'''
	return os.path.exists(file_name)

# Write to todo.json method
def write_json(
		data: dict,
		filename: str = 'todo.json'):
	'''
	Function to write data back into the TODO list file.
	
	Keyword Arguments:
	
	data: The dictionary to write into TODO list file
	filename: The file name of the TODO list file
	'''
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4)

# Check for missing todo.json file
def missingTodoFile(
		filename: str = 'todo.json'):
	'''
	Function to check if the 'todo.json' file is missing
	
	Keyword Arguments:
	
	filename: The file name of the TODO list file
	'''
	if where_json(filename):
		pass
	else:
		todo: dict = {
			"todo":[

			]
		}
		with open('todo.json', 'w') as todo_file:
			json.dump(todo, todo_file)

# Gets CLI arguments following the command
def getCommandArguments(
		command_list: List[str]):
	'''
	Function to get command arguments following the commands.
	
	Keyword Arguments:
	
	command_list: The string list passed through argparse
	
	e.g. python todo.py create 'test1' 'test2'
	
	command_list: ['create','test1','test2']
	returns: ['test1','test2']
	'''
	x = command_list
	x.pop(0)
	return x