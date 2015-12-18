# -*- coding: UTF-8 -*-
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
#there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

def latticePaths(n):
    matrix = [1] * n
    for i in range(n):
        for j in range(i):
            matrix[j] = matrix[j]+matrix[j-1]
            #print matrix , i , j
        matrix[i] = 2 * matrix[i - 1]
        #print matrix, i
    return matrix[n-1] #returns the bottom right corner

if __name__ == '__main__':
    print(latticePaths(20))

#once again, help was found from Jason's Code Blog.
#http://code.jasonbhill.com/python/project-euler-problem-15/
