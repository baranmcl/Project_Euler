#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
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

def largestPrimeFactor(n):
    answer = 0
    for i in range(1, int(math.sqrt(n))):
        if n % i == 0:
            if isPrime(i):
                answer = i
    return answer


if __name__ == '__main__':
  print(largestPrimeFactor(600851475143))
