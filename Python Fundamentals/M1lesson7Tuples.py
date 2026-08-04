# =============================================================
# LESSON 7: Tuples -- IMMUTABLE, ordered collections
# =============================================================
# A tuple looks like a list but uses () instead of [], and once
# created its CONTENTS can never be changed (no append, no item
# assignment). This immutability makes tuples useful for fixed
# collections of values, dictionary keys, and function returns.

point = (10, 20, 30, 40, 50)

print(point[0])      # 10        -> indexing works the same as lists
print(point[1:4])    # (20, 30, 40) -> slicing a tuple returns a tuple

# -------------------------------------------------------------
# Tuple unpacking -- assigning multiple variables at once
# -------------------------------------------------------------
x, y = (20, 30)      # x = 20, y = 30  (number of names must match tuple length)
print(x)              # 20
print(y)              # 30

# EXTRA: unpacking works with any iterable, and parentheses are optional
a1, b1, c1 = 1, 2, 3          # this IS a tuple under the hood: (1, 2, 3)
print(a1, b1, c1)              # 1 2 3

# EXTRA: swapping two variables in one line, thanks to tuple packing/unpacking
p, q = 5, 10
p, q = q, p            # packs (q, p) into a tuple, then unpacks into p, q
print(p, q)             # 10 5

# -------------------------------------------------------------
# Immutability + aliasing: same rules as lists for the VARIABLE,
# but you can never mutate the tuple's contents in place.
# -------------------------------------------------------------
a = (1, 2)
b = a               # b aliases the same tuple object as a

a = (10, 20)        # this REBINDS a to a brand-new tuple object.
                     # It does not and cannot modify the old (1, 2),
                     # because tuples don't support in-place changes anyway.

print(a)   # (10, 20)  -> a's new tuple
print(b)   # (1, 2)    -> b still points to the original, untouched

# -------------------------------------------------------------
# EXTRA: tuples truly cannot be mutated (unlike lists)
# -------------------------------------------------------------
# a[0] = 99   # TypeError: 'tuple' object does not support item assignment

# -------------------------------------------------------------
# EXTRA: single-element tuple needs a trailing comma!
# -------------------------------------------------------------
not_a_tuple = (5)        # this is just the int 5 in parentheses
actual_tuple = (5,)      # the comma is what makes it a tuple
print(type(not_a_tuple))    # <class 'int'>
print(type(actual_tuple))   # <class 'tuple'>

# -------------------------------------------------------------
# EXTRA: tuple vs list -- when to use which
# -------------------------------------------------------------
# - Use a LIST when the collection may grow/shrink/change over time.
# - Use a TUPLE for a fixed, "read-only" group of values, e.g.
#   coordinates, RGB colors, or returning multiple values from a
#   function (see M2lesson14Return.py).

def get_coordinates():
    return (12.9, 77.6)     # returning a tuple of (lat, lng)

lat, lng = get_coordinates()
print(lat, lng)   # 12.9 77.6

# EXTRA: tuples are also "hashable" (if their contents are), so
# they CAN be used as dictionary keys -- lists cannot.
locations = {
    (12.9, 77.6): "Bangalore",
    (28.6, 77.2): "Delhi"
}
print(locations[(12.9, 77.6)])   # Bangalore
