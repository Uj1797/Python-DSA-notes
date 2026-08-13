# =============================================================
# LESSON 1: Introduction to Python & Variables
# =============================================================
# Python is a high-level programming language designed to be
# readable and easy to learn. Variables store data that your
# program uses.

# ---------------------------------------------------------
# What is a variable?
# ---------------------------------------------------------
# A VARIABLE is a named container that holds a value.
# Think of it as a labeled box storing some data.

# Creating variables (assignment)
name = "Alice"         # variable `name` holds the string "Alice"
age = 25               # variable `age` holds the number 25
score = 95.5           # variable `score` holds a decimal number

# Print the values stored in variables
print(name)            # Alice
print(age)             # 25
print(score)           # 95.5

# ---------------------------------------------------------
# Naming variables (rules and conventions)
# ---------------------------------------------------------
# Rules:
#   - Variable names must start with a letter or underscore (_)
#   - Can contain letters, numbers, and underscores
#   - Are case-sensitive (Name and name are different)
#   - Cannot use Python keywords (if, for, def, etc.)

# Good variable names (descriptive):
student_name = "Bob"
total_score = 100
is_active = True

# Avoid these (unclear or hard to read):
# x = "Bob"            # too generic
# n = 100              # unclear what n represents
# Name = "Bob"         # inconsistent with conventions

# ---------------------------------------------------------
# Types of values (data types)
# ---------------------------------------------------------
# Every value in Python has a TYPE. The main types are:

# Strings (text) -- enclosed in quotes
text = "Hello"
print(text, type(text))       # Hello <class 'str'>

# Integers (whole numbers) -- no decimal point
count = 42
print(count, type(count))     # 42 <class 'int'>

# Floats (decimal numbers) -- have a decimal point
temperature = 98.6
print(temperature, type(temperature))  # 98.6 <class 'float'>

# Booleans (True or False) -- used for logic
is_valid = True
is_empty = False
print(is_valid, type(is_valid))   # True <class 'bool'>

# ---------------------------------------------------------
# Reassigning variables (changing values)
# ---------------------------------------------------------
count = 10
print(count)     # 10

count = 20       # reassign the same variable to a new value
print(count)     # 20

count = count + 5  # use the old value to calculate a new value
print(count)     # 25

# ---------------------------------------------------------
# Multiple assignment
# ---------------------------------------------------------
# Assign multiple variables in one line
x, y, z = 1, 2, 3
print(x, y, z)   # 1 2 3

# Swap two variables
a = 5
b = 10
a, b = b, a      # elegant Python swapping
print(a, b)      # 10 5

# ---------------------------------------------------------
# Naming conventions in Python (PEP 8 style guide)
# ---------------------------------------------------------
# Use lowercase with underscores (snake_case) for variables:
student_age = 20        # GOOD
studentAge = 20         # works, but not conventional
STUDENT_AGE = 20        # reserved for constants

# CONSTANTS (values that never change) use UPPERCASE:
MAX_ATTEMPTS = 3
PI = 3.14159

# ---------------------------------------------------------
# Getting user input
# ---------------------------------------------------------
# The input() function lets users type data
# user_name = input("What is your name? ")
# print(f"Hello, {user_name}!")
# (Commented out so this file can run without user interaction)

# ---------------------------------------------------------
# RULE OF THUMB:
#   - Variables store data with meaningful names
#   - Use lowercase with underscores (snake_case)
#   - Every value has a type: str, int, float, bool
#   - You can reassign variables to new values at any time
#   - Pick clear, descriptive names -- future you will thank you
# ---------------------------------------------------------
