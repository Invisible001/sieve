# Author: Nguyen L.
# Date:   April 25th, 2020
# Generating prime numbers, implementing Sieve of Eratosthenes algorithm

# function to find prime numbers
def sieveOfEratosthenes(n):

    # set p to 2
    p = 2 

    # there's a more efficient way to do this too, by setting up all unmarked to true in the list
    # but I'm taking a longer route
    marked_list = []
    prime_list = []
    for i in range(p, n+1):

        # if unmarked, that means it's a prime number 
        if i not in marked_list:
            prime_list.append(i)

        for j in range(p*p, n+1, p):
            marked_list.append(j)
        p+=1

    return prime_list 

print("Input parameter: ", end='')
num = int(input())
my_list = sieveOfEratosthenes(num)

print(my_list)
