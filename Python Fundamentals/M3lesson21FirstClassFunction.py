# =============================================================
# LESSON 21: First-Class Functions
# =============================================================
# In Python, functions are FIRST-CLASS OBJECTS -- you can:
#   - Assign them to variables
#   - Pass them to other functions
#   - Return them from functions
#   - Store them in lists/dicts
# This is the foundation of functional programming patterns.

# ---------------------------------------------------------
# 1. Assign functions to variables
# ---------------------------------------------------------
def greet(name):
    return f"Hello, {name}!"

say_hello = greet      # assign the function object to a variable
print(say_hello("Alice"))    # Hello, Alice!
# say_hello and greet point to the same function.

# ---------------------------------------------------------
# 2. Pass functions as arguments (callbacks)
# ---------------------------------------------------------
def apply_operation(a, b, operation):
    """Execute an operation on two numbers."""
    return operation(a, b)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

print(apply_operation(5, 3, add))        # 8
print(apply_operation(5, 3, multiply))   # 15

# ---------------------------------------------------------
# 3. Return functions from functions
# ---------------------------------------------------------
def make_multiplier(factor):
    """Return a function that multiplies by a fixed factor."""
    def multiplier(x):
        return x * factor
    return multiplier

times_three = make_multiplier(3)
times_five = make_multiplier(5)

print(times_three(10))   # 30
print(times_five(10))    # 50

# ---------------------------------------------------------
# 4. Store functions in lists/dicts
# ---------------------------------------------------------
operations = [add, multiply]

for op in operations:
    print(op(4, 2))   # 6, then 8

function_map = {
    "add": add,
    "multiply": multiply,
    "subtract": lambda x, y: x - y
}

print(function_map["add"](10, 5))         # 15
print(function_map["subtract"](10, 5))    # 5

# ---------------------------------------------------------
# 5. map() and filter() -- practical built-in uses
# ---------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# map(func, iterable) applies func to each element
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)   # [2, 4, 6, 8, 10]

# filter(func, iterable) keeps elements where func returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)       # [2, 4]

# ---------------------------------------------------------
# 6. sorted() with a custom key function
# ---------------------------------------------------------
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort by age using a key function
by_age = sorted(people, key=lambda p: p["age"])
print("By age:", [(p["name"], p["age"]) for p in by_age])
# By age: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

# ---------------------------------------------------------
# REAL-WORLD: Decorator pattern (sneak preview)
# ---------------------------------------------------------
def log_call(func):
    """A decorator: a function that takes a function and returns
    an enhanced version of it."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}")
        result = func(*args, **kwargs)
        print(f"  -> returned {result}")
        return result
    return wrapper

# Apply the decorator
logged_add = log_call(add)
logged_add(5, 3)
# Output:
# Calling add with args=(5, 3)
#   -> returned 8

# ---------------------------------------------------------
# RULE OF THUMB:
#   - Functions are objects; treat them like any other value.
#   - Pass functions to other functions for customizable behavior.
#   - Return functions to create specialized versions.
#   - This enables map/filter, sorting with custom keys, callbacks,
#     and decorators -- powerful patterns you'll use constantly.
# ---------------------------------------------------------
