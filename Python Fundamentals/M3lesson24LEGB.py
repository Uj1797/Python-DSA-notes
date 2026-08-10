# =============================================================
# LESSON 24: LEGB Rule -- Python's Variable Scope Resolution
# =============================================================
# Python looks for variables in a specific order: L→E→G→B
#   L = Local     -- inside the current function
#   E = Enclosing -- inside enclosing function(s) (closures)
#   G = Global    -- at the module/file level
#   B = Built-in  -- Python's built-in namespace (len, print, etc.)

# ---------------------------------------------------------
# 1. LOCAL scope
# ---------------------------------------------------------
def example_local():
    x = "LOCAL"      # x only exists inside this function
    print(x)

example_local()  # LOCAL
# print(x)       # NameError! x doesn't exist outside the function

# ---------------------------------------------------------
# 2. ENCLOSING scope (closures)
# ---------------------------------------------------------
def outer():
    x = "ENCLOSING"    # x in the enclosing function

    def inner():
        print(x)       # inner() can access outer's x

    inner()

outer()  # ENCLOSING

# ---------------------------------------------------------
# 3. GLOBAL scope
# ---------------------------------------------------------
x = "GLOBAL"           # x at the module level

def example_global():
    print(x)           # this function can read global x

example_global()  # GLOBAL

# ---------------------------------------------------------
# 4. BUILT-IN scope
# ---------------------------------------------------------
# Python's built-in functions are always available
print(len("hello"))     # len() is built-in (returns 5)
print(max([1, 5, 3]))   # max() is built-in (returns 5)

# ---------------------------------------------------------
# LEGB in action: the lookup order
# ---------------------------------------------------------
# When Python encounters a variable name, it searches in this order:
# 1. LOCAL   (current function scope)
# 2. ENCLOSING (outer function scopes, working outward)
# 3. GLOBAL  (module-level scope)
# 4. BUILT-IN (Python's built-ins)

x = "GLOBAL"

def outer():
    x = "ENCLOSING"

    def inner():
        x = "LOCAL"        # defines x in LOCAL scope
        print(x)           # prints LOCAL

    inner()
    print(x)               # prints ENCLOSING (didn't touch it)

outer()
print(x)                   # prints GLOBAL (unchanged)
# Output: LOCAL, ENCLOSING, GLOBAL

# ---------------------------------------------------------
# IMPORTANT: modifying global variables with `global`
# ---------------------------------------------------------
count = 0

def increment_global():
    global count       # declare that we're modifying the global count
    count += 1         # modifies the GLOBAL count, not a local one

increment_global()
increment_global()
print(count)           # 2 (global variable was modified)

# Without `global`, Python assumes count is local:
def increment_local():
    # count += 1       # UnboundLocalError! count is treated as local
                        # but was never assigned in LOCAL scope first
    pass

# ---------------------------------------------------------
# IMPORTANT: modifying enclosing variables with `nonlocal`
# ---------------------------------------------------------
def outer_counter():
    count = 0

    def increment():
        nonlocal count  # declare that we're modifying the ENCLOSING count
        count += 1
        return count

    return increment

counter = outer_counter()
print(counter())        # 1
print(counter())        # 2
print(counter())        # 3
# nonlocal let the inner function modify the closure variable

# ---------------------------------------------------------
# Real-world example: request counter middleware
# ---------------------------------------------------------
def create_request_middleware():
    """A closure that maintains request count state."""
    request_count = 0

    def middleware(request):
        nonlocal request_count
        request_count += 1
        print(f"Request #{request_count}: {request}")
        return request_count

    return middleware

api = create_request_middleware()
api("GET /home")         # Request #1: GET /home
api("POST /login")       # Request #2: POST /login
api("GET /dashboard")    # Request #3: GET /dashboard

# ---------------------------------------------------------
# Shadowing: redefining a variable at a closer scope
# ---------------------------------------------------------
x = "GLOBAL"

def show_shadowing():
    x = "LOCAL"           # shadows (hides) the global x
    print(x)              # prints LOCAL, not GLOBAL

show_shadowing()          # LOCAL
print(x)                  # GLOBAL (unchanged, not affected by function)

# ---------------------------------------------------------
# RULE OF THUMB:
#   - Python searches for variables in order: Local → Enclosing → Global → Built-in
#   - Use `global` to modify a global variable from inside a function
#   - Use `nonlocal` to modify an enclosing (closure) variable
#   - Avoid excessive use of global; prefer passing variables as arguments
#   - Each scope shadows (hides) outer scopes with the same variable name
# ---------------------------------------------------------
