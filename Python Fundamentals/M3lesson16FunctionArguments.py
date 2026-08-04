# =============================================================
# LESSON 16: How arguments are actually passed to functions
# =============================================================
# Python uses "pass by object reference" (sometimes called
# "pass by assignment"). The parameter name inside the function
# becomes ANOTHER name pointing at the SAME object the caller
# passed in -- exactly like a normal `=` assignment.
#
# What happens next depends on whether the object is MUTABLE
# (list, dict, set) or IMMUTABLE (int, str, float, tuple):
#   - MUTATING the object in place (append, item assignment, etc.)
#     is visible to the caller, because both names point to the
#     same object.
#   - REASSIGNING the parameter to a new object only affects the
#     local name -- the caller's variable is untouched.

def change(x):
    x = 100          # REASSIGNS the local name x to a new int object

a = 10
change(a)
print(a)   # 10 -> unaffected

# because `a` is an int (immutable), and `change` only reassigns
# its local parameter `x` to point at a new object (100). The
# caller's variable `a` still points at the original int, 10.

def change(lst):
    lst.append(100)     # MUTATES the list object in place

numbers = [10, 20]
change(numbers)
print(numbers)   # [10, 20, 100] -> changed!

# because `numbers` is a list (mutable), and inside `change`, `lst`
# is just another name for that SAME list object. `.append()`
# mutates the shared object directly, so the caller sees the change.

def change(lst):
    lst = [100]          # REASSIGNS the local name lst to a brand-new list

numbers = [1, 2]
change(numbers)
print(numbers)   # [1, 2] -> unaffected

# because although `lst` starts out pointing at the same list as
# `numbers`, the line `lst = [100]` makes `lst` point at a DIFFERENT,
# brand-new list object. It doesn't touch the original list that
# `numbers` still refers to.

def add(text):
    text += "!"           # for strings, += creates a NEW string (strings
                            # are immutable, they can't be changed in place)

word = "Hello"
add(word)
print(word)   # Hello -> unaffected

# because `word` is a string (immutable). Inside add(), `text += "!"`
# is really `text = text + "!"`, which reassigns the LOCAL name
# `text` to a new string object. The caller's `word` never changes.

def add(items):
    items += [4]           # for LISTS, += mutates in place (it's shorthand
                             # for items.extend([4]), unlike string +=!)

numbers = [1, 2, 3]
add(numbers)
print(numbers)   # [1, 2, 3, 4] -> changed!

# because `numbers` is a list (mutable), and += on a list calls the
# in-place .extend() method rather than building a new object. So
# the shared object is modified, and the caller sees the update too.

# =================================================================
# SUMMARY TABLE
# =================================================================
# Argument type      | Action inside function      | Caller affected?
# -------------------|------------------------------|------------------
# int / str / tuple   | reassign (=, +=)             | No  (immutable)
# list / dict / set    | mutate in place (append,     | Yes (mutable)
#                       item assignment, +=, etc.)   |
# list / dict / set    | reassign (= new object)       | No  (rebinding
#                       to a whole new value)         |      the local name)

# =================================================================
# EXTRA: *args and **kwargs -- accepting a variable number of arguments
# =================================================================
def total(*numbers):            # *numbers collects any number of positional
    print(numbers)                 # args into a TUPLE
    return sum(numbers)

print(total(1, 2, 3))       # (1, 2, 3) then 6
print(total(1, 2, 3, 4))    # (1, 2, 3, 4) then 10

def show_info(**details):        # **details collects any number of keyword
    print(details)                  # args into a DICT
    for key, value in details.items():
        print(key, "->", value)

show_info(name="Alice", age=30)   # {'name': 'Alice', 'age': 30}

# EXTRA: combining regular params, *args, and **kwargs together
def build_profile(name, *hobbies, **extra_info):
    print("Name:", name)
    print("Hobbies:", hobbies)
    print("Extra info:", extra_info)

build_profile("Bob", "chess", "reading", city="Delhi", age=28)
# Name: Bob
# Hobbies: ('chess', 'reading')
# Extra info: {'city': 'Delhi', 'age': 28}
