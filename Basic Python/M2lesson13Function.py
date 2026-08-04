def greet():
    print("Hello")

greet()

#PARAMETERS

def greet(name):
    print("Hello", name)

greet("Alice")

#Fastapi example

#@app.get("/users")
#def get_users():
 #   ...

def greet(name):
    print("Hello", name)

person = "Bob"

greet(person)

def welcome(name):
    print("Welcome", name)

users = [
    "Alice",
    "Bob",
    "Charlie"
]

for user in users:
    welcome(user)

print("Done")