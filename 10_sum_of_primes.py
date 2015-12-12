#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import math

def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

def sumPrimes(n):
    answer = 2
    for i in xrange(3, n, 2):
        if isPrime(i):
            answer += i
    return answer


if __name__ == '__main__':
    print(sumPrimes(2000000))
