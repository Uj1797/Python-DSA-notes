# =============================================================
# LESSON 17: Recursion -- a function that calls itself
# =============================================================
# Recursion needs exactly two parts:
#   1. BASE CASE  -- a condition where the function stops calling
#      itself and just returns a value directly. Without this,
#      the function calls itself forever (until Python's call
#      stack runs out -> RecursionError).
#   2. RECURSIVE CASE -- the function calls itself with a "smaller"
#      or "closer to the base case" version of the problem, so it
#      eventually reaches the base case.

# -------------------------------------------------------------
# WRONG: no base case at all -> infinite recursion
# -------------------------------------------------------------
def countdown_broken(n):
    print(n)
    countdown_broken(n - 1)     # n keeps decreasing forever: 5, 4, 3, 2, 1,
                                  # 0, -1, -2, ... nothing ever stops it.

# We do NOT call countdown_broken() here, because it would eventually
# raise a RecursionError ("maximum recursion depth exceeded") once
# Python's call stack fills up. Try it yourself if you want to see
# the crash:
#
#   countdown_broken(5)

# -------------------------------------------------------------
# CORRECT: a base case stops the recursion when n reaches 0
# -------------------------------------------------------------
def countdown(n):
    if n == 0:          # BASE CASE
        return            # stop recursing, don't print anything more

    print(n)              # RECURSIVE CASE's work
    countdown(n - 1)        # RECURSIVE CASE's call, moving toward the base case

countdown(5)
# Output: 5 4 3 2 1  (each on its own line)

# -------------------------------------------------------------
# WRONG (again): a function with zero base case is ALWAYS a bug
# -------------------------------------------------------------
def hello_broken():
    print("hello")
    hello_broken()         # never stops -> RecursionError if called

# Not calling hello_broken() for the same reason as above -- it's
# here purely to show what "no base case" looks like in its
# simplest possible form.

# =================================================================
# TRACING EXECUTION: understanding the CALL STACK
# =================================================================
# Every recursive call is "paused" and pushed onto the call stack
# until the calls below it finish. Code written BEFORE the
# recursive call runs on the way DOWN (as calls stack up); code
# written AFTER the recursive call runs on the way UP (as calls
# return, "unwinding" the stack).

def mystery(n):
    if n == 0:
        return

    print("Start", n)     # runs on the way DOWN
    mystery(n - 1)
    print("End", n)        # runs on the way UP (after the deeper call returns)

mystery(3)
# Output:
# Start 3
# Start 2
# Start 1
# End 1
# End 2
# End 3
#
# Trace it step by step:
#   mystery(3) prints "Start 3", calls mystery(2)
#     mystery(2) prints "Start 2", calls mystery(1)
#       mystery(1) prints "Start 1", calls mystery(0)
#         mystery(0) -> n == 0, returns immediately (base case)
#       mystery(1) resumes, prints "End 1"
#     mystery(2) resumes, prints "End 2"
#   mystery(3) resumes, prints "End 3"

# -------------------------------------------------------------
# EXTRA: what happens if you print AFTER the recursive call only?
# -------------------------------------------------------------
def test(n):
    if n == 0:
        return

    test(n - 1)       # recurse ALL the way down first...
    print(n)            # ...then print while unwinding back up

test(3)
# Output: 1 2 3   (printed in REVERSE of the call order!)
#
# WHY: the recursive calls happen first and go all the way down to
# the base case BEFORE any print() runs. Only once test(0) returns
# does test(1) resume and print 1, then test(2) resumes and prints
# 2, then test(3) resumes and prints 3. The numbers come out in
# reverse because printing happens on the way back UP the stack,
# not on the way down.

# =================================================================
# EXTRA: classic recursive patterns used constantly in DSA problems
# =================================================================

# --- 1. Factorial: n! = n * (n-1) * (n-2) * ... * 1 ---
def factorial(n):
    if n == 0:                     # BASE CASE: 0! is defined as 1
        return 1
    return n * factorial(n - 1)     # RECURSIVE CASE

print(factorial(5))   # 120  (5 * 4 * 3 * 2 * 1)

# --- 2. Sum of a list, recursively ---
def sum_list(nums):
    if not nums:                        # BASE CASE: empty list sums to 0
        return 0
    return nums[0] + sum_list(nums[1:])  # first item + sum of the rest

print(sum_list([1, 2, 3, 4, 5]))   # 15

# --- 3. Reversing a string, recursively ---
def reverse_str(s):
    if len(s) <= 1:                       # BASE CASE: 0 or 1 char is its own reverse
        return s
    return reverse_str(s[1:]) + s[0]        # reverse of the rest, then the first char

print(reverse_str("hello"))   # olleh

# --- 4. Fibonacci -- the naive (slow) version ---
# Each call branches into TWO more calls, so this recomputes the
# same values over and over (exponential time complexity, O(2^n)).
def fib(n):
    if n <= 1:              # BASE CASE: fib(0) = 0, fib(1) = 1
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(8)])   # [0, 1, 1, 2, 3, 5, 8, 13]

# --- 5. Fibonacci -- memoized (fast) version ---
# We cache results we've already computed so each value is only
# calculated once. This turns it from O(2^n) into O(n) time.
def fib_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:                     # already computed? reuse it
        return cache[n]
    if n <= 1:                          # BASE CASE
        return n
    result = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    cache[n] = result                    # store before returning
    return result

print([fib_memo(i) for i in range(10)])   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# --- 6. Greatest Common Divisor (Euclidean algorithm) ---
def gcd(a, b):
    if b == 0:              # BASE CASE
        return a
    return gcd(b, a % b)     # RECURSIVE CASE: shrinks toward the base case fast

print(gcd(48, 18))   # 6

# =================================================================
# EXTRA: recursion has a limit -- it's not free
# =================================================================
import sys

print(sys.getrecursionlimit())   # 1000 by default -- Python's cap on call depth

def blow_the_stack(n):
    return blow_the_stack(n + 1)   # no base case, grows forever

try:
    blow_the_stack(0)
except RecursionError as e:
    print("Got an error:", e)
    # Got an error: maximum recursion depth exceeded
    # This is exactly what countdown_broken()/hello_broken() above
    # would eventually do too, if we actually called them.

# -------------------------------------------------------------
# RULE OF THUMB:
#   - Every recursive function needs a base case that is
#     GUARANTEED to be reached.
#   - Each recursive call should move the input CLOSER to that
#     base case (smaller n, shorter list, etc.).
#   - Recursion is often more readable for naturally recursive
#     problems (trees, backtracking, divide-and-conquer), but a
#     plain loop is usually faster and uses less memory for
#     simple repetition -- use recursion where it makes the
#     problem clearer, not just because it's possible.
# -------------------------------------------------------------
