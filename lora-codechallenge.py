# input_str = sorted(input().split(' '))
#
# x = int(input_str[0])
# y = int(input_str[1])
#
# print(x,y)
#
# def prime(i):
#     for j in range(2,i):
#         if i % j == 0:
#             return False
#
# def find_primes(x,y): #1,5
#     print(list((i+j) for i in range(x,y + 1) for j in range(2,y) if i % j != 0))
#
# find_primes(x,y)

stuff = [[4,1], [1,2], [1,3], [1,4]]

money = stuff[0][1]
print(f'The money is {money}')

lst1 = [item[0] for item in stuff[1:]]
lst2 = [item[1] for item in stuff[1:]]
print(lst1, lst2)

# print(list((i,j) for i in lst1 for j in lst2 if abs(i - j) == money))

for i in lst1:
    for j in lst2:
        if abs(i-j) == money:
            print(i,j)
