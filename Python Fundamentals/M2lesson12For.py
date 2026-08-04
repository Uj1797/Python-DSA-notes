# =============================================================
# LESSON 12: for loops
# =============================================================
# A `for` loop iterates directly over the items of a sequence
# (list, string, tuple, dict, range, etc.) -- no manual counter
# or condition needed like `while` requires.

numbers = [10, 20]

for n in numbers:
    print(n)          # 10, then 20

# -------------------------------------------------------------
# IMPORTANT: the loop variable still exists AFTER the loop ends,
# holding whatever value it had on the LAST iteration.
# -------------------------------------------------------------
print(n)   # 20 -> `n` "leaks" out of the loop body; this is normal
            # in Python (unlike some other languages where the loop
            # variable would be scoped only to the loop).

# -------------------------------------------------------------
# IMPORTANT: reassigning the loop variable does NOT change the
# original list, because integers are IMMUTABLE.
# -------------------------------------------------------------
numbers = [1, 2, 3]

for number in numbers:
    number = 100        # this only rebinds the LOCAL name `number` to
                          # point at a new int object (100). It has no
                          # effect on the list itself.

print(numbers)   # [1, 2, 3] -> unchanged!

# -------------------------------------------------------------
# BUT: if the items themselves are MUTABLE (like lists), calling a
# mutating method on them DOES affect the original data, because
# `item` is a reference to the actual sub-list object, not a copy.
# -------------------------------------------------------------
numbers = [[1], [2], [3]]

for item in numbers:
    item.append(100)     # mutates the actual list object in place

print(numbers)   # [[1, 100], [2, 100], [3, 100]] -> changed!

# -------------------------------------------------------------
# EXTRA: range() -- generate a sequence of numbers to loop over
# -------------------------------------------------------------
for i in range(5):           # 0, 1, 2, 3, 4  (stop is exclusive, like slicing)
    print(i)

for i in range(2, 6):        # 2, 3, 4, 5     (start inclusive, stop exclusive)
    print(i)

for i in range(0, 10, 2):    # 0, 2, 4, 6, 8  (step of 2)
    print(i)

# -------------------------------------------------------------
# EXTRA: enumerate() -- get both the index AND the value while looping
# -------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)     # 0 apple / 1 banana / 2 cherry

# -------------------------------------------------------------
# EXTRA: break / continue work in for loops exactly like while loops
# -------------------------------------------------------------
for i in range(10):
    if i == 3:
        continue        # skip printing 3
    if i == 6:
        break             # stop the loop entirely once i reaches 6
    print(i)              # prints 0, 1, 2, 4, 5

# -------------------------------------------------------------
# EXTRA: looping over a dictionary and a string
# -------------------------------------------------------------
user = {"name": "Alice", "age": 30}
for key, value in user.items():
    print(key, "->", value)

for letter in "abc":
    print(letter)          # a, b, c
