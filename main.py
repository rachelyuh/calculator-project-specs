'''
File Name: main.py
Dependencies: interface.py, calc.py

'''
# import statements for interface and calc
import calc
import interface
# Write your code here
interface = interface.Interface(None) 
black = "\u001b[30m"
blue = "\u001b[34m"
reset = "\u001b[37m"

print(f'{blue}Here are some operations for this calculator: ')
calc.help_seq()

while True:
    mainIn = input(f'{reset}')
    interface.read(mainIn)