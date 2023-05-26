'''
File Name: main.py
Dependencies: interface.py
Purpose: Contains code that runs the operations
'''
# import statements (if any)
from interface import Interface
from calc import Calculator
# Write your code here

command_prompt = "Enter a command to begin calculation. Type 'help' for a list of commands, and 'exit' to quit."
command = input(command_prompt)
while command != "exit":
    match command:
        case "help":
            # print out some helpful information
            print("list of commands")
        case "add":
            # run the command to start adding using your interface library
            print("do the add command")
        case other:
            print("That wasn't a valid input, try again!")
    command = input(command_prompt)