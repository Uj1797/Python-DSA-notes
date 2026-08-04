# =============================================================
# LESSON 6: Lists -- MUTABLE, ordered collections
# =============================================================
# Unlike strings, lists CAN be changed in place after creation.
# This is the source of a very common bug: two variables can
# accidentally point to the SAME list (aliasing), so changing
# one appears to change the other too.

products = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

print(products[1])   # Mouse -> indexing works just like strings

products.append("IPAD")     # adds one item to the END of the list, in place
print(products)              # ['Laptop', 'Mouse', 'Keyboard', 'IPAD']

# -------------------------------------------------------------
# ALIASING: y = products does NOT copy the list
# -------------------------------------------------------------
y = products          # y now points to the SAME list object as products
print(y)               # ['Laptop', 'Mouse', 'Keyboard', 'IPAD']

products.append("IPhone")     # mutating products in place...
print(y)                       # ...also shows up in y! Same object, two names.
print(products is y)           # True -> confirms they're the same object

print(dir(products))   # lists every method/attribute available on a list
                        # (append, remove, sort, pop, insert, etc.)

# -------------------------------------------------------------
# Comparing id() to prove aliasing vs independent objects
# -------------------------------------------------------------
a = [10, 20]
b = a                   # b is an alias of a (same list object)

print(id(a))
print(id(b))            # identical to id(a)

print(id(a[0]))         # id of the element itself (the int 10)

# -------------------------------------------------------------
# REASSIGNING a variable is different from MUTATING its object
# -------------------------------------------------------------
a = [1, 2]
b = a                   # b aliases this [1, 2] list

a = [10, 20]            # this makes `a` point to a BRAND NEW list.
                         # It does NOT touch the old [1, 2] list that
                         # b still points to.

print(a)   # [10, 20]   -> a's new list
print(b)   # [1, 2]     -> b still holds the original list, unaffected

# -------------------------------------------------------------
# `+` on a list creates a NEW list; it doesn't mutate in place
# -------------------------------------------------------------
a = [1, 2]
b = a                   # alias again

a = a + [3]             # a + [3] BUILDS a new list [1, 2, 3] and
                         # rebinds `a` to it. The original [1, 2] list
                         # (still referenced by b) is untouched.

print(a)   # [1, 2, 3]
print(b)   # [1, 2]     -> unaffected, proving `+` doesn't mutate

# Contrast with `.append()` or `+=`, which DO mutate in place:
c = [1, 2]
d = c
c += [3]        # += on a list calls extend() internally -> mutates in place
print(c)         # [1, 2, 3]
print(d)         # [1, 2, 3] -> d is affected too, because c was mutated,
                  # not reassigned to a new object!

# -------------------------------------------------------------
# EXTRA: common list operations you'll use all the time
# -------------------------------------------------------------
nums = [5, 3, 8, 1]

nums.insert(0, 99)      # insert 99 at index 0 -> [99, 5, 3, 8, 1]
print(nums)

nums.remove(99)          # removes the FIRST matching value -> [5, 3, 8, 1]
print(nums)

popped = nums.pop()      # removes & returns the LAST item -> 1
print(popped, nums)      # 1 [5, 3, 8]

nums.sort()               # sorts in place, ascending -> [3, 5, 8]
print(nums)

nums.sort(reverse=True)   # descending -> [8, 5, 3]
print(nums)

print(len(nums))          # 3     -> number of items
print(3 in nums)          # True  -> membership check

# -------------------------------------------------------------
# EXTRA: how to actually COPY a list (avoid accidental aliasing)
# -------------------------------------------------------------
original = [1, 2, 3]
safe_copy = original.copy()      # or: list(original) / original[:]
safe_copy.append(4)
print(original)    # [1, 2, 3]      -> untouched
print(safe_copy)   # [1, 2, 3, 4]   -> independent list

# -------------------------------------------------------------
# EXTRA: list comprehension -- a compact way to build lists
# -------------------------------------------------------------
squares = [n * n for n in range(1, 6)]     # [1, 4, 9, 16, 25]
print(squares)

evens_only = [n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]
print(evens_only)
