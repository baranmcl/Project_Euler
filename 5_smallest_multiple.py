#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def smallestMultiple():
    factorList = [11, 13, 14, 16, 17, 18, 19, 20] # no need to check all numbers in range(1-20)
    for i in xrange(20,999999999,20): #searches arbitrarily large range by steps of 20
        if all(i % n == 0 for n in factorList): #if all factorlists divide return answer
            return i
    return None

if __name__ == '__main__':
    print(smallestMultiple())
