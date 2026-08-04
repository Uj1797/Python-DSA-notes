def test():
    print("A")

    return

    print("B")

## B will not be printed because the return statement ends the function execution before it can reach that line.

def hello():
    return "Hello"

print(hello())

# Output: Hello because the function returns the string "Hello" and it is printed to the console.

def add():
    print(10 + 20)

x = add()

print(x)

# Output: 30 because the function add() prints the sum of 10 and 20, but it does not return any value. Therefore, x is assigned None, and printing x will output None.