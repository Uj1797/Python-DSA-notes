# =============================================================
# LESSON 4: Basic Data Types
# =============================================================
# Python's core built-in types you'll use constantly:
#   int    -> whole numbers            (20, -5, 0)
#   float  -> decimal numbers          (5.8, -0.1)
#   str    -> text                     ("Alice")
#   bool   -> True / False
# There's also complex, NoneType, and the containers covered in
# later lessons (list, tuple, dict, set).

age = 20
name = "Alice"
height = 5.8
is_student = True

print(type(age))          # <class 'int'>
print(type(name))         # <class 'str'>
print(type(height))       # <class 'float'>
print(type(is_student))   # <class 'bool'>

# -------------------------------------------------------------
# bool is secretly a subclass of int!
# -------------------------------------------------------------
# True behaves like 1, False behaves like 0 in arithmetic.
print(True + True)     # 2   (1 + 1)
print(True + False)    # 1   (1 + 0)
print(False + False)   # 0   (0 + 0)
print(isinstance(True, int))   # True  -> proof bool subclasses int

# -------------------------------------------------------------
# EXTRA: other built-in types worth knowing early
# -------------------------------------------------------------
nothing = None
print(type(nothing))       # <class 'NoneType'> -> represents "no value"

complex_num = 2 + 3j
print(type(complex_num))   # <class 'complex'>  -> rarely needed day-to-day

# -------------------------------------------------------------
# EXTRA: type casting / conversion between types
# -------------------------------------------------------------
num_text = "42"
num = int(num_text)            # str -> int
print(num, type(num))          # 42 <class 'int'>

price_text = "19.99"
price = float(price_text)      # str -> float
print(price, type(price))      # 19.99 <class 'float'>

count = 7
count_text = str(count)        # int -> str (useful for concatenating with text)
print("Count: " + count_text)  # Count: 7

print(int(3.9))     # 3      -> float -> int TRUNCATES (does not round!)
print(round(3.9))   # 4      -> use round() if you want rounding

print(bool(0))       # False -> 0 is falsy
print(bool(1))       # True  -> any non-zero number is truthy
print(bool(""))      # False -> empty string is falsy
print(bool("hi"))    # True  -> non-empty string is truthy

# -------------------------------------------------------------
# EXTRA: checking types safely
# -------------------------------------------------------------
value = 10
if isinstance(value, int):        # preferred over type(value) == int
    print("value is an integer")
