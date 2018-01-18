"""
Write a program that takes L and R as input and displays the number of prime numbers that lie between L and R(L and R inclusive) and can be represented as sum of two consecutive prime numbers + 1.

Example:
Case1:
For the input provided as follows:
1 20
Output of the program will  be: 2
Explanation: 13 is a prime number which can be expressed like 5 + 7 + 1.
19 is a prime number which can be expressed like 7 + 11 + 1.

Note that 5 and 7 are consecutive primes. Similarly 7 and 11 are consecutive primes.

Case2:
Input: 1 10
Output: 0
Explanation: No prime numebrs lie between 1 and 10 that can be represented as sum of two consecutive prime numbers + 1, hence 0 is displayed.
"""
input_str = raw_input()

input_str = sorted(input_str.split(' '))


x = int(input_str[0])
y = int(input_str[1])


primelist = []
between = []
consec_primes = []


def prime(i):
   for j in range(2, i):
       if i % j == 0:
           return False

for i in range(2, (y + 1)):
   if prime(i) is not False:
       primelist.append(i)

for z in range(x, (y + 1)):
    if z >= 13 and prime(z) is not False:
        between.append(z)

def consecutive(a):
   for c in range(0, (len(primelist) - 1)):
       x = c
       y = c + 1
       if primelist[x] + primelist[y] + 1 == a:
         print(primelist[x], '+', primelist[y], '+ 1 = ', a)
         consec_primes.append(a)


for i in between:
    consecutive(i)

print('primelist: ', primelist)
print('between: ', between)
print('consec_primes: ', consec_primes)
print(len(consec_primes))
