# =============================================================
# LESSON 25: Decorators -- enhancing functions without changing them
# =============================================================
# A DECORATOR is a function that takes a function, wraps it with
# extra behavior, and returns the enhanced version.
# Use @decorator syntax to apply decorators cleanly.

# ---------------------------------------------------------
# Basic decorator pattern
# ---------------------------------------------------------
def simple_decorator(func):
    """A decorator that runs code before and after the wrapped function."""
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

# Apply the decorator manually:
def hello():
    print("Hello")

hello = simple_decorator(hello)  # wrapping
hello()
# Output:
# Before
# Hello
# After

# ---------------------------------------------------------
# Using the @decorator syntax (same as above, but cleaner)
# ---------------------------------------------------------
@simple_decorator
def goodbye():
    print("Goodbye")

goodbye()
# Output:
# Before
# Goodbye
# After

# ---------------------------------------------------------
# Decorators with arguments (passing through *args and **kwargs)
# ---------------------------------------------------------
def logging_decorator(func):
    """A decorator that prints the function name before calling it."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logging_decorator
def add(a, b):
    """Add two numbers."""
    return a + b

print(add(5, 3))   # Calling add, then 8

@logging_decorator
def greet(name, greeting="Hello"):
    """Greet someone."""
    return f"{greeting}, {name}!"

print(greet("Alice"))              # Calling greet, then Hello, Alice!
print(greet("Bob", greeting="Hi"))  # Calling greet, then Hi, Bob!

# ---------------------------------------------------------
# Preserving function metadata with functools.wraps
# ---------------------------------------------------------
import functools

def preserve_metadata(func):
    """A decorator that preserves the original function's metadata."""
    @functools.wraps(func)  # This copies name, docstring, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def multiply(x, y):
    """Multiply two numbers."""
    return x * y

print(multiply.__name__)  # multiply (not 'wrapper')
print(multiply.__doc__)   # Multiply two numbers. (preserved)
print(multiply(4, 5))     # Calling multiply, then 20

# Without @functools.wraps, the function name and docstring
# would be lost (wrapper, None).

# ---------------------------------------------------------
# Real-world example: timing decorator
# ---------------------------------------------------------
import time

def timer(func):
    """A decorator that measures how long a function takes."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """A function that takes a moment."""
    time.sleep(0.1)
    return "Done"

slow_function()
# Output: slow_function took 0.1xxx seconds

# ---------------------------------------------------------
# Real-world example: authentication decorator
# ---------------------------------------------------------
def require_auth(func):
    """A decorator that simulates requiring authentication."""
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated"):
            print("ERROR: User not authenticated")
            return None
        print(f"User {user['name']} is authenticated. Proceeding...")
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def delete_account(user):
    """Delete a user account (requires authentication)."""
    return f"Account for {user['name']} deleted"

alice = {"name": "Alice", "authenticated": True}
bob = {"name": "Bob", "authenticated": False}

print(delete_account(alice))   # Proceeding... Account for Alice deleted
print(delete_account(bob))     # ERROR: User not authenticated

# ---------------------------------------------------------
# Stacking multiple decorators
# ---------------------------------------------------------
def decorator_a(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("A: before")
        result = func(*args, **kwargs)
        print("A: after")
        return result
    return wrapper

def decorator_b(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("B: before")
        result = func(*args, **kwargs)
        print("B: after")
        return result
    return wrapper

@decorator_a
@decorator_b
def my_function():
    print("function running")

my_function()
# Output:
# A: before
# B: before
# function running
# B: after
# A: after
# Decorators are applied bottom-to-top, but execute outside-in

# ---------------------------------------------------------
# RULE OF THUMB:
#   - A decorator is a function that wraps another function
#   - Use @decorator syntax for clean, readable code
#   - Always use @functools.wraps to preserve function metadata
#   - Decorators are perfect for cross-cutting concerns: logging,
#     authentication, timing, caching, validation, rate-limiting
#   - Multiple decorators stack; innermost decorator is applied first
# ---------------------------------------------------------
