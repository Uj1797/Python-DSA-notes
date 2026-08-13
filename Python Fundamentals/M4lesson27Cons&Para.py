# =============================================================
# LESSON 27: Constructors & Parameters (__init__)
# =============================================================
# The __init__ method is a CONSTRUCTOR -- a special method that
# runs automatically when you create a new object (instance).
# It lets you initialize the object's attributes with custom values.

# ---------------------------------------------------------
# Basic constructor (no parameters)
# ---------------------------------------------------------
class Student:
    def __init__(self):
        """Constructor: runs automatically when Student() is called."""
        self.name = "Unknown"
        self.age = 18

s1 = Student()       # __init__ runs automatically
print(s1.name)       # Unknown
print(s1.age)        # 18

# Every object gets the same default values
s2 = Student()
print(s2.name)       # Unknown (same default)

# ---------------------------------------------------------
# Constructor with parameters (customization)
# ---------------------------------------------------------
# Parameters let each object have different starting values

class BankAccount:
    def __init__(self, owner, balance=0):
        """Constructor with owner (required) and balance (optional)."""
        self.owner = owner
        self.balance = balance

# Create accounts with different values
account1 = BankAccount("Alice", 5000)
account2 = BankAccount("Bob")           # uses default balance=0
account3 = BankAccount("Charlie", 2500)

print(account1.owner, account1.balance)  # Alice 5000
print(account2.owner, account2.balance)  # Bob 0
print(account3.owner, account3.balance)  # Charlie 2500

# ---------------------------------------------------------
# Modifying attributes after creation
# ---------------------------------------------------------
# You can change attributes after the object is created

account1.balance += 1000
account2.balance += 200

print(account1.balance)   # 6000
print(account2.balance)   # 200

# ---------------------------------------------------------
# Multiple parameters in __init__
# ---------------------------------------------------------
class Person:
    def __init__(self, name, age, city):
        """Constructor with three required parameters."""
        self.name = name
        self.age = age
        self.city = city

person1 = Person("Alice", 30, "New York")
person2 = Person("Bob", 25, "Los Angeles")

print(f"{person1.name} is {person1.age} and lives in {person1.city}")
# Alice is 30 and lives in New York

# ---------------------------------------------------------
# Default parameter values in __init__
# ---------------------------------------------------------
class Car:
    def __init__(self, brand, year=2024, color="white"):
        """Constructor with defaults for year and color."""
        self.brand = brand
        self.year = year
        self.color = color

car1 = Car("Toyota")                    # uses defaults for year and color
car2 = Car("Honda", 2023)               # custom year, default color
car3 = Car("BMW", 2022, "black")        # all custom

print(car1.brand, car1.year, car1.color)  # Toyota 2024 white
print(car2.brand, car2.year, car2.color)  # Honda 2023 white
print(car3.brand, car3.year, car3.color)  # BMW 2022 black

# ---------------------------------------------------------
# Real-world example: User registration
# ---------------------------------------------------------
class User:
    def __init__(self, username, email, password):
        """Initialize a new user with required registration info."""
        self.username = username
        self.email = email
        self.password = password  # in real code, password should be hashed!
        self.is_active = True     # all new users start active
        self.created_at = "2024"  # simplified for this example

user1 = User("alice123", "alice@example.com", "secret123")
user2 = User("bob456", "bob@example.com", "password456")

print(f"User {user1.username} created at {user1.created_at}")
# User alice123 created at 2024

# ---------------------------------------------------------
# Real-world example: Game character with stats
# ---------------------------------------------------------
class Character:
    def __init__(self, name, level=1, health=100):
        """Create a game character with name, level, and health."""
        self.name = name
        self.level = level
        self.health = health
        self.experience = 0

player1 = Character("Hero", level=5, health=150)
player2 = Character("Novice")  # uses defaults: level 1, health 100

print(f"{player1.name}: Level {player1.level}, Health {player1.health}")
# Hero: Level 5, Health 150

print(f"{player2.name}: Level {player2.level}, Health {player2.health}")
# Novice: Level 1, Health 100

# ---------------------------------------------------------
# IMPORTANT: Each object is independent
# ---------------------------------------------------------
# Changes to one object do NOT affect another

account_a = BankAccount("Alice", 500)
account_b = BankAccount("Bob", 500)

account_a.balance += 1000   # only affects account_a

print(account_a.balance)    # 1500
print(account_b.balance)    # 500 (unchanged)

# ---------------------------------------------------------
# Key concepts
# ---------------------------------------------------------
# __init__         = Constructor method, runs on object creation
# self             = refers to the current object
# Parameters       = values passed to __init__ to customize the object
# Default values   = optional parameters with fallback values
# Attributes       = data stored on the object (self.name, etc.)
# Independence     = each object has its own separate attributes

# ---------------------------------------------------------
# RULE OF THUMB:
#   - __init__ runs automatically when you create an object
#   - Use parameters to customize each object differently
#   - Use default parameter values for optional settings
#   - Each object's attributes are independent of others
#   - Remember: self.attribute assigns to the current object
# ---------------------------------------------------------
