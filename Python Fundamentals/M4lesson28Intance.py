# =============================================================
# LESSON 28: Instance Methods (methods inside classes)
# =============================================================
# A METHOD is a function defined inside a class that operates on
# an object's data (attributes). Methods let objects DO things,
# not just store data.

# ---------------------------------------------------------
# What is an instance method?
# ---------------------------------------------------------
# An INSTANCE METHOD is a function inside a class that:
#   1. Takes `self` as the first parameter (refers to the object)
#   2. Can access and modify the object's attributes
#   3. Is called on an object using dot notation

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # This is an instance method:
    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount

# Create an account and call the method
account = BankAccount("Alice", 100)
account.deposit(50)            # calling the method
print(account.balance)         # 150

# ---------------------------------------------------------
# Multiple methods in one class
# ---------------------------------------------------------
class BankAccount2:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount
        return self.balance    # return the new balance

    def withdraw(self, amount):
        """Remove money if funds are available."""
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        print("Insufficient funds")
        return None

    def get_balance(self):
        """Return the current balance."""
        return self.balance

# Use the methods
account = BankAccount2("Bob", 500)
print(account.get_balance())      # 500

account.deposit(200)
print(account.get_balance())      # 700

account.withdraw(100)
print(account.get_balance())      # 600

# ---------------------------------------------------------
# Methods that return values vs methods that just modify
# ---------------------------------------------------------
class Counter:
    def __init__(self, start=0):
        self.count = start

    def increment(self):
        """Increment the counter and return the new value."""
        self.count += 1
        return self.count

    def reset(self):
        """Reset the counter to zero (returns nothing)."""
        self.count = 0

counter = Counter()
print(counter.increment())        # 1
print(counter.increment())        # 2
result = counter.increment()      # 3
print(result)                     # 3
counter.reset()
print(counter.count)              # 0

# ---------------------------------------------------------
# Methods that call other methods (chaining behavior)
# ---------------------------------------------------------
class Todo:
    def __init__(self, title):
        self.title = title
        self.is_completed = False

    def complete(self):
        """Mark the todo as completed."""
        self.is_completed = True
        self.show_status()       # call another method

    def show_status(self):
        """Display the todo status."""
        status = "✓" if self.is_completed else "○"
        print(f"{status} {self.title}")

task = Todo("Buy groceries")
task.show_status()                # ○ Buy groceries
task.complete()                   # ✓ Buy groceries (and shows status)

# ---------------------------------------------------------
# Real-world example: Student grade tracker
# ---------------------------------------------------------
class StudentGradeTracker:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Add a grade to the list."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False

    def get_average(self):
        """Calculate and return the average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_highest(self):
        """Return the highest grade."""
        if not self.grades:
            return None
        return max(self.grades)

    def print_summary(self):
        """Print a summary of grades."""
        print(f"\n{self.name}'s Grades:")
        print(f"  All grades: {self.grades}")
        print(f"  Average: {self.get_average():.1f}")
        print(f"  Highest: {self.get_highest()}")

student = StudentGradeTracker("Alice")
student.add_grade(95)
student.add_grade(87)
student.add_grade(92)
student.print_summary()
# Alice's Grades:
#   All grades: [95, 87, 92]
#   Average: 91.3
#   Highest: 95

# ---------------------------------------------------------
# Real-world example: Shopping cart
# ---------------------------------------------------------
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, price):
        """Add an item to the cart."""
        self.items.append({"name": item_name, "price": price})
        print(f"Added {item_name} (${price})")

    def remove_item(self, item_name):
        """Remove an item by name."""
        self.items = [item for item in self.items if item["name"] != item_name]
        print(f"Removed {item_name}")

    def get_total(self):
        """Calculate the total price."""
        return sum(item["price"] for item in self.items)

    def show_cart(self):
        """Display all items in the cart."""
        if not self.items:
            print("Cart is empty")
        else:
            for item in self.items:
                print(f"  - {item['name']}: ${item['price']}")
            print(f"Total: ${self.get_total():.2f}")

cart = ShoppingCart()
cart.add_item("Laptop", 999)
cart.add_item("Mouse", 25)
cart.add_item("Keyboard", 75)
cart.show_cart()
# Laptop: $999
# Mouse: $25
# Keyboard: $75
# Total: $1099.00

cart.remove_item("Mouse")
cart.show_cart()
# Laptop: $999
# Keyboard: $75
# Total: $1074.00

# ---------------------------------------------------------
# Key differences: Function vs Method
# ---------------------------------------------------------
# Function (standalone):
def add_numbers(a, b):
    return a + b

# Method (inside a class):
class Calculator:
    def add_numbers(self, a, b):
        return a + b

calc = Calculator()
print(add_numbers(5, 3))           # 8 (function call)
print(calc.add_numbers(5, 3))      # 8 (method call)

# ---------------------------------------------------------
# RULE OF THUMB:
#   - Methods are functions inside a class
#   - First parameter is always `self` (refers to the object)
#   - Methods can access and modify object attributes (self.x)
#   - Methods can call other methods on the same object
#   - Use methods to make objects DO things, not just store data
#   - Methods make code more organized and object-oriented
# ---------------------------------------------------------
