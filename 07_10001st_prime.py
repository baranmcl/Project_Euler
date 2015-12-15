#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import math

def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in xrange(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

def primeNumber(n):
    currentPrime = 2
    primeCount = 1
    primeLimit = n
    for i in xrange(3, 9999999, 2):
        if isPrime(i):
            currentPrime = i
            primeCount += 1
        if primeCount == primeLimit:
            break
    return currentPrime

if __name__ == '__main__':
    print(primeNumber(10001))
