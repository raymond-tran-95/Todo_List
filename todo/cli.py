# Use this file to add in functions for your cli if you use one!
import argparse

# Declare CLI positional and non-positional arguments
def get_cli():
	'''
	Declares the arguments for CLI following:
	
	Positional:
		command
	
	Non-Positional:
		--substring
		--no-complete
		--complete
	'''
	todo = argparse.ArgumentParser(description='TODO list CLI')
	todo.add_argument('command', type=str, nargs='+', help='TODO list commands')
	todo.add_argument('--substring', type=str, nargs=1, help='TODO list-all substring search')
	todo.add_argument('--no-complete', type=str, nargs=1, help='TODO list-all substring search not complete')
	todo.add_argument('--complete', type=str, nargs=1, help='TODO list-all substring search complete')

	args = todo.parse_args()
	return args