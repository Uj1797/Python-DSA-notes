# =============================================================
# LESSON 9: Sets -- unordered collections of UNIQUE items
# =============================================================
# A set automatically removes duplicates and has no fixed order
# (you cannot index into a set with set[0]). Sets are mutable and
# very fast for membership testing (`in`) and mathematical set
# operations like union/intersection.

numbers = {10, 20}

numbers.add(30)         # adds a new item -> {10, 20, 30}
print(numbers)           # order is not guaranteed to match insertion order

numbers = {1, 2, 3}

print(2 in numbers)     # True  -> membership check, very fast (O(1) average)
print(5 in numbers)     # False

# -------------------------------------------------------------
# EXTRA: duplicates are automatically dropped
# -------------------------------------------------------------
with_dupes = {1, 2, 2, 3, 3, 3}
print(with_dupes)          # {1, 2, 3} -> duplicates silently removed

# A classic trick: dedupe a list by round-tripping through a set
raw_list = [1, 2, 2, 3, 3, 3, 4]
unique_list = list(set(raw_list))
print(unique_list)   # [1, 2, 3, 4] (order is not guaranteed to be preserved!)

# -------------------------------------------------------------
# EXTRA: removing items
# -------------------------------------------------------------
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")     # removes "banana"; raises KeyError if it's missing
print(fruits)                 # {'apple', 'cherry'}

fruits.discard("mango")      # removes if present, does NOT error if missing
print(fruits)                  # {'apple', 'cherry'}  -> no crash, safer than remove()

# -------------------------------------------------------------
# EXTRA: sets have no order or index
# -------------------------------------------------------------
# print(fruits[0])   # TypeError: 'set' object is not subscriptable

# -------------------------------------------------------------
# EXTRA: mathematical set operations
# -------------------------------------------------------------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # union            -> {1, 2, 3, 4, 5, 6}   (everything from both)
print(a & b)   # intersection     -> {3, 4}               (in both)
print(a - b)   # difference       -> {1, 2}               (in a, not in b)
print(b - a)   # difference       -> {5, 6}               (in b, not in a)
print(a ^ b)   # symmetric diff   -> {1, 2, 5, 6}          (in one but not both)

# same operations, using method names instead of operators:
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# -------------------------------------------------------------
# EXTRA: when to use a set vs a list
# -------------------------------------------------------------
# - Use a LIST when order matters or duplicates are allowed.
# - Use a SET when you only care about uniqueness / fast lookups
#   and don't need to preserve order or store duplicates.
