#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
#therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

def sumDivisors(n):
    answer = 0
    for i in xrange(1, n):
        if n  % i == 0: answer += i
    return answer

def amicableNumbers(limit):
    amicableList = []
    for i in xrange(1, limit):
        x = sumDivisors(i)
        y = sumDivisors(x)
        if x != y and i == y:
            if i not in amicableList: amicableList.append(i)
            if x not in amicableList: amicableList.append(x)
    return sum(amicableList)
    
if __name__ == '__main__':
    print(amicableNumbers(10000))
