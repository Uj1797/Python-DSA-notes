# =============================================================
# LESSON 23: Closures
# =============================================================
# A CLOSURE is a function that "remembers" variables from its
# enclosing (outer) scope, even after the outer function returns.
# The inner function has access to the outer function's local
# variables -- this forms a closure.

# ---------------------------------------------------------
# Basic closure example
# ---------------------------------------------------------
def outer():
    message = "Hello"

    def inner():
        print(message)  # inner() accesses outer()'s variable

    return inner

# Call outer() to get the inner function
f = outer()
f()   # Output: Hello
# Even though outer() finished, inner() still has access to `message`

# ---------------------------------------------------------
# Closures with parameters
# ---------------------------------------------------------
def multiplier(x):
    """Returns a function that multiplies by x."""
    def multiply(number):
        return number * x  # multiply() closes over x
    return multiply

times_two = multiplier(2)
times_five = multiplier(5)

print(times_two(10))    # 20  (10 * 2)
print(times_five(10))   # 50  (10 * 5)
# Each closure remembers its own value of x

# ---------------------------------------------------------
# More closure examples
# ---------------------------------------------------------
def make_adder(n):
    def add(x):
        return x + n
    return add

plus_100 = make_adder(100)
print(plus_100(50))   # 150

# Closure in action: functions with customized behavior
def outer_func():
    x = 10
    def inner_func():
        print(x)
    return inner_func

f = outer_func()
f()   # Output: 10

def make_text_processor(prefix):
    """Return a function that adds a prefix to text."""
    def process(text):
        return f"{prefix}: {text}"
    return process

log = make_text_processor("LOG")
error = make_text_processor("ERROR")

print(log("Application started"))      # LOG: Application started
print(error("Something went wrong"))    # ERROR: Something went wrong

# ---------------------------------------------------------
# REAL-WORLD: Authentication decorator pattern
# ---------------------------------------------------------
def require_role(required_role):
    """Return a checker function that validates user roles."""
    def checker(user):
        if user.get("role") == required_role:
            return True
        return False
    return checker

# Create specialized checkers
is_admin = require_role("admin")
is_user = require_role("user")

alice = {"name": "Alice", "role": "admin"}
bob = {"name": "Bob", "role": "user"}

print(is_admin(alice))   # True
print(is_admin(bob))     # False
print(is_user(bob))      # True

# ---------------------------------------------------------
# IMPORTANT: modifying closure variables with nonlocal
# ---------------------------------------------------------
# If you want the inner function to MODIFY a closure variable,
# you must use the `nonlocal` keyword.

def counter_broken():
    """This doesn't work as a counter -- count never changes."""
    count = 0
    def increment():
        return count + 1  # just reads count, doesn't modify it
    return increment

c_broken = counter_broken()
print(c_broken())   # 1
print(c_broken())   # 1 (still 1, not 2!)

# FIX: use nonlocal to modify the closure variable
def counter_fixed():
    """A proper counter that maintains state."""
    count = 0
    def increment():
        nonlocal count  # allow modification of closure variable
        count += 1
        return count
    return increment

c_fixed = counter_fixed()
print(c_fixed())    # 1
print(c_fixed())    # 2
print(c_fixed())    # 3 (now it works!)

# ---------------------------------------------------------
# REAL-WORLD: stateful function
# ---------------------------------------------------------
def rate_limiter(max_calls):
    """Return a function that tracks and limits call counts."""
    calls = 0
    def call_allowed():
        nonlocal calls
        if calls < max_calls:
            calls += 1
            return True
        return False
    return call_allowed

api_limit = rate_limiter(3)
print(api_limit())   # True (1st call)
print(api_limit())   # True (2nd call)
print(api_limit())   # True (3rd call)
print(api_limit())   # False (limit reached)

# ---------------------------------------------------------
# RULE OF THUMB:
#   - Closures let inner functions "remember" outer variables
#   - Use closures to create functions with customized behavior
#   - Use `nonlocal` if the inner function needs to MODIFY a closure variable
#   - Closures are the foundation of decorators and factories
# ---------------------------------------------------------
