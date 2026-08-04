# =============================================================
# LESSON 14: return -- sending a value back from a function
# =============================================================
# `return` does two things at once:
#   1. Immediately STOPS the function's execution (nothing after
#      it in that function runs).
#   2. Sends a value back to wherever the function was called.
# A function with no `return` (or a bare `return`) gives back
# `None` automatically.

def test():
    print("A")

    return           # function execution ends HERE

    print("B")        # never runs -- unreachable code after return

test()
# Output: A
# "B" is never printed because `return` ends the function before
# execution can reach that line.

# -------------------------------------------------------------
# Returning an actual value
# -------------------------------------------------------------
def hello():
    return "Hello"

print(hello())
# Output: Hello
# because hello() RETURNS the string "Hello", and print() displays
# whatever value it receives.

# -------------------------------------------------------------
# The crucial difference between printing and returning
# -------------------------------------------------------------
def add():
    print(10 + 20)     # this DISPLAYS 30 to the console...

x = add()               # ...but add() does not RETURN anything,
                          # so the result of calling it is None.
print(x)

# Output:
# 30      <- printed by add() itself, while it's running
# None    <- because add() has no return statement, so x = add()
#            stores None, and printing x shows None.

# -------------------------------------------------------------
# EXTRA: this is a very common beginner bug -- confusing
# "printing inside a function" with "returning a usable value".
# -------------------------------------------------------------
def add_and_return(a, b):
    return a + b        # this actually hands the result back

result = add_and_return(10, 20)
print(result)             # 30 -> now we can store/reuse the value

# -------------------------------------------------------------
# EXTRA: returning multiple values (as a tuple, see M1lesson7Tuples.py)
# -------------------------------------------------------------
def min_max(numbers):
    return min(numbers), max(numbers)      # packs two values into a tuple

low, high = min_max([4, 1, 9, 2])          # unpacks them into two variables
print(low, high)   # 1 9

# -------------------------------------------------------------
# EXTRA: early return -- a common, clean pattern for guard clauses
# -------------------------------------------------------------
def divide(a, b):
    if b == 0:
        return None          # bail out early, avoid dividing by zero
    return a / b

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # None -> handled gracefully instead of crashing
