# Chapter 17 - Lambda & Higher Order Functions

## Learn Python fast with some content ideas

Learning Python is a great choice, especially given your interest in web development, mobile app development, and software engineering. Here are some excellent resources to get you started:

**1. LearnPython.org:** This interactive Python tutorial offers free lessons for beginners. It covers topics like variables, loops, functions, and more. You can even get certified after completing the [`tutorials[1]`](https://www.learnpython.org/).

**2. Python Official Documentation:** The official Python documentation provides comprehensive information about the language. Start with the Python Tutorial for beginners and explore further as you gain [`confidence[2]`](https://stackoverflow.com/questions/70577/best-online-resource-to-learn-python).

**3. freeCodeCamp’s Python Courses:**
**- [`Full Course for Beginners`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/):** This YouTube course covers programming basics, including lists, conditionals, strings, and small projects like a calculator and a guessing game.
**- [`The Ultimate Python Beginner’s Handbook`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/)** Dive deeper into Python concepts and explore its growing popularity [`3`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/) and [`4`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/).

**REMEMBER:** practice coding regularly, work on small projects, and explore real-world examples.

## What is Lambda & Higher Order Functions in Python?

### Lambda Functions in Python

Lambda functions are small anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions are often used for short, throwaway functions.

**Syntax:**

```python
lambda arguments: expression
```

**Example:**

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

### Higher Order Functions in Python

Higher-order functions are functions that can take other functions as arguments or return them as results. This allows for more abstract and flexible code.

**Examples:**

1. **Using a function as an argument:**

   ```python
   def apply_function(func, value):
       return func(value)

   def square(x):
       return x * x

   print(apply_function(square, 5))  # Output: 25
   ```

2. **Returning a function:**

   ```python
   def outer_function(x):
       def inner_function(y):
           return x + y
       return inner_function

   add_five = outer_function(5)
   print(add_five(3))  # Output: 8
   ```

Lambda functions are often used with higher-order functions like `map()`, `filter()`, and `reduce()`.

**Example with `map()`:**

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x * x, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]
```

## What are some common use cases for lambda functions in Python?

Lambda functions in Python are often used in scenarios where small, throwaway functions are needed. Here are some common use cases:

1. **Using with `map()` Function:**
   The `map()` function applies a given function to all items in an input list.

   ```python
   numbers = [1, 2, 3, 4]
   squared = map(lambda x: x * x, numbers)
   print(list(squared))  # Output: [1, 4, 9, 16]
   ```

2. **Using with `filter()` Function:**
   The `filter()` function constructs an iterator from elements of an iterable for which a function returns true.

   ```python
   numbers = [1, 2, 3, 4, 5, 6]
   even_numbers = filter(lambda x: x % 2 == 0, numbers)
   print(list(even_numbers))  # Output: [2, 4, 6]
   ```

3. **Using with `sorted()` Function:**
   The `sorted()` function returns a new sorted list from the elements of any iterable.

   ```python
   points = [(1, 2), (3, 1), (5, -1), (2, 3)]
   sorted_points = sorted(points, key=lambda point: point[1])
   print(sorted_points)  # Output: [(5, -1), (3, 1), (1, 2), (2, 3)]
   ```

4. **Using with `reduce()` Function:**
   The `reduce()` function from the `functools` module applies a rolling computation to sequential pairs of values in a list.

   ```python
   from functools import reduce
   numbers = [1, 2, 3, 4]
   product = reduce(lambda x, y: x * y, numbers)
   print(product)  # Output: 24
   ```

5. **Inline Functions in GUI Callbacks:**
   Lambda functions can be used for short callback functions in GUI applications.

   ```python
   import tkinter as tk

   root = tk.Tk()
   button = tk.Button(root, text="Click Me", command=lambda: print("Button Clicked"))
   button.pack()
   root.mainloop()
   ```

6. **Using with `any()` and `all()` Functions:**
   Lambda functions can be used to create conditions for `any()` and `all()` functions.
   ```python
   numbers = [1, 2, 3, 4, 5]
   all_even = all(map(lambda x: x % 2 == 0, numbers))
   print(all_even)  # Output: False
   ```

These are just a few examples of how lambda functions can be used to simplify code and make it more readable in Python.

## Shorthand of lambda function

What is the shorthand of lambda function?
Is it this code:

### Create a function called 'squared(num)' that takes a number and returns the number squared.

def squared(num): return num \* num

### def squared(num): return num \*\* 2 # This is another way to write the same function.

### lambda num : num \* num # This is a lambda function that does the same thing.

Yes, the shorthand for a lambda function is indeed the line:

```python
lambda num: num * num
```

This lambda function is equivalent to the `squared` function defined as:

```python
def squared(num): return num * num
```

In the context of your file [`lambda.py`], the lambda function can be used as follows:

```python
squared = lambda num: num * num
```

This creates an anonymous function that takes a single argument `num` and returns `num` squared.

## What are the advantages of using lambda functions in Python?

Lambda functions in Python offer several advantages, particularly in scenarios where concise and inline functions are beneficial. Here are some key advantages:

1. **Conciseness:**
   Lambda functions allow you to write small functions in a single line, making the code more concise and readable.

   ```python
   add = lambda x, y: x + y
   ```

2. **Inline Usage:**
   They are useful for defining small functions that are used only once or a few times, especially as arguments to higher-order functions like `map()`, `filter()`, and `sorted()`.

   ```python
   numbers = [1, 2, 3, 4]
   squared = map(lambda x: x * x, numbers)
   print(list(squared))  # Output: [1, 4, 9, 16]
   ```

3. **No Need for Naming:**
   Lambda functions do not require a name, which can be useful to avoid polluting the namespace with unnecessary function names.

   ```python
   sorted_points = sorted(points, key=lambda point: point[1])
   ```

4. **Functional Programming:**
   They facilitate functional programming techniques by allowing functions to be passed as arguments and returned from other functions.

   ```python
   def apply_function(func, value):
       return func(value)

   print(apply_function(lambda x: x * x, 5))  # Output: 25
   ```

5. **Readability in Simple Cases:**
   For simple operations, lambda functions can make the code more readable by reducing the need for separate function definitions.

   ```python
   numbers = [1, 2, 3, 4]
   even_numbers = filter(lambda x: x % 2 == 0, numbers)
   print(list(even_numbers))  # Output: [2, 4]
   ```

6. **Quick Prototyping:**
   They are useful for quick prototyping and testing small pieces of functionality without the overhead of defining full functions.
   ```python
   print((lambda x, y: x + y)(3, 4))  # Output: 7
   ```

While lambda functions are powerful and useful, they should be used judiciously. For more complex operations, traditional function definitions with `def` are often more readable and maintainable.
