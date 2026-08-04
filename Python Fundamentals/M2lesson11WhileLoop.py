# =============================================================
# LESSON 11: while loops
# =============================================================
# A `while` loop keeps repeating its body as long as its condition
# stays truthy. YOU are responsible for making the condition
# eventually become False -- forgetting to update it causes an
# infinite loop.

count = 1

while count <= 5:
    print(count)         # 1, 2, 3, 4, 5
    count = count + 1     # without this line, count never changes and
                            # the condition count <= 5 is ALWAYS True
                            # -> infinite loop that never stops!

# -------------------------------------------------------------
# Shorthand: += / -= etc. (augmented assignment operators)
# -------------------------------------------------------------
count = 1
while count <= 3:
    count += 1            # same as: count = count + 1
print("count is now:", count)   # 4

x = 10
x += 5     # same as x = x + 5
print(x)    # 15

count = 5
while count >= 1:
    count -= 1            # same as: count = count - 1
print("count is now:", count)   # 0

# -------------------------------------------------------------
# A while loop with a FALSY condition never runs at all
# -------------------------------------------------------------
x = 0
while x:                 # 0 is falsy, so this loop body is skipped entirely
    print("Hi")            # never printed
print("loop with falsy x was skipped")

# -------------------------------------------------------------
# EXTRA: `break` -- exit a loop immediately, ignoring the condition
# -------------------------------------------------------------
# `while True` creates a deliberately infinite loop; `break` is
# what actually stops it. This is the classic pattern for
# "keep asking until the user gets it right".
correct_password = "secret"     # NOTE: must be a STRING (quoted!),
                                  # otherwise Python treats it as a
                                  # variable name and raises a NameError
                                  # if that name was never defined.
attempts = 0

while True:
    password = input("Password: ")
    attempts += 1

    if password == correct_password:
        break                     # exits the while loop immediately

    print("Wrong password, try again.")

print(f"Welcome! (took {attempts} attempt(s))")

# -------------------------------------------------------------
# EXTRA: `continue` -- skip to the next iteration, without breaking out
# -------------------------------------------------------------
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue        # skips the print below ONLY when n == 3
    print("n =", n)      # prints 1, 2, 4, 5 (3 is skipped)
