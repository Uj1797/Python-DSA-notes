class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


a = BankAccount("Alice", 5000)

b = BankAccount("Bob")

a.balance += 1000

b.balance += 200

print(a.owner)
print(a.balance)

print(b.owner)
print(b.balance)