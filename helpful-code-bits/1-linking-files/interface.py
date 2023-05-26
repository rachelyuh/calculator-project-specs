'''
File Name: interface.py
Dependencies: calc.py
Purpose: Contains code that operates the interface of the calculator app 
(i.e mostly printing, running certain commands)
'''
# import statements 
# if OOP
from calc import Calculator
c = Calculator()
c.add(x, y)
c.subtract(x,y)
# if functional
import calc
calc.add(x, y)
calc.subtract(x, y)

# Write your code here: