# =============================================================
# LESSON 5: Strings
# =============================================================
# Strings are ORDERED sequences of characters, and they are
# IMMUTABLE -- once created, a string's contents can never be
# changed in place. Every "modifying" string method actually
# returns a brand-new string.

name = "Kindled"

# -------------------------------------------------------------
# Indexing -- accessing a single character by position
# -------------------------------------------------------------
# Indexes start at 0. Negative indexes count from the end.
#   K  i  n  d  l  e  d
#   0  1  2  3  4  5  6
#  -7 -6 -5 -4 -3 -2 -1
print(name[0])     # K   -> first character
print(name[1])     # i   -> second character
print(name[-1])    # d   -> last character (shortcut instead of name[len(name)-1])

# -------------------------------------------------------------
# Slicing -- extracting a sub-string: name[start:stop]
# -------------------------------------------------------------
# `start` is inclusive, `stop` is EXCLUSIVE (stops right before it).
print(name[0:4])   # Kind   -> characters at index 0,1,2,3
print(name[-3:])   # led    -> from 3rd-last character to the end
print(name[:3])    # Kin    -> omitting start defaults to 0
print(name[::2])   # Kidd   -> step of 2: every other character
print(name[::-1])  # delnikK -> step of -1: reverses the whole string!

# -------------------------------------------------------------
# Useful built-in functions / methods
# -------------------------------------------------------------
print(len(name))              # 7           -> number of characters
print(name.upper())           # KINDLED     -> new string, all caps
print(name.lower())           # kindled     -> new string, all lowercase
print(name.replace("K", "M")) # Mindled     -> new string with replacement

# IMPORTANT: none of the above change `name` itself, because
# strings are immutable. `name` is still "Kindled" right now:
print(name)                   # Kindled

# -------------------------------------------------------------
# EXTRA: more string methods you'll use constantly
# -------------------------------------------------------------
messy = "   Hello World   "
print(messy.strip())              # "Hello World"      -> removes leading/trailing whitespace
print(messy.strip().split(" "))   # ['Hello', 'World'] -> splits into a list on the separator

words = ["Hello", "World"]
print(" ".join(words))            # "Hello World"      -> opposite of split: list -> string

sentence = "the quick brown fox"
print(sentence.find("quick"))     # 4     -> index where "quick" starts (-1 if not found)
print("quick" in sentence)        # True  -> membership check, often clearer than find()
print(sentence.startswith("the")) # True
print(sentence.endswith("fox"))   # True
print(sentence.title())           # "The Quick Brown Fox"
print(sentence.count("o"))        # 2     -> counts occurrences

# -------------------------------------------------------------
# EXTRA: string concatenation vs f-strings (formatted strings)
# -------------------------------------------------------------
age = 24
# Concatenation requires everything to be a string already:
print(name + " is " + str(age) + " years old")

# f-strings (prefix f before the quotes) let you embed expressions
# directly inside {} -- this is the modern, preferred way to build
# strings with variables in them.
print(f"{name} is {age} years old")
print(f"{name.upper()} is turning {age + 1} next year")

# -------------------------------------------------------------
# EXTRA: strings are immutable -- this would raise an error
# -------------------------------------------------------------
# name[0] = "M"   # TypeError: 'str' object does not support item assignment
# To "change" a character, you must build a new string instead:
name = "M" + name[1:]
print(name)   # Mindled
