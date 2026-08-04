# =============================================================
# LESSON 10: Conditions -- if / elif / else and truthy/falsy values
# =============================================================
print("Wake up")

is_raining = False

if is_raining:
    print("Take umbrella")   # skipped, because is_raining is False

print("Go to office")   # always runs -> it's outside the if block

age = 20

if age >= 18:
    print("Adult")     # runs, because 20 >= 18 is True

# -------------------------------------------------------------
# TRUTHY / FALSY: Python doesn't require a bool in `if` --
# it converts (almost) any value to True/False automatically.
# -------------------------------------------------------------
# Falsy values: 0, 0.0, "", [], {}, (), set(), None, False
# Everything else is truthy.

x = 10

if x:                    # 10 is truthy (any non-zero number is)
    print("Hello")         # runs

if 0:                    # 0 is falsy
    print("A")
else:
    print("B")             # runs

if "":                   # empty string is falsy
    print("Hello")
else:
    print("Empty")          # runs

if [1, 2]:                # non-empty list is truthy
    print("List")            # runs
else:
    print("Nothing")

if None:                  # None is always falsy
    print("Yes")
else:
    print("No")             # runs

# -------------------------------------------------------------
# EXTRA: elif -- checking multiple conditions in sequence
# -------------------------------------------------------------
score = 75

if score >= 90:
    grade = "A"
elif score >= 75:          # only checked if the first condition was False
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"

print(grade)   # B -> stops at the FIRST matching condition, skips the rest

# -------------------------------------------------------------
# EXTRA: comparison operators
# -------------------------------------------------------------
print(5 == 5)    # True   -> equal to
print(5 != 4)    # True   -> not equal to
print(5 > 3)     # True   -> greater than
print(5 < 3)     # False  -> less than
print(5 >= 5)    # True   -> greater than or equal to
print(5 <= 4)    # False  -> less than or equal to

# -------------------------------------------------------------
# EXTRA: logical operators -- and / or / not
# -------------------------------------------------------------
temperature = 30
is_sunny = True

if temperature > 25 and is_sunny:    # BOTH must be True
    print("Great beach day")          # runs

if temperature > 40 or is_sunny:     # AT LEAST ONE must be True
    print("Still pretty nice")         # runs, because is_sunny is True

if not is_raining:                    # flips True/False
    print("No umbrella needed")         # runs, because is_raining is False

# -------------------------------------------------------------
# EXTRA: chained comparisons (a very handy Python-only feature)
# -------------------------------------------------------------
age2 = 25
if 18 <= age2 < 65:      # equivalent to: 18 <= age2 and age2 < 65
    print("Working age")   # runs

# -------------------------------------------------------------
# EXTRA: ternary (conditional) expression -- an if/else in one line
# -------------------------------------------------------------
status = "Adult" if age >= 18 else "Minor"
print(status)   # Adult
