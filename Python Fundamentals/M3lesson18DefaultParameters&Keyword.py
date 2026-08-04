# =============================================================
# LESSON 18: Default Parameters & Keyword Arguments
# =============================================================
# A DEFAULT PARAMETER lets you skip an argument when calling a
# function -- Python fills in a pre-set value automatically.

def greet(name="World"):
    print("Hello", name)

greet()          # Output: Hello World   -> no argument given, uses the default
greet("Alice")   # Output: Hello Alice   -> argument given, overrides the default

# -------------------------------------------------------------
# Multiple parameters: required ones can be mixed with defaults
# -------------------------------------------------------------
def add(a, b=10):
    return a + b

print(add(5))        # 15  -> b uses its default (10), so this is 5 + 10
print(add(5, 20))     # 25  -> b is overridden to 20, so this is 5 + 20

# IMPORTANT RULE: parameters WITHOUT a default must come BEFORE
# parameters WITH a default in the function signature.
#   def add(a, b=10):       OK
#   def add(a=10, b):       SyntaxError! non-default after default

# -------------------------------------------------------------
# KEYWORD ARGUMENTS: passing arguments by NAME instead of position
# -------------------------------------------------------------
def order(
    item,
    quantity=1,
    delivery="Standard"
):
    print(item)
    print(quantity)
    print(delivery)

order("Laptop")
# Laptop
# 1            <- default quantity
# Standard     <- default delivery

print("---")

order(
    "Phone",
    delivery="Express"      # named explicitly -> skips straight past `quantity`,
                              # which falls back to its default (1)
)
# Phone
# 1
# Express

print("---")

order(
    "Keyboard",
    3,               # positional -> fills `quantity`
    "Express"         # positional -> fills `delivery`
)
# Keyboard
# 3
# Express

# -------------------------------------------------------------
# EXTRA: mixing positional and keyword arguments in ONE call
# -------------------------------------------------------------
# Rule: positional arguments must always come BEFORE keyword
# arguments in a function call.
order("Mouse", delivery="Express", quantity=2)
# Mouse
# 2
# Express
# -> keyword args can be given in ANY order relative to each other,
#    since they're matched by name, not position.

# order(quantity=2, "Mouse")   # SyntaxError! positional after keyword

# -------------------------------------------------------------
# EXTRA: why keyword arguments make calls more readable
# -------------------------------------------------------------
def create_user(name, age, is_admin=False, is_active=True):
    print(f"{name}, {age}, admin={is_admin}, active={is_active}")

# Compare these two equivalent calls:
create_user("Sam", 30, True, False)                         # what do True/False mean here?? unclear
create_user("Sam", 30, is_admin=True, is_active=False)       # self-documenting, much clearer

# =================================================================
# EXTRA (IMPORTANT GOTCHA): never use a MUTABLE default argument
# =================================================================
# A default value is created ONCE, when the function is DEFINED --
# not fresh on every call! If that default is a mutable object
# (like a list or dict), every call that relies on the default
# shares and mutates the SAME object.

def add_item_broken(item, cart=[]):     # DANGER: mutable default!
    cart.append(item)
    return cart

print(add_item_broken("apple"))    # ['apple']
print(add_item_broken("banana"))   # ['apple', 'banana']  <- unexpected!
                                      # the SAME list from the first call
                                      # was reused and mutated again.

# FIX: use `None` as the default, and create a new mutable object
# INSIDE the function body if none was provided.
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []          # a brand-new list, created fresh on THIS call
    cart.append(item)
    return cart

print(add_item_fixed("apple"))    # ['apple']
print(add_item_fixed("banana"))   # ['banana']  <- correct, independent call
print(add_item_fixed("cherry", ["existing"]))   # ['existing', 'cherry']

# -------------------------------------------------------------
# EXTRA: forcing keyword-only arguments with `*`
# -------------------------------------------------------------
# Anything listed AFTER a bare `*` in the parameter list can ONLY
# be passed by keyword -- never positionally. Useful for options
# that would be confusing or risky to pass by position.
def divide(a, b, *, precision=2):
    return round(a / b, precision)

print(divide(10, 3))                    # 3.33  -> a, b positional; precision defaults
print(divide(10, 3, precision=4))       # 3.3333 -> precision MUST be named
# divide(10, 3, 4)                      # TypeError! precision can't be positional

# -------------------------------------------------------------
# EXTRA: forcing positional-only arguments with `/`
# -------------------------------------------------------------
# Anything listed BEFORE a bare `/` can ONLY be passed positionally
# -- never by keyword. Useful when the parameter name isn't
# meaningful to the caller or you want the freedom to rename it
# later without breaking anyone's code.
def power(base, /, exponent=2):
    return base ** exponent

print(power(3))                  # 9   -> base passed positionally (required)
print(power(3, exponent=3))       # 27  -> exponent passed by keyword
# power(base=3)                   # TypeError! base can't be passed by keyword

# -------------------------------------------------------------
# RULE OF THUMB:
#   - Give a parameter a default when it has a sensible "usual"
#     value most callers won't need to change.
#   - Prefer calling with keyword arguments for booleans/flags or
#     when a call has many arguments -- it documents intent at
#     the call site.
#   - NEVER default a parameter to a mutable object ([], {}, set())
#     -- default to None and create the mutable object inside the
#     function body instead.
# -------------------------------------------------------------
