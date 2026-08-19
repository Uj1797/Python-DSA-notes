# =============================================================
# LESSON 28: Instance Methods (functions inside classes)
# =============================================================
# An INSTANCE METHOD is a function inside a class.
# First parameter is always `self` (refers to the current object).
# Methods let objects DO things with their own data.

# ---------------------------------------------------------
# Basic instance method
# ---------------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount

account = BankAccount("Alice", 100)
account.deposit(50)
print(account.balance)  # 150

# ---------------------------------------------------------
# Multiple methods in one class
# ---------------------------------------------------------
class BankAccount2:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money."""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Remove money if funds available."""
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        print("Insufficient funds")
        return None

    def get_balance(self):
        """Return current balance."""
        return self.balance

account = BankAccount2("Bob", 500)
print(account.get_balance())      # 500
account.deposit(200)              # 700
account.withdraw(100)             # 600
print(account.get_balance())      # 600

# ---------------------------------------------------------
# Methods that return values vs modify state
# ---------------------------------------------------------
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment and return new value."""
        self.count += 1
        return self.count

    def reset(self):
        """Reset to zero (returns nothing)."""
        self.count = 0

counter = Counter()
print(counter.increment())  # 1
print(counter.increment())  # 2
counter.reset()
print(counter.count)        # 0

# ---------------------------------------------------------
# Real-world example: Student with methods
# ---------------------------------------------------------
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Record a grade."""
        self.grades.append(grade)

    def get_average(self):
        """Calculate average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_highest(self):
        """Return highest grade."""
        return max(self.grades) if self.grades else None

student = Student("Alice")
student.add_grade(95)
student.add_grade(87)
student.add_grade(92)
print(f"Average: {student.get_average():.1f}")   # 91.3
print(f"Highest: {student.get_highest()}")       # 95

# ---------------------------------------------------------
# Function vs Method comparison
# ---------------------------------------------------------
# Standalone function:
def add(a, b):
    return a + b

# Method inside class:
class Calculator:
    def add(self, a, b):
        return a + b

print(add(5, 3))              # 8 (function)
calc = Calculator()
print(calc.add(5, 3))         # 8 (method)

# ---------------------------------------------------------
# RULE OF THUMB:
#   - Methods are functions inside a class
#   - First parameter is always `self` (current object)
#   - Use methods to make objects DO things
#   - Each object has independent copies of its data
#   - Methods work on the object's own attributes (self.x)
# ---------------------------------------------------------
