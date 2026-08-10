# =============================================================
# LESSON 26: Object-Oriented Programming (OOP) Basics
# =============================================================
# A CLASS is a blueprint for creating objects.
# An OBJECT is an instance of a class -- a concrete thing created
# from that blueprint with its own data and methods.

# ---------------------------------------------------------
# Creating a simple class
# ---------------------------------------------------------
class Student:
    pass       # an empty class (still valid)

# Student is now a class object. We haven't created any students yet.
print(Student)   # <class '__main__.Student'>

# Creating objects (instances) from the class
s1 = Student()   # create first student object
s2 = Student()   # create second student object

print(s1)        # <__main__.Student object at 0x...>
print(s2)        # <__main__.Student object at 0x...>
# s1 and s2 are separate objects (different memory addresses)

# ---------------------------------------------------------
# Adding attributes to objects
# ---------------------------------------------------------
class Student2:
    pass

alice = Student2()
bob = Student2()

# Assign attributes directly
alice.name = "Alice"
alice.age = 20

bob.name = "Bob"
bob.age = 22

print(alice.name, alice.age)   # Alice 20
print(bob.name, bob.age)       # Bob 22

# ---------------------------------------------------------
# Using __init__ to initialize objects automatically
# ---------------------------------------------------------
class Student3:
    def __init__(self):
        """Constructor: called automatically when creating a new object."""
        self.name = "Unknown"
        self.age = 18

s1 = Student3()
s2 = Student3()

print(s1.name, s1.age)   # Unknown 18
print(s2.name, s2.age)   # Unknown 18

# Each object has its own attributes
s1.name = "Alice"
s1.age = 20

print(s1.name, s1.age)   # Alice 20
print(s2.name, s2.age)   # Unknown 18 (s2 unchanged)

# ---------------------------------------------------------
# __init__ with parameters (customizing each object)
# ---------------------------------------------------------
class Student4:
    def __init__(self, name, age):
        """Constructor with parameters to customize the object."""
        self.name = name
        self.age = age
        self.gpa = 3.5  # default value

s1 = Student4("Alice", 20)
s2 = Student4("Bob", 22)

print(s1.name, s1.age)   # Alice 20
print(s2.name, s2.age)   # Bob 22

# ---------------------------------------------------------
# Adding methods (functions inside a class)
# ---------------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance=0):
        """Initialize account with owner name and balance."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Remove money from the account if funds are available."""
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        print("Insufficient funds")
        return None

    def show_balance(self):
        """Display the current balance."""
        return f"{self.owner}'s balance: ${self.balance}"

# Create an account object
account = BankAccount("Alice", 100)

print(account.show_balance())   # Alice's balance: $100
print(account.deposit(50))      # 150 (new balance)
print(account.withdraw(30))     # 120 (new balance)
print(account.show_balance())   # Alice's balance: $120

# ---------------------------------------------------------
# Understanding `self`
# ---------------------------------------------------------
# `self` refers to the current object (instance).
# When you call account.deposit(50), Python automatically passes
# `account` as `self` to the deposit method.
# So deposit(self, amount) receives:
#   self = account
#   amount = 50

# ---------------------------------------------------------
# Real-world example: User profile class
# ---------------------------------------------------------
class User:
    def __init__(self, username, email):
        """Create a user with username and email."""
        self.username = username
        self.email = email
        self.is_active = True
        self.posts = []

    def create_post(self, content):
        """Add a new post to the user's posts."""
        self.posts.append(content)
        return f"{self.username} posted: {content}"

    def deactivate(self):
        """Deactivate the user account."""
        self.is_active = False
        return f"{self.username}'s account is now inactive"

    def get_post_count(self):
        """Return the number of posts."""
        return len(self.posts)

user1 = User("alice123", "alice@example.com")
user2 = User("bob456", "bob@example.com")

print(user1.create_post("Hello world!"))    # alice123 posted: Hello world!
print(user1.create_post("Python is fun"))   # alice123 posted: Python is fun
print(user1.get_post_count())               # 2

print(user2.create_post("Hi everyone"))     # bob456 posted: Hi everyone
print(user2.get_post_count())               # 1

print(user1.deactivate())                   # alice123's account is now inactive
print(user1.is_active)                      # False
print(user2.is_active)                      # True

# ---------------------------------------------------------
# Key concepts recap
# ---------------------------------------------------------
# Class     = blueprint, template for creating objects
# Object    = an instance of a class, created with data and methods
# __init__  = constructor, automatically called when creating an object
# self      = refers to the current object (instance)
# Attribute = data stored on an object (self.name, self.age)
# Method    = a function defined inside a class (def deposit(self):)

# ---------------------------------------------------------
# RULE OF THUMB:
#   - Classes group related data (attributes) and functions (methods)
#   - __init__ is called automatically when you create a new object
#   - Use `self` to access and modify the object's own attributes
#   - Each object is independent with its own copy of attributes
#   - Methods are functions that work with the object's data
# ---------------------------------------------------------
