class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} logged in")

class Customer(User):
    pass


class Staff(User):
    pass


class Admin(User):

# Function overide
   # def login(self):
     #    print(f"Admin {self.name} logged in")

#example of super when you want to take some from the parent and some your own
    def login(self):
        super().login()
        print("Admin authentication successful")

    def create_user(self):
        print("User Created")

    def disable_user(self):
        print("disable user")

    def view_activity_log(self):
        print("Activity logs of selected user")

admin = Admin("Jane", "jane@example.com")     

customer = Customer("John Doe", "john@example.com")

customer.login()

admin.login()
admin.create_user()
admin.disable_user()
admin.view_activity_log()


#####################################

class Order:

    def __init__(self, order_id, customer, products, payment):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.payment = payment
        self.status = "Pending"

    def show_order(self):
        print(f"Order: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.status}")


customer = Customer("Alice", "alice@example.com")

order = Order(
    101,
    customer,
    [],
    Payment()
)

order.show_order()

###############################################################

class Order:

    def __init__(self, order_id, customer, payment):
        self.order_id = order_id
        self.customer = customer
        self.payment = payment
        self.products = []
        self.status = "Pending"

    def add_product(self, product):
        """Adds a Product object to the products list."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a Product object from the list if it exists."""
        if product in self.products:
            self.products.remove(product)

    def calculate_total(self):
        """Calculates and returns the total price of all products."""
        total = 0
        for product in self.products:
            total += product.price
        return total

    def checkout(self):
        """Processes the payment and updates the order status."""
        total_amount = self.calculate_total()
        self.payment.pay(total_amount)
        self.status = "Paid"

#############finalTest#########################

from abc import ABC, abstractmethod


# ==========================================
# 1. USER & CUSTOMER COMPONENTS
# ==========================================
class User:
    def __init__(self, name):
        self.name = name


class Customer(User):
    # Inherits everything from User for now
    pass


# ==========================================
# 2. PRODUCT COMPONENT (With Property & Setter)
# ==========================================
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0.")
        self._price = value


# ==========================================
# 3. PAYMENT COMPONENT (Abstract Class & Subclasses)
# ==========================================
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class Wallet(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")


# ==========================================
# 4. ORDER COMPONENT
# ==========================================
class Order:
    def __init__(self, order_id, customer, payment):
        self.order_id = order_id
        self.customer = customer
        self.payment = payment
        self.products = []
        self.status = "Pending"

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def checkout(self):
        total_amount = self.calculate_total()
        self.payment.pay(total_amount)
        self.status = "Paid"


# ==========================================
# 🎯 FINAL TEST EXECUTION
# ==========================================
if __name__ == "__main__":
    # Create Entities
    alice = Customer("Alice")
    laptop = Product("Laptop", 50000)
    mouse = Product("Mouse", 1000)
    upi_payment = UPI()
    
    # Create Order
    order = Order("#101", alice, upi_payment)

    # Manage Items
    order.add_product(laptop)
    order.add_product(mouse)

    # Test Outputs
    print(order.calculate_total())
    order.checkout()
    print(order.status)
