"""
https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
Let min_guess = 0 and max_guess = n-1.
If max_guess < min_guess, then stop: target is not present in array. Return -1.
Compute guess as the average of max_guess and min_guess, rounded down (so that it is an integer).
If array[guess] equals target, then stop. You found it! Return guess.
If the guess was too low, that is, array[guess] < target, then set min_guess = guess + 1.
Otherwise, the guess was too high. Set max_guess = guess - 1.
Go back to step 2.
"""
from math import floor

def binarySearch(array, target):
    min_guess = 0
    max_guess = len(array) - 1

    while max_guess > min_guess :
        guess = floor(( max_guess + min_guess ) / 2 )
        if array[guess] == target:
            return guess
        elif array[guess] < target:
            min_guess = guess + 1
        else:
            max_guess = guess -1

    return -1


array = [1,2,3,4,5,6,7,8,9,10]
target = 8

answer = binarySearch(array, target)
print(answer)
