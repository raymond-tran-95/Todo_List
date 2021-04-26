# Use this file as your main entrypoint for your program
from todo import createTodo, readListAll, deleteAll, readListSubstring, readListComplete, readListNotComplete,toggleStatus, deleteMultiple, getCommandArguments, updateDescription, get_cli

if __name__ == "__main__":
	if get_cli().command[0] == 'create':
		x = getCommandArguments(get_cli().command)
		createTodo(x)
	
	if get_cli().command[0] == 'list-all':
		if get_cli().substring:
			readListSubstring(get_cli().substring[0])
		elif get_cli().no_complete:
			readListNotComplete(get_cli().no_complete[0])
		elif get_cli().complete:
			readListComplete(get_cli().complete[0])
		else:
			if len(get_cli().command) == 1:
				print('All TODO items below:')
				readListAll()
			# Catch for inputs after list-all
			else:
				print('Do not include argument after "list-all"')
		
	if get_cli().command[0] == 'delete-all':
		deleteAll()
		print('All TODO items have been deleted')
	
	if get_cli().command[0] == 'toggle':
		x = getCommandArguments(get_cli().command)
		toggleStatus(x)
		
	if get_cli().command[0] == 'delete':
		x = getCommandArguments(get_cli().command)
		deleteMultiple(x)

	if get_cli().command[0] == 'update':
		x = getCommandArguments(get_cli().command)
		# Checks for only 2 inputs
		if len(x) == 2 :
			todo_id = x[0]
			todo_desc = x[1]
			updateDescription(todo_id, todo_desc)
		else:
			print('Only parse a single TODO id and description to update')