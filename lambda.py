# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:51:46 2024

@author: chien
"""
# %%
from turtle import title
from functools import reduce


print("")
title = " Chapter 17 - Lambda & Higher Order Functions in lambda.py "
print(f"{title}".upper().center(80, "="))
print("")

title = " # Create a function called 'squared(num)': # "
print(f"{title}".center(80, "#"))

# Create a function called 'squared(num)' that takes a number and returns the number squared.
def squared(num): return num * num
# def squared(num): return num ** 2 # This is another way to write the same function. 
# lambda num : num * num # This is a lambda function that does the same thing.

title = " # Test the function # "
print(f"{title}".center(80, "*"))
print(f"Output= {squared(5)}") # Output= 25
print(f"Output= {squared(2)}") # Output= 4
  
print("")

title = " # Lambda Functions # "
print(f"{title}".center(80, "*"))
squared = lambda num: num * num
print(f"Output = {squared(4)}") # Output= 16
print(f"Output = {squared(8)}") # Output= 64

print("")
title = " # Higher Order Functions # "
print(f"{title}".center(80, "*"))
lambda arguments: arguments * arguments
add = lambda x, y: x + y
print(f"Output = {add(2, 3)}")  # Output: 5
print(f"Output = {add(5, 5)}")  # Output: 10

print("")
title = " # 1. Using a function as an argument: # "
print(f"{title}".center(80, "*"))
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

print(f"Output = {apply_function(square, 5)}")  # Output: 25
print(f"Output = {apply_function(square, 6)}")  # Output: 36

print("")
title = " # 2. Returning a function: # "
print(f"{title}".center(80, "*"))
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(f"Output = {add_five(3)}")  # Output: 8
print(f"Output = {add_five(10)}")  # Output: 15

print("")
title = " # Here are some common use cases: # "
print(f"{title}".center(80, "#"))
title = " # 1. Using with map() Function: The map() function applies a given function \n" \
        " # to all items in an input list. \n # "
print(f"{title}".center(80, "*"))
numbers = [1, 2, 3, 4]
squared = map(lambda x: x * x, numbers)
print(f"Output = {list(squared)}")  # Output: [1, 4, 9, 16]

print("")
title = " # 2. Using with filter() Function: The filter() function filters elements \n" \
        " # from a list based on a given function. \n # "
print(f"{title}".center(80, "*"))
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"Output = {list(even_numbers)}")  # Output: [2, 4, 6]

print("")
title = " # 3. Using with reduce() Function: The reduce() function applies a rolling \n" \
        " # computation to sequential pairs of values in a list. \n # "
print(f"{title}".center(80, "*"))
points = [(1, 2), (3, 1), (5, -1), (2, 3)]
sorted_points = sorted(points, key=lambda point: point[1])
print(f"Output = {sorted_points}")  # Output: [(5, -1), (3, 1), (1, 2), (2, 3)]

print("")
title = " # 4. Using with sorted() Function: The sorted() function sorts the elements \n" \
        " # of a list based on a given function. \n # "
print(f"{title}".center(80, "*"))
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(f"Output = {product}")  # Output: 24

print("")
title = " # 5. Inline Functions in GUI Callbacks: Lambda functions can be used for \n" \
        " #  short callback functions in GUI applications. \n # "
print(f"{title}".center(80, "*"))
import tkinter as tk

root = tk.Tk()
button = tk.Button(root, text="Click Me", command=lambda: print(f"{("Button Clicked!")}".center(80, "*")))
button.pack()
root.mainloop()

print("")
title = " # 6. Using with any() and all() Functions: Lambda functions can be used to create  \n" \
        " #  conditions for any() and all() functions. \n # "
print(f"{title}".center(80, "*"))
numbers = [1, 2, 3, 4, 5]
all_even = all(map(lambda x: x % 2 == 0, numbers))
print(f"Output = {all_even}")  # Output: False

print("")
title = " # add-two function #"
print(f"{title}".center(80, "#"))
def add_two(num): return num + 2 # This is a normal function that adds 2 to a number.
add_two = lambda num: num + 2 # This is a lambda function that does the same thing.
print(f"Output = {add_two(3)}") # Output= 5
# Shorthand for the above lambda function:
lambda num: num + 2
print(f"Output = {add_two(12)}") # Output= 14

print("")
title = " # sum_total function #"
print(f"{title}".center(80, "#"))
def sum_total(a, b): return a + b # This is a normal function that adds two numbers.
sum_total = lambda a, b: a + b # This is a lambda function that does the same thing.
print(f"Output = {sum_total(10, 8)}") # Output= 18
# Shorthand for the above lambda function:
lambda a, b: a + b
print(f"Output = {sum_total(5, 5)}") # Output= 10

print("")
title = " # Builder function #"
print(f"{title}".center(80, "#"))
def funcBuilder(x):
    return lambda num: num + x


add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(f"Output = {add_ten(7)}") # Output= 17
print(f"Output = {add_twenty(7)}") # Output= 27

print("")
title = " # Using Lambda Functions with the map() Square Array Function  #"
print(f"{title}".center(80, "#"))
numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(f"Output = {list(squared_nums)}") # Output= [9, 49, 144, 324, 400, 441]

print("")
title = " # Using Lambda Functions with the filter() Odd Number Function  #"
print(f"{title}".center(80, "#"))
odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(f"Output = {list(odd_nums)}") # Output= [3, 7, 21]

print("")
title = " # Using Lambda Functions with the filter() Even number Function  #"
print(f"{title}".center(80, "#"))
even_nums = filter(lambda num: num % 2 == 0, numbers)

print(f"Output = {list(even_nums)}") # Output= [12, 18, 20]

print("")
title = " # Using Lambda Functions with the reduce() Sum Function  #"
print(f"{title}".center(80, "#"))
from functools import reduce
numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(f"Output = {total}") # Output= 26

print(f"Output = {sum(numbers, 10)}") # Output= 26


names = ['Chieng Sisovin', 'Ou Sovanny', 'Phouthuon Viphop Jingleheimerschmidt'] # 59 characters

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0) # 0 is the initial value of the accumulator.

print(f"Output = {char_count}") # Output= 59 characters

print("")