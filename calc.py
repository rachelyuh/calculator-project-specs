'''
File Name: main.py
Dependencies: none
Purpose: Contains code that runs the operations
'''
# import statements (if any)
import sys
import math
import statistics as stats
from collections import deque
import requests
import interface

# Write your code here

history = deque()

green = "\033[0;32m"
reset = "\u001b[37m"
red = "\u001b[31m"

def calculate_future_value(present_value, interest, period):
    return present_value*((1 + interest/100)**period)

#esc: command sequence that terminates program
def esc_seq():
    sys.exit()
       

#help: command sequence that gives a list of helpful commands
def help_seq():
    blue = "\u001b[34m"
    reset = "\u001b[37m"

    print(f"{blue}esc: {reset}exit \n{blue}help: {reset}list of helpful commands")
    print(f"{blue}mean: {reset}finds the mean of a series of numbers")
    print(f"{blue}median: {reset}finds the median of a series of numbers")
    print(f"{blue}mode: {reset}finds the mode of a series of numbers")
    print(f"{blue}unitc: {reset}unit converter(mm, cm, m, km)")
    print(f"{blue}currencyc: {reset}currency converter")
    print(f"{blue}addm: {reset}add entries of a matrix")
    print(f"{blue}subtractm: {reset}subtract entries of a matrix")
    print(f'{blue}fv: {reset}calculate the future value of an asset over time. \
           \n\t{blue}Present Value: {reset}current value of the investment \
           \n\t{blue}Interest Rate: {reset}percent interest per time period \
            \n\t{blue}Period: {reset}time in years' ) 
    
        

#checks if the number is a valid number or if it is a command sequence
def check_if_valid(value):
    match value:
        case "help":
            help_seq()
            return True
        case "esc":
            esc_seq()
            return True
        case other:
            try:
                if (int(value) < 0):
                    print("You must enter a positive number")
                    return True
                return False
            except:
                print("You must enter a valid number")
                return True
            
#adds numbers
def add():
    try:
        second_num = input('')
        first_num = history.pop()
        ans = int(first_num) + int(second_num)
        history.append(ans)
        print(f'{green}{ans}{reset}')
    except:
        print(f"{red}Input Error{reset}")

#subtracts numbers
def subtract():
    try:
        second_num = input('')
        first_num = history.pop()
        ans = int(first_num) - int(second_num)
        history.append(ans)
        print(f'{green}{ans}{reset}')
    except:
        print(f"{red}Input Error{reset}")

#multiplies numbers
def multiply():
    try:
        second_num = input('')
        first_num = history.pop()
        ans = int(first_num) * int(second_num)
        history.append(ans)
        print(f'{green}{ans}{reset}')
    except:
        print(f"{red}Input Error{reset}")

#divides numbers
def divide():
    try:
        second_num = input('')
        first_num = history.pop()
        ans = int(first_num) / int(second_num)
        history.append(ans)
        print(f'{green}{ans}{reset}')
    except:
        print(f"{red}Input Error{reset}")

#takes the powers of numbers
def exponent():
    try:
        second_num = input('')
        first_num = history.pop()
        ans = math.pow(int(first_num), int(second_num))
        history.append(ans)
        print(f'{green}{ans}{reset}')
    except:
        print(f"{red}Input Error{reset}")

def square_root():
    try:
        first_num = history.pop()
        ans = math.pow(int(first_num), 1/2)
        history.append(ans)
        print(f'{green}{ans}{reset}')
    except:
        print(f"{red}Input Error{reset}")


def mean():
    list = []
    print('Add numbers to the list until satisfied. Enter nothing to calculate')
    while (True):
        inp = input('')
        if inp == '':
            break
        if not inp.isnumeric:
            raise stats.StatisticsError
        list.append(int(inp))
    try:
        print(f'{green}Mean is {stats.mean(list)}{reset}')
    except stats.StatisticsError:
        print('Invalid input')

def median():
    list = []
    print('Add numbers to the list until satisfied. Enter nothing to calculate')
    while (True):
        inp = input('')
        if inp == '':
            break
        if not inp.isnumeric:
            raise stats.StatisticsError
        list.append(int(inp))
    try:
        print(f'{green}Median is {stats.median(list)}{reset}')
    except stats.StatisticsError:
        print(f'{red}Invalid input{reset}')


