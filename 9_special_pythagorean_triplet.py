#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a**2 + b**2 = c**2

#For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
def pythagTrip(n):
    for i in range(1,n,1):
        for j in range(1,n-1,1):
            k = n-i-j
            if i**2+j**2==k**2:
                return i*j*k
    return 0


if __name__ == '__main__':
    print(pythagTrip(1000))
