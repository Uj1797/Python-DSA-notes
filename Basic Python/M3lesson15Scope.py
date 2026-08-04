#Local variables are more important than global variables.

#Python always looks:

#Local

#↓

#Global

#This is called scope resolution.

#user = "Kindled"

#def login():

  #  user = "Alice"

 #   print(user)

#login()

#print(user)

x = 10

def test():
    print(x)

    x = 20

test()