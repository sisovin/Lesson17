# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:58:04 2024

@author: chien 
"""

from turtle import tilt


tilt = " Chapter 17 - Lambda & Higher Order Functions in main.py "
print(f"{tilt}".upper().center(80, "="))
print("")
tilt = " # Advantages of using lambda functions: # "
print(f"{tilt}".center(80, "#"))
# 1. Conciseness: Lambda functions allow you to write small functions in a single line, making the code more concise and readable.
add = lambda x, y: x + y
print(f"Output = {add(2, 3)}")  # Output: 5

# 2. Inline Usage: They are useful for defining small functions that are used only once or a few times, especially as arguments to higher-order functions like map(), filter(), and sorted().
numbers = [1, 2, 3, 4]
squared = map(lambda x: x * x, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]

# 3. No Need for Naming: Lambda functions do not require a name, which can be useful to avoid polluting the namespace with unnecessary function names.
points = [(1, 3), (2, 1), (3, 2)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)

# 4. Functional Programming: They facilitate functional programming techniques by allowing functions to be passed as arguments and returned from other functions.
def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x * x, 5))  # Output: 25

# 5. Readability in Simple Cases: For simple operations, lambda functions can make the code more readable by reducing the need for separate function definitions.
numbers = [1, 2, 3, 4]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

# 6. Quick Prototyping: They are useful for quick prototyping and testing small pieces of functionality without the overhead of defining full functions.
print((lambda x, y: x + y)(3, 4))  # Output: 7