def mode():
    list = []
    print('Add numbers to the list until satisfied. Enter nothing to calculate')
    while (True):
        inp = input('')
        if inp == '':
            break
        if not inp.isnumeric:
            raise stats.StatisticsError
        list.append(int(inp))
    try:
        print(f'{green}Mode is {stats.mode(list)}{reset}')
    except stats.StatisticsError:
        print(f'{red}Invalid input{reset}')
        

def unit_conversion():
    start = input(f"{reset}Enter first unit(mm, cm, m, km): {red}")
    end = input(f"{reset}Enter second unit(mm, cm, m, km):{red} ")
    val = input(f"{reset}Enter value to convert: {red}")
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
    ans = float(val)*SI[start]/SI[end]
    print(f'{green}{ans}{reset}')


#converts currency
def money_conversion():
    fCurr = input(f'Enter first currency:')
    sCurr = input(f'{reset}Enter second currency:')
    amt = input(f'{reset}Enter amount for first currency:')
    try:
        assert fCurr.isalpha()
        assert sCurr.isalpha()
        assert amt.isalnum()
        
        response = requests.get('http://cs1110.cs.cornell.edu/2022fa/a1/?old=' + fCurr.upper() + '&new=' + sCurr.upper() + '&amt=' + str(amt)).json()
        
        if response['err'] != '':
            print(f'{red}Invalid amount or currencies. Please enter valid currencies/amounts!{reset}')
            return
        
        print(response['rhs'])

    except AssertionError:
        print(f'{red}Invalid currencies or amount. Please enter valid currencies/amounts!{reset}')

#adds matrices
def add_matrix():
    row = int(input("Input number of rows: "))
    column = int(input("Input number of columns: "))
    x = 0
    list = []
    new = []
    while (x < int(column)):
        print(f"enter {row} numbers in column {x+1}")
        y = 0
        while (y < int(row)):
            temp = input("")
            try:
                new.append(float(temp))
            except ValueError:
                print(f'{red}Invalid matrix entry!{reset}')
                return
            y += 1
        list.append(new)
        new = []
        x += 1
    matrix1 = list
    list = []
    new = []
    x = 0
    while (x < int(column)):
        print(f"enter {row} numbers in column {x+1}")
        y = 0
        while (y < int(row)):
            temp = input("")
            try:
                new.append(float(temp))
            except ValueError:
                print(f'{red}Invalid matrix entry!{reset}')
                return
            y += 1
        list.append(new)
        new = []
        x += 1
    matrix2 = list
    
    ansmatrix = []
    new = []
    for i in range(0, column):
        for j in range(0, row):
            new.append(matrix1[i][j] + matrix2[i][j])
        ansmatrix.append(new)
        new = []
    
    print(f"{green}{ansmatrix}{reset}")
    
#subtracts matrices
def sub_matrix():
    row = int(input("Input number of rows: "))
    column = int(input("Input number of columns: "))
    x = 0
    list = []
    new = []
    while (x < int(column)):
        print(f"enter {row} numbers in column {x+1}")
        y = 0
        while (y < int(row)):
            temp = input("")
            try:
                new.append(float(temp))
            except ValueError:
                print(f'{red}Invalid matrix entry!{reset}')
                return
            y += 1
        list.append(new)
        new = []
        x += 1
    matrix1 = list
    list = []
    new = []
    x = 0
    while (x < int(column)):
        print(f"enter {row} numbers in column {x+1}")
        y = 0
        while (y < int(row)):
            temp = input("")
            try:
                new.append(float(temp))
            except ValueError:
                print(f'{red}Invalid matrix entry!{reset}')
                return
            y += 1
        list.append(new)
        new = []
        x += 1
    matrix2 = list
    
    ansmatrix = []
    new = []
    for i in range(0, column):
        for j in range(0, row):
            new.append(matrix1[i][j] - matrix2[i][j])
        ansmatrix.append(new)
        new = []
    
    print(f"{green}{ansmatrix}{reset}")

#calculates future value
def future_value():
    pv = ask_input("Present Value: ")
    i = ask_input("Interest rate: ")
    cp = ask_input("Period: ")
    future_val = round(calculate_future_value(int(pv), int(i), int(cp)), 2)
    
    green = "\033[0;32m"
    
    print(f"{green}Your future value is: {future_val}{reset}")

#helper for future value
def ask_input(value):
    x = input(value)
    while(check_if_valid(x) == True):
        x = input(value)
    return x