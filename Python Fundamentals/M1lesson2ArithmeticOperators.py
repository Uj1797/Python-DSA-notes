# =============================================================
# LESSON 2: Arithmetic Operators & Basic Operations
# =============================================================
# Python can do math! You can perform calculations using
# arithmetic operators on numbers.

# ---------------------------------------------------------
# Basic arithmetic operators
# ---------------------------------------------------------
# Addition: +
a = 10
b = 3
print(a + b)     # 13

# Subtraction: -
print(a - b)     # 7

# Multiplication: *
print(a * b)     # 30

# Division: / (always returns a float, even if dividing evenly)
print(a / b)     # 3.333...
print(10 / 2)    # 5.0 (not 5, but 5.0)

# Floor division: // (divides and rounds down)
print(a // b)    # 3 (10 divided by 3 is 3.333..., rounded down)
print(10 // 2)   # 5

# Modulo (remainder): % (gives the remainder after division)
print(a % b)     # 1 (10 divided by 3 leaves remainder 1)
print(10 % 3)    # 1
print(10 % 2)    # 0 (10 divides evenly by 2)

# Exponentiation (power): **
print(2 ** 3)    # 8 (2 to the power of 3)
print(5 ** 2)    # 25 (5 squared)

# ---------------------------------------------------------
# Order of operations (PEMDAS/BODMAS)
# ---------------------------------------------------------
# Python follows the standard mathematical order:
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

result1 = 2 + 3 * 4       # multiplication first
print(result1)            # 14 (not 20)

result2 = (2 + 3) * 4     # parentheses first
print(result2)            # 20

result3 = 10 - 2 ** 2     # exponent first
print(result3)            # 6 (10 - 4)

# ---------------------------------------------------------
# Compound assignment operators (shorthand)
# ---------------------------------------------------------
# Instead of x = x + 5, you can write x += 5

x = 10
x += 5               # equivalent to x = x + 5
print(x)             # 15

x -= 3               # equivalent to x = x - 3
print(x)             # 12

x *= 2               # equivalent to x = x * 2
print(x)             # 24

x /= 4               # equivalent to x = x / 4
print(x)             # 6.0

# Other compound operators:
x //= 2              # floor division
x **= 2              # exponentiation
x %= 3               # modulo

# ---------------------------------------------------------
# Working with strings (concatenation and repetition)
# ---------------------------------------------------------
# String concatenation (joining): +
greeting = "Hello" + " " + "World"
print(greeting)      # Hello World

# String repetition (repeating): *
stars = "*" * 10
print(stars)         # **********

word = "Ha"
laugh = word * 3
print(laugh)         # HaHaHa

# ---------------------------------------------------------
# Type conversion (casting)
# ---------------------------------------------------------
# Convert between types using int(), float(), str()

# String to integer
num_str = "42"
num_int = int(num_str)
print(num_int, type(num_int))     # 42 <class 'int'>

# String to float
price_str = "19.99"
price_float = float(price_str)
print(price_float, type(price_float))  # 19.99 <class 'float'>

# Number to string
count = 100
count_str = str(count)
print(count_str, type(count_str))     # 100 <class 'str'>

# Float to integer (truncates decimal)
value = 9.7
truncated = int(value)
print(truncated)     # 9 (decimal part is removed)

# ---------------------------------------------------------
# Practical examples
# ---------------------------------------------------------
# Calculate total price with tax
price = 50
tax_rate = 0.08      # 8% tax
total = price + (price * tax_rate)
print(f"Price: ${price}, Total with tax: ${total:.2f}")
# Price: $50, Total with tax: $54.00

# Calculate average of three numbers
score1 = 85
score2 = 90
score3 = 78
average = (score1 + score2 + score3) / 3
print(f"Average score: {average:.1f}")
# Average score: 84.3

# Convert temperature (Fahrenheit to Celsius)
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F = {celsius:.1f}°C")
# 98.6°F = 37.0°C

# ---------------------------------------------------------
# RULE OF THUMB:
#   - Use +, -, *, /, //, %, ** for math operations
#   - Remember: / always returns float, // returns integer
#   - Use compound operators (+=, -=, etc.) for cleaner code
#   - Python follows standard math order: PEMDAS
#   - Use parentheses to make order explicit and readable
#   - Convert types with int(), float(), str() when needed
# ---------------------------------------------------------
