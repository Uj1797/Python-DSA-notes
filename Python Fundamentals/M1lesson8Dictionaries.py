# =============================================================
# LESSON 8: Dictionaries -- key-value pairs
# =============================================================
# A dict stores data as KEY: VALUE pairs. Keys must be unique and
# hashable (strings, numbers, tuples of hashables). Values can be
# anything. Dicts are mutable, like lists, and preserve insertion
# order (guaranteed since Python 3.7+).

user = {
    "name": "Kindled",
    "age": 24,
    "country": "India"
}

print(user["country"])   # India -> access a value by its key

user["Job"] = "Engineer"      # adding a NEW key creates a new entry
print(user["Job"])             # Engineer

user["age"] = 25               # assigning to an EXISTING key updates it
print(user["age"])             # 25

print(user)   # {'name': 'Kindled', 'age': 25, 'country': 'India', 'Job': 'Engineer'}

# -------------------------------------------------------------
# EXTRA: safe access with .get() -- avoids crashing on missing keys
# -------------------------------------------------------------
print(user["salary"] if "salary" in user else None)   # works, but clunky

print(user.get("salary"))            # None   -> no KeyError, just returns None
print(user.get("salary", 0))         # 0      -> custom default if key is missing
# print(user["salary"])              # KeyError! Accessing a missing key with [] crashes.

# -------------------------------------------------------------
# EXTRA: checking existence, deleting keys
# -------------------------------------------------------------
print("name" in user)        # True   -> `in` checks KEYS by default
print("Kindled" in user)     # False  -> not a key, it's a value

del user["Job"]               # removes the "Job" key entirely
print(user)                    # {'name': 'Kindled', 'age': 25, 'country': 'India'}

removed_value = user.pop("age")   # removes "age" AND returns its value
print(removed_value)               # 25
print(user)                         # {'name': 'Kindled', 'country': 'India'}

# -------------------------------------------------------------
# EXTRA: iterating over a dictionary
# -------------------------------------------------------------
user["age"] = 25   # add it back for the examples below

for key in user:                 # default iteration is over KEYS
    print(key)

for key, value in user.items():  # .items() gives (key, value) pairs -- most common pattern
    print(key, "->", value)

for value in user.values():      # iterate over VALUES only
    print(value)

print(list(user.keys()))     # ['name', 'country', 'age'] -> as an actual list
print(list(user.values()))   # ['Kindled', 'India', 25]

# -------------------------------------------------------------
# EXTRA: aliasing works the same way as lists (dicts are mutable!)
# -------------------------------------------------------------
a = {"x": 1}
b = a              # b points to the SAME dict object
b["x"] = 99
print(a)            # {'x': 99} -> a is affected too, since a and b are the same object

# To avoid this, copy explicitly:
c = a.copy()
c["x"] = 1
print(a)            # {'x': 99} -> untouched
print(c)            # {'x': 1}  -> independent copy

# -------------------------------------------------------------
# EXTRA: nested dictionaries (very common with real-world/JSON data)
# -------------------------------------------------------------
profile = {
    "name": "Kindled",
    "address": {
        "city": "Bangalore",
        "pincode": "560001"
    }
}
print(profile["address"]["city"])   # Bangalore -> chain the keys to go deeper

# -------------------------------------------------------------
# EXTRA: dict comprehension -- compact way to build a dict
# -------------------------------------------------------------
squares = {n: n * n for n in range(1, 5)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16}
