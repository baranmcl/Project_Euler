#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def palCheck(n):
    number = str(n)
    backwards = number[::-1]
    if number == backwards:
        return True
    return False

def palNum():
    answer =
    digitrange = xrange(100, 1000)
    for i1 in digitrange:
        for i2 in digitrange:
            if palCheck(i1*i2):
                if i1*i2 > answer: i1*i2 = answer
    return answer

if __name__ == '__main__':
    print(palNum())
