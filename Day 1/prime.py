import math as m
num = int(input())

# Approach 1
def isPrime1(num):
    cnt = 0
    prime = True
    for i in range(2, num-1):
        cnt += 1
        if num % i == 0:
            prime = False
            print(num, "Not a prime")
            break
    if prime:
        print(num, "is a prime")
    print(cnt, " no. of times loop has been executed!")
isPrime1(num)

# Approach 2
def isPrime2(num):
    cnt = 0
    prime = True
    for i in range(2, (num//2)+1):
        cnt += 1
        if num % i == 0:
            prime = False
            print(num, "Not a prime")
            break
    if prime:
        print(num, "is a prime")
    print(cnt, " no. of times loop has been executed!")
isPrime2(num)

# Approach 3
def isPrime3(num):
    cnt = 0
    prime = True
    for i in range(2, int(m.sqrt(num))+1):
        cnt += 1
        if num % i == 0:
            prime = False
            print(num, "Not a prime")
            break
    if prime:
        print(num, "is a prime")
    print(cnt, " no. of times loop has been executed!")
isPrime3(num)
