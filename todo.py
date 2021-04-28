# Use this file as your main entrypoint for your program
from todo import TodoList, getCommandArguments, get_cli

if __name__ == "__main__":

    # Initialise TodoList Object
    todo = TodoList()

    # Create TODO item(s)
    if get_cli().command[0] == "create":
        x = getCommandArguments(get_cli().command)
        todo.createTodo(x)

    # List item(s)
    if get_cli().command[0] == "list-all":
        # Handle --substring CLI argument
        if get_cli().substring:
            todo.readListSubstring(get_cli().substring[0])
        # Handle --no-complete CLI argument
        elif get_cli().no_complete:
            todo.readListNotComplete(get_cli().no_complete[0])
        # Handle --complete CLI argument
        elif get_cli().complete:
            todo.readListComplete(get_cli().complete[0])
        else:
            # Handle 'list-all'
            if len(get_cli().command) == 1:
                print("All TODO items below:")
                todo.readListAll()
            # Catch for inputs after list-all
            else:
                print('Do not include argument after "list-all"')

    # Delete all TODOs in todo.json
    if get_cli().command[0] == "delete-all":
        todo.deleteAll()
        print("All TODO items have been deleted")

    # Delete TODO item(s)
    if get_cli().command[0] == "delete":
        x = getCommandArguments(get_cli().command)
        todo.deleteMultiple(x)

    # Toggle 'completion_status' in all TODOs
    if get_cli().command[0] == "toggle":
        x = getCommandArguments(get_cli().command)
        todo.toggleStatus(x)

    # Update a TODO item description
    if get_cli().command[0] == "update":
        x = getCommandArguments(get_cli().command)
        # Checks for only 2 inputs
        if len(x) == 2:
            todo_id = x[0]
            todo_desc = x[1]
            todo.updateDescription(todo_id, todo_desc)
        else:
            print("Only parse a single TODO id and description to update")
