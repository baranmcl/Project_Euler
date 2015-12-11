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
    return n



if __name__ == '__main__':
    print(primeNumber(10001))
