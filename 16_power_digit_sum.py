#2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2**1000?
def powerDigitSum(x, y):
    power_sum = x**y
    answer = 0
    for number in str(power_sum):
        answer += int(number)
    return answer

if __name__ == '__main__':
    print(powerDigitSum(2, 1000))
