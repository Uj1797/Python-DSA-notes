# =============================================================
# LESSON 19: *args -- accept any number of positional arguments
# =============================================================
# The `*args` parameter lets a function accept ANY number of
# positional arguments and collects them into a TUPLE.
# "args" is just a convention -- you could call it *numbers or
# *items, but *args is the standard name.

def add(*args):
    print(args)  # args is a tuple of all positional arguments passed

add(1, 2, 3, 4, 5)
# Output: (1, 2, 3, 4, 5)

# args is a tuple, so you can loop over it, index it, etc.
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3, 4, 5))   # 15
print(add(10, 20))           # 30
print(add())                 # 0 (empty tuple sums to 0)

# =================================================================
# RULE: when you mix regular params and *args
# =================================================================
# Regular parameters (required or with defaults) come BEFORE *args.
# Keyword-only parameters (with ->) come AFTER *args.

def test(a, *args):
    print("a:", a)
    print("args:", args)

test(1, 2, 3)
# a: 1
# args: (2, 3)

# The first positional argument fills `a`; the rest go into `args`.

# This WRONG because keyword params would come before *args:
# def test(*args, a):  # ERROR! a is keyword-only but before *args in spirit
#     ...

# CORRECT: if you want keyword-only params after *args:
def test_correct(a, *args, b=10):
    print("a:", a)
    print("args:", args)
    print("b (keyword-only):", b)

test_correct(1, 2, 3, b=20)
# a: 1
# args: (2, 3)
# b (keyword-only): 20

# =================================================================
# EXTRA: unpacking an iterable into *args with `*`
# =================================================================
# The SAME `*` operator can unpack a list/tuple when CALLING
# a function, spreading its elements as separate positional arguments.

numbers = [10, 20, 30, 40, 50]
print(add(*numbers))   # 150
# The * unpacks the list, passing each element as a separate arg.
# Equivalent to: add(10, 20, 30, 40, 50)

# This is useful when you have data in a list/tuple but the function
# expects separate arguments.

# =================================================================
# REAL-WORLD EXAMPLE: flexible sum/min/max/print replacements
# =================================================================

def my_sum(*numbers):
    """Sum any number of numbers passed as arguments."""
    return sum(numbers)

def my_min(*numbers):
    """Find the minimum of any number of numbers."""
    if not numbers:
        return None
    smallest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
    return smallest

def my_max(*numbers):
    """Find the maximum of any number of numbers."""
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

print(my_sum(5, 10, 15, 20))           # 50
print(my_min(100, 50, 200, 25))         # 25
print(my_max(100, 50, 200, 25))         # 200

# =================================================================
# REAL-WORLD EXAMPLE: format_string with flexible substitution
# =================================================================

def format_string(template, *values):
    """Replace {} placeholders with provided values in order."""
    result = template
    for value in values:
        result = result.replace("{}", str(value), 1)  # replace first {} only
    return result

print(format_string("Hello {}, you are {} years old.", "Alice", 25))
# Hello Alice, you are 25 years old.

# =================================================================
# REAL-WORLD EXAMPLE: logging with variable number of context items
# =================================================================

def log_event(event_type, *context):
    """Log an event with any number of context details."""
    message = f"[{event_type}]"
    for item in context:
        message += f" {item}"
    return message

print(log_event("LOGIN", "user@example.com", "IP: 192.168.1.1", "browser: Chrome"))
# [LOGIN] user@example.com IP: 192.168.1.1 browser: Chrome

# =================================================================
# RULE OF THUMB:
#   - Use *args when a function needs to accept a variable number
#     of positional arguments.
#   - *args collects them into a TUPLE, which you can iterate, index,
#     slice, or convert as needed.
#   - The unpacking operator * works both ways:
#     - In function definition: collect arguments into a tuple
#     - In function call: spread a sequence into separate arguments
# =================================================================
