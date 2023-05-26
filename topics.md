We covered a lot of content and techniques in python. Here's a list for reference:

External Libraries you may have seen:
- `sys`
- `time`
- `requests`
- `os`

Day 2: Data Types, VS Code, Command Line
- Int, float, str types
- Type casting
- `If/elif/else`
- Logical Operators: `==, ===, !=, <,>, <=, >=`
- Advanced Logical Operators: `and, in, or, not, is`
- `==` vs `is`
- Match statements: 
```
match value:
    case val1:
        # do something
    case val2:
        # do something
    ...
    case other:
        # do if no match
```
- Inline If statements: `"true" if condition else "false"`
- Escape Sequences (`\', \", \n, \t`, ...)
- ANSI Escape Sequences (Terminal Control): see helpful-code folder 

Day 3: Lists, Dictionaries, Loops
- Lists, Dictionaries, and their methods
- `dict.keys()` vs `dict.values()`
- `for item in iterable `loops
- `for i in range(0,n) `loops
- nested lists and dictionaries
- `nested_dict.sort(key = lambda x : x[key][index][key][...]...)`
- List comprehensions: `foo(x) for x in iterable` or `var = [foo(x) for x in iterable]`

Day 4:
- `def` keyword to write a function
- `return` as a breakpoint
- default args: `def foo(arg="default")` 
- advanced functions:
    - **callback functions**: Any function that takes in another function as a parameter
    - **anonymous lambda functions**: A way to write a function without storing it as a variable/in the namespace, `lambda args : foo(args)`. Commonly used with callback functions/methods like `map`, `filter`, `.sort()`, etc.
    - **decorator functions**: A function that takes in a function `@foo` method
    - **generator functions**: a function that uses `yield` to return an iterator that can be used in a `for val in iterator` loop
    - **recursive functions**: a function that calls itself
- OOP
    - `def __init__(self, ...)`  defines the constructor function
    - we define a blueprint for an Object using `class Object_Name` and call an instance using `Object_Name(...)`
    - the `self` keyword in a method definition of a class refers to the instance of an object 
    - methods: `def method_name(args):`, to call `instance.method_name(args)`
    - properties: in init, write `self.property = val...`, then to access, write `instance.property`, or if in class definition, `self.property`
    - magic/dunder methods are flanked by 2 underscores and allow your object to use built in python operators. Ex:
        - `__eq__(self, other)` runs when `==` is used
        - `__setitem__` and `__getitem__` are used with `[]` and `[]` assignment
        - `__str__` allows you to specify how to print your object/give a string representation
        - there are many more... googlealo
