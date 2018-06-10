"""
https://www.hackerrank.com/challenges/collections-counter/problem
"""

if __name__ == '__main__':
    x = int(input()) #num of shoes

    n = input() #list of all the shoe sizes in the shop, space-separated
    list_of_shoe_sizes = []
    for i in n.split():
        list_of_shoe_sizes.append(int(i))
    print(list_of_shoe_sizes)

    num_of_customers = int(input()) # num of customers

    total = 0
    for i in range(0,num_of_customers):
        this = input()
        shoe_size, price = this.split()
        shoe_size = int(shoe_size)
        price = int(price)

        if shoe_size in list_of_shoe_sizes:
            total += price
            list_of_shoe_sizes.remove(shoe_size)
    print("Total ",total)
    print("List", list_of_shoe_sizes)
