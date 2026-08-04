def change(x):
    x = 100

a = 10

change(a)

print(a)

#because the variable a is passed by value, the change function does not affect the original variable a. The output will be 10.

def change(lst):
    lst.append(100)

numbers = [10, 20]

change(numbers)

print(numbers)

#because the variable numbers is passed by reference, the change function modifies the original list. The output will be [10, 20, 100].

def change(lst):
    lst = [100]

numbers = [1,2]

change(numbers)

print(numbers)

#because the variable numbers is passed by reference, but the change function reassigns lst to a new list, the original list remains unchanged. The output will be [1, 2].

def add(text):
    text += "!"

word = "Hello"

add(word)

print(word)

#because the variable word is passed by value, the add function does not affect the original variable word. The output will be "Hello".

def add(items):
    items += [4]

numbers = [1,2,3]

add(numbers)

print(numbers)

#because the variable numbers is passed by reference, the add function modifies the original list. The output will be [1, 2, 3, 4].