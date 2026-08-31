class product:
      def __init__(self,price):
            self._price = price

      @property
      def price(self):
            return self._price

      @price.setter
      def price(self,value):
            if value < 100:
                  raise ValueError("Minimum balance should be 100")
            self._price = value

x = product(500)

print(x.price)

x.price = 2500

print(x.price)

#x._price = 1000

#print(x._price)
