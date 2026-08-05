# =============================================================
# LESSON 20: **kwargs -- accept any number of keyword arguments
# =============================================================
# The `**kwargs` parameter lets a function accept ANY number of
# keyword arguments and collects them into a DICTIONARY.
# "kwargs" stands for "keyword arguments" -- you could call it
# **options or **metadata, but **kwargs is standard.

def show(**kwargs):
    """Print all keyword arguments as key-value pairs."""
    for key in kwargs:
        print(key, "->", kwargs[key])

show(name="Alice", city="Delhi")
# Output:
# name -> Alice
# city -> Delhi

# kwargs is a dict, so you can access values by key, iterate,
# check membership, etc.

# =================================================================
# RULE: the order of parameters in a function signature matters
# =================================================================
# When mixing regular params, *args, and **kwargs:
#   1. Regular positional parameters come first (required or default)
#   2. *args comes next (collects extra positional arguments)
#   3. **kwargs comes last (collects extra keyword arguments)

def demo(a, *args, **kwargs):
    """A function that accepts all three kinds of arguments."""
    print("a (required):", a)
    print("args (extra positional):", args)
    print("kwargs (extra keyword):", kwargs)

demo(
    10,           # fills `a`
    20, 30,       # go into `args`
    name="Alice", # go into `kwargs`
    age=25
)
# Output:
# a (required): 10
# args (extra positional): (20, 30)
# kwargs (extra keyword): {'name': 'Alice', 'age': 25}

# =================================================================
# EXTRA: accessing kwargs values by key
# =================================================================

def create_user(**kwargs):
    """Create a user dict from any provided keyword arguments."""
    return kwargs

user = create_user(name="Bob", age=30, city="Mumbai", verified=True)
print(user)
# {'name': 'Bob', 'age': 30, 'city': 'Mumbai', 'verified': True}

# You can check if a key is in kwargs:
def greet(**kwargs):
    if "name" in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello, stranger!")

greet(name="Alice")   # Hello, Alice!
greet(age=30)         # Hello, stranger!

# You can use kwargs.get(key, default):
def process(**kwargs):
    timeout = kwargs.get("timeout", 30)
    retries = kwargs.get("retries", 3)
    print(f"timeout={timeout}, retries={retries}")

process()                              # timeout=30, retries=3 (all defaults)
process(timeout=60)                    # timeout=60, retries=3 (one custom)
process(timeout=60, retries=5)          # timeout=60, retries=5 (all custom)

# =================================================================
# EXTRA: unpacking a dictionary into **kwargs with `**`
# =================================================================
# The SAME `**` operator can unpack a dictionary when CALLING a
# function, spreading its key-value pairs as separate keyword arguments.

config = {"name": "Charlie", "age": 35, "city": "Bangalore"}
user = create_user(**config)
# Equivalent to: create_user(name="Charlie", age=35, city="Bangalore")
print(user)

# This is useful when you have configuration/options in a dict
# but the function expects separate keyword arguments.

# =================================================================
# REAL-WORLD EXAMPLE: flexible data building
# =================================================================

def build_api_request(**options):
    """Build an API request dict from any options provided."""
    request = {
        "method": options.get("method", "GET"),
        "timeout": options.get("timeout", 30),
        "headers": options.get("headers", {}),
        "data": options.get("data", None)
    }
    return request

print(build_api_request())
# {'method': 'GET', 'timeout': 30, 'headers': {}, 'data': None}

print(build_api_request(method="POST", timeout=60))
# {'method': 'POST', 'timeout': 60, 'headers': {}, 'data': None}

# =================================================================
# REAL-WORLD EXAMPLE: database query with dynamic filters
# =================================================================

def query_users(**filters):
    """Simulate a database query with dynamic filters."""
    # In real life, this would build a SQL WHERE clause or similar.
    query = "SELECT * FROM users WHERE "
    conditions = []
    for key, value in filters.items():
        conditions.append(f"{key} = '{value}'")
    return query + " AND ".join(conditions)

print(query_users(name="Alice", age=25))
# SELECT * FROM users WHERE name = 'Alice' AND age = '25'

print(query_users(city="Delhi"))
# SELECT * FROM users WHERE city = 'Delhi'

# =================================================================
# REAL-WORLD EXAMPLE: employee profile with variable details
# =================================================================

def employee(name, *skills, **details):
    """Create an employee profile with flexible skills and details."""
    print("Name:", name)
    print("Skills:", skills)
    print("Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

employee(
    "Alice",
    "Python",
    "FastAPI",
    city="Delhi",
    age=25,
    department="Engineering"
)
# Output:
# Name: Alice
# Skills: ('Python', 'FastAPI')
# Details:
#   city: Delhi
#   age: 25
#   department: Engineering

# =================================================================
# EXTRA: combining *args, **kwargs, and unpacking in one expression
# =================================================================

def process_data(operation, *numbers, **options):
    """Process numbers with an operation and flexible options."""
    print(f"Operation: {operation}")
    print(f"Numbers: {numbers}")
    print(f"Options: {options}")

# Call with mixed arguments AND unpacked sequences:
data = [10, 20, 30]
opts = {"debug": True, "verbose": False}
process_data("sum", *data, **opts)
# Output:
# Operation: sum
# Numbers: (10, 20, 30)
# Options: {'debug': True, 'verbose': False}

# =================================================================
# COMPARISON TABLE: *args vs **kwargs
# =================================================================
# *args:
#   - Collects POSITIONAL arguments into a TUPLE
#   - Access by index: args[0], args[1], ...
#   - Unpack when calling with: func(*list_or_tuple)
#
# **kwargs:
#   - Collects KEYWORD arguments into a DICT
#   - Access by key: kwargs['key'] or kwargs.get('key', default)
#   - Unpack when calling with: func(**dict)

# =================================================================
# RULE OF THUMB:
#   - Use *args when you need a variable number of positional args.
#   - Use **kwargs when you need a variable number of keyword args.
#   - Combine them for ultimate flexibility.
#   - The * and ** operators work both ways:
#     - In function definition: collect arguments
#     - In function call: unpack sequences/dicts
# =================================================================
