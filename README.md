# CLI Calculator Program
## Introduction
You will be building and presenting a calculator application in python that runs in the command line.

The requirements for this project are:
- Your calculator should be able to perform at least 4 different operations. At least 1 of them should be finance related.
- Your calculator should adhere to at least the Mild level interface specifications

## Interface Specifications
These interface specifications include explorations with using other libraries, or making things cleaner, along with standard instructions. Although one stage is not necessarily harder than the other, the challenge is managing all these moving parts since each level requires all the functionality of the previous.
### Mild
- **Command Input Loop**: Your program must contain a command input loop that asks them what operation they want to perform. (hint: `while` loops and  `match` are useful here)
- **Help Command**: Your program must include a `help` command that lists all the available commands on your calculator.
- **Ability to Exit**: You must also include a command in that command input loop that allows them to exit the program. 
- **Readability**: You must use escape sequences (such as `\n` and `\t`) to properly format your answers
- **Modular Code**: Your program must have modular code, i.e. one file called `main.py`, one file called `interface.py`and another called `calc.py`. 
    - `main.py` should contain your main command loop and call functions from your `interface.py` to run commands.
    - `interface.py` should contain all functions/classes related to running commands. It should use functions from `calc.py` and then properly format/print them.
    - `calc.py` should contain all functions/classes related to working your interface
- We highly encourage you to use Object Oriented Programming at this stage, but understand that, at this level, a functional programming paradigm works just as well.
### Medium
- All of the previous specifications.
- **Object Oriented**: At this stage both your `interface.py` and `calc.py` files should operate using Object Orienting programming.
- **Storage**: Keep the history of operations performed
- **Auto Clearing**: Use ANSI escape codes to clear out the command line every time the command input loop is run.
- **Design**: Use ANSI escape codes to make your output easier to read with highlighting, color, and text decoration (i.e bold, italics)
### Spicy
- All of the previous specifications.
- **Settings**: Use the `sys` python library so that command line arguments can be inputted to change the way the way your calculator functions. Below are some examples of settings you can include:
    - Scientific Notation or Normal Notation
    - Decimal Place Rounding
    - Text Color
    - Radians or Degrees
    - Here is an example of what we mean by a command line argument:
    ```
    python main.py -s 5 -r
    ```
    - This command would initialize a calculator that gives answers in scientific notation, rounded up to 5 decimal places, red in color, and in degrees.
    - This is just an example, feel free to use your own conventions for arguments
- **Error Handling**: Your operations should use `try/except` (or another error catching method) to handle calculation errors from inputs WITHOUT causing the program to end abruptly.
- **Well Documented Code**: Include docstrings for each class and function you write in `interface.py` and `calc.py`

## Example Operations 
Below are a list of example operations rated by how difficult they are to complete. Here is also a [list of finance operations](https://docs.google.com/document/d/1tWqVNCtFf0M6-Zeb1dY7aku0qB2iuT0CV0vGJ0rs_10/edit?usp=sharing) from our brain storm.
### Mild
At the mild level, these usually require just one operation. (hint: you can probably use a decorator to make your life easier)
- Addition, Multiplication, Subtraction, and Division
- Exponentiation and Square Rooting
- Mean, Median, Mode
- Quadratic Roots finder
- Unit conversion
- Money conversion 
### Medium
At the medium level, these tend to require loops, conditionals, recursion, etc.
- Prime number checker
- Greatest common factor 
- Find the equation of a line given two points in the xy plane
- Time zone calculator 
- Loan calculator
- Factorial Calculator
- Fibonnaci Sequence Calculator
- Collatz Conjecture Calculator
- Money conversion using an API and the `requests` library in python (e.g. [Exchange Rates API](https://exchangeratesapi.io/documentation/))
### Spicy
At the spicy level, these operations lend themselves to implementing a data structure, more complex algorithms, or combine making API calls with multiple calculations.
- Matrix Operations:
    - Read in a matrix from input and use lists to represent it. 
    - The following matrix operations: Add, Subtract, Multiply, Divide, Get Dimensions, and Transpose
    - Note: If you do this in vanilla python, this is a spicy challenge. If you use the `numpy` library, this is on the medium side.
- Algebra as a string (allowed symbols: `+`, `-`, `*`, `/`, `(`, and `)`) (hint: queues or finite state machines could be useful here)
- Weather Difference Calculator using the Open Weather API
    - Note: To do this one, you need to sign up and get an API key from them.
    - Use the `requests` library to access data from Open Weather's [Current Weather API](https://openweathermap.org/current) and create a weather difference calculator for today between two cities in the United States. It should take in two dates (some python libraries would be helpful for this) and then neatly report
        - The difference in average temperature
        - The difference in average wind speed
        - The geographical distance between the two locations
        - Emojis for each that represent the status of the weather that day (i.e sunny, cloudy, rainy, etc.)
## **FAQ**
### **Can I use external libraries?**
Yes! Be aware that this can either lower or increase the difficulty listed in this spec.
### **What do I do if I finish early**
Add more operations or increase the complexity of your interface.
### **What do I need to present?**
Just your program. When you present, demonstrate its functionality and answer the following questions in **6 minutes** max:
1. What is your project?
1. What are your glows and grows?
1. What were the challenges you faced when making your project?
1. Would you manage your time differently if you were to do this again?
### **Can I have additional files?**
Yes.