# =============================================================
# LESSON 15: Scope -- local vs global variables
# =============================================================
# SCOPE = "where in the code a variable name is visible/usable."
#
# Python looks up a name in this order (this is called
# SCOPE RESOLUTION, sometimes remembered as the "LEGB" rule):
#   Local    (inside the current function)
#         |
#         v
#   Enclosing (an outer function, if this one is nested)
#         |
#         v
#   Global   (top-level of the module/file)
#         |
#         v
#   Built-in (Python's own names, like print, len, etc.)
#
# Python stops at the FIRST place it finds the name.

# -------------------------------------------------------------
# A local variable "shadows" (hides) a global one of the same name
# -------------------------------------------------------------
user = "Kindled"     # this is a GLOBAL variable

def login():
    user = "Alice"    # this creates a NEW, separate LOCAL variable
                        # named `user`, which only exists inside login().
                        # It does NOT touch the global `user` at all.
    print(user)          # Alice -> found locally, search stops there

login()
print(user)   # Kindled -> the global variable was never modified

# =================================================================
# THE CLASSIC GOTCHA: UnboundLocalError
# =================================================================
# Python decides whether a name is local or global by scanning the
# WHOLE function body BEFORE running it. If a name is assigned to
# ANYWHERE inside the function, Python treats it as LOCAL for the
# ENTIRE function -- even on lines BEFORE that assignment happens!

x = 10

def test_broken():
    print(x)     # you might expect this to print the global x (10)...
    x = 20        # ...but because x is assigned here, Python has already
                   # decided x is LOCAL to this whole function. So the
                   # print(x) above tries to read a local x that doesn't
                   # have a value YET -> crash.

try:
    test_broken()
except UnboundLocalError as e:
    print("Got an error:", e)
    # Got an error: cannot access local variable 'x' where it is
    # not associated with a value

print(x)   # 10 -> the global x was never touched; the function crashed
            # before it could even try to reassign it.

# -------------------------------------------------------------
# FIX 1: use a different local variable name (avoid the clash)
# -------------------------------------------------------------
def test_fixed_v1():
    print(x)        # now this unambiguously refers to the GLOBAL x
    local_x = 20      # a genuinely new local variable, no conflict
    print(local_x)

test_fixed_v1()   # prints 10, then 20
print(x)            # still 10 -> global untouched, as expected

# -------------------------------------------------------------
# FIX 2: use the `global` keyword to explicitly modify the global
# -------------------------------------------------------------
def test_fixed_v2():
    global x          # tells Python: "x inside this function IS the
                        # global x, don't make a local one"
    print(x)            # 10 -> reads the global value, no error now
    x = 20               # this REASSIGNS the actual global x

test_fixed_v2()
print(x)   # 20 -> the global was genuinely changed this time

# -------------------------------------------------------------
# RULE OF THUMB:
#   - Reading a global inside a function: just works, no keyword needed.
#   - Reassigning a global inside a function: requires `global`,
#     otherwise Python silently creates a local variable instead
#     (or crashes, if you also try to read it first).
#   - In general, prefer passing values in as parameters and
#     getting results out via `return` instead of relying on
#     `global` -- it keeps functions predictable and easier to test.
# -------------------------------------------------------------
