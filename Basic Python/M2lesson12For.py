numbers = [10,20]

for n in numbers:
    #print(n)

#print(n)

## Important

 numbers = [1,2,3]

for number in numbers:
    number = 100
    ## this will not change the original iterable as integers are immutable in Python

#print(numbers)

numbers = [[1],[2],[3]]

for item in numbers:
    item.append(100)

print(numbers)