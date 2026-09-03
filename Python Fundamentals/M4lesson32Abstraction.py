from abc import ABC, abstractmethod

##############################

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print("Paid using UPI:", amount)

class CreditCard(Payment):

    def pay(self, amount):
        print("Paid using Credit Card:", amount)


###################################

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    def validate(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")


class UPI(Payment):

    def pay(self, amount):
        self.validate(amount)
        print("UPI payment:", amount)


class Card(Payment):

    def pay(self, amount):
        self.validate(amount)
        print("Card payment:", amount)


class Wallet(Payment):

    pass


upi = UPI()
card = Card()

upi.pay(500)
card.pay(1000)

wallet = Wallet()