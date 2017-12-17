import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
numbers = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

print (list(itertools.chain(letters, booleans, decimals)))

#count goes on infinitely
for i in itertools.count(10, 0.25):
    if i < 20:
        print(i)
    else:
        break
#compress(a,b) returns all elements in a if the corresponding element in b is True
print (list(itertools.compress(letters, booleans)))
