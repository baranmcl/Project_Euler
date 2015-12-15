#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def sumthreefive(n):
    answer = 0
    for i in range(n):
        if i % 3 == 0:
            answer += i
        elif i % 5 == 0:
            answer += i
    return answer


if __name__ == '__main__':
    print(sumthreefive(1000))
