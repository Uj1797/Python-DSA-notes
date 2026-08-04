# =============================================================
# LESSON 13: Functions -- defining and calling, parameters
# =============================================================
# A function is a reusable, named block of code. `def` defines
# it; the code inside only runs when the function is CALLED.

def greet():
    print("Hello")

greet()      # "Hello" is only printed now, when we call greet()

# -------------------------------------------------------------
# PARAMETERS -- values passed into a function to customize its behavior
# -------------------------------------------------------------
def greet(name):          # `name` is a parameter (a placeholder)
    print("Hello", name)

greet("Alice")   # "Alice" here is the ARGUMENT (the actual value passed in)

# NOTE: redefining `greet` above with `def greet(name):` completely
# REPLACES the earlier no-argument `greet()`. Python doesn't support
# overloading by argument count -- the latest `def` wins. Calling the
# old `greet()` with no arguments now would raise a TypeError.

# -------------------------------------------------------------
# You can pass a variable as the argument, not just a literal
# -------------------------------------------------------------
person = "Bob"
greet(person)      # Hello Bob

# -------------------------------------------------------------
# Real-world shape: this is exactly the pattern used by web
# frameworks like FastAPI -- a decorator "registers" a function
# to run automatically when a specific request comes in.
# -------------------------------------------------------------
# @app.get("/users")
# def get_users():
#     ...

# -------------------------------------------------------------
# Calling the same function repeatedly, e.g. inside a loop
# -------------------------------------------------------------
def welcome(name):
    print("Welcome", name)

users = [
    "Alice",
    "Bob",
    "Charlie"
]

for user in users:
    welcome(user)     # Welcome Alice / Welcome Bob / Welcome Charlie

print("Done")

# -------------------------------------------------------------
# EXTRA: default parameter values
# -------------------------------------------------------------
def greet_with_default(name="stranger"):
    print("Hi", name)

greet_with_default()          # Hi stranger  -> uses the default
greet_with_default("Dana")     # Hi Dana      -> overrides the default

# -------------------------------------------------------------
# EXTRA: multiple parameters, positional vs keyword arguments
# -------------------------------------------------------------
def describe_pet(name, animal_type):
    print(f"{name} is a {animal_type}")

describe_pet("Rex", "dog")                     # positional: order matters
describe_pet(animal_type="cat", name="Milo")   # keyword: order doesn't matter,
                                                  # since arguments are named explicitly

# -------------------------------------------------------------
# EXTRA: docstrings -- documenting what a function does
# -------------------------------------------------------------
def add(a, b):
    """Return the sum of a and b."""
    return a + b

print(add(2, 3))       # 5
print(add.__doc__)      # Return the sum of a and b.
