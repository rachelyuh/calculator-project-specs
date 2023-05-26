'''
File Name: interface.py
Dependencies: calc.py
Purpose: Contains code that operates the interface of the calculator app 
(i.e mostly printing, running certain commands)
'''
# import statements 
import calc
import sys
from collections import deque

# Write your code here:
class Interface:
    def __init__(self, input):
        self.input = input

    #reads info
    def read(self, val):
        match val:
            case 'help':
                calc.help_seq()
            case 'esc':
                calc.esc_seq()
            case 'fv':
                calc.future_value()
            case '+':
                calc.add()
            case '-':
                calc.subtract()
            case '*':
                calc.multiply()
            case '/':
                calc.divide()
            case '^':
                calc.exponent()
            case 'clear':
                calc.history.clear()
            case 'mean':
                calc.mean()
            case 'median':
                calc.median()
            case 'mode':
                calc.mode()
            case 'unitc':
                calc.unit_conversion()
            case 'currencyc':
                calc.money_conversion()
            case 'addm':
                calc.add_matrix()
            case 'subtractm':
                calc.sub_matrix()
            case other:
                if (val.isnumeric()):
                    calc.history.append(val)
                else:
                    print('Enter a valid operation!')