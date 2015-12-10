#The sum of the squares of the first ten natural numbers is,
#1**2 + 2**2 + ... + 10**2 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)**2 = 55**2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers
#and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def sumSquareDiff(n):
    numRange = range(1, n+1)
    sumSquare = (sum(numRange))**2 #square of the sum
    squareSum = 0 #sum of the squares
    for i in numRange:
        squareSum += (i**2)
        
    return sumSquare-squareSum

if __name__ == '__main__':
    print(sumSquareDiff(100))
