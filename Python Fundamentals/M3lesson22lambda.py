# =============================================================
# LESSON 22: Lambda Functions (anonymous functions)
# =============================================================
# A lambda is a tiny nameless function written in one line.
# SYNTAX: lambda arguments: expression
# Think of it as "def but shorter" for simple operations.

# ---------------------------------------------------------
# Basic lambdas
# ---------------------------------------------------------
# Instead of:
# def square(x):
#     return x * x
# You can write:
square = lambda x: x * x
print(square(5))   # 25

# Multiple arguments:
add = lambda a, b: a + b
print(add(3, 7))   # 10

greet = lambda name: f"Hello, {name}!"
print(greet("Alice"))   # Hello, Alice!

# ---------------------------------------------------------
# THE IMPORTANT RULE: only ONE expression allowed
# ---------------------------------------------------------
# This works:
result = (lambda x: x * 2)(10)
print(result)   # 20

# This DOES NOT work (multiple statements):
# bad = lambda x:
#     print(x)
#     return x * 2
# Multiple statements aren't allowed in a lambda.
# If your logic needs multiple lines, use `def` instead.

# ---------------------------------------------------------
# Practical use: with map() and filter()
# ---------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6]

# map(lambda, list) applies lambda to each element
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)   # [2, 4, 6, 8, 10, 12]

# filter(lambda, list) keeps elements where lambda returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)   # [2, 4, 6]

# ---------------------------------------------------------
# Practical use: with sorted() and custom key
# ---------------------------------------------------------
words = ["python", "java", "c", "rust"]

# Sort by word length
by_length = sorted(words, key=lambda w: len(w))
print("By length:", by_length)   # ['c', 'java', 'rust', 'python']

# Sort by last character
by_last_char = sorted(words, key=lambda w: w[-1])
print("By last char:", by_last_char)   # ['c', 'java', 'python', 'rust']

# ---------------------------------------------------------
# When to use lambda vs def
# ---------------------------------------------------------
# Use lambda for: simple one-line operations, inline with map/filter/sorted
# Use def for: anything requiring multiple statements, named functions you call repeatedly

# Bad: complex logic in a lambda
# result = list(map(lambda x: x * 2 if x > 5 else x, numbers))  # unreadable

# Better: use def if it gets complicated
def double_if_big(x):
    """Double x if it's greater than 5, else return as-is."""
    return x * 2 if x > 5 else x

result = list(map(double_if_big, numbers))
print("Doubled if big:", result)   # [1, 2, 3, 4, 5, 12]

# ---------------------------------------------------------
# RULE OF THUMB:
#   - Lambda = quick, throwaway function for simple operations
#   - Keep it to ONE expression
#   - Use for map/filter/sorted/callbacks where a full function is overkill
#   - If you need multiple lines, use def instead
# ---------------------------------------------------------
