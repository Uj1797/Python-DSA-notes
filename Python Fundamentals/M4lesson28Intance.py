What Is an Instance Method?

A method is simply a function defined inside a class.

class BankAccount:

    def deposit(self, amount):
        self.balance += amount


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


Multiple Methods

We can now build a useful object:

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance