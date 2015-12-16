#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.
def collatzLen(n):
    count = 1
    current = n
    while current > 1:
        if current % 2 == 0:
            current = current / 2
        elif current % 2 == 1:
            current = 3*current + 1
        count += 1
    return count

def longestCollatz(n):
    answer = 0
    longest = 0
    for i in xrange(n):
        collatz = collatzLen(i)
        if collatz > longest:
            longest = collatz
            answer = i
    return longest, answer


if __name__ == '__main__':
    print(longestCollatz(1000000))
