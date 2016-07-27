# Problem Set 4 Question 2
# Minimize Sum of Aboluste
# 7/27/16

# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
# 
# Your code should run in Theta(n) time
#
#from Less4statistics import median 

# scratch work to find relationship between summing list and x...minimizing the sum occurs at the median
def scratch_minimize_absolute(L):
    minX = 0
    
    minSum = sum(L)
    for x in range(0,max(L)/2):
        hsum = 0
        for y in L:
            hsum += abs(y - x)
        print hsum, x
        if hsum < minSum:
            minSum = hsum
            minX = x
    print minSum, minX
    
    return minX

def median(L):
    L.sort()
    return L[len(L)/2]

def minimize_absolute(L):    
    return median(L)

L = [5,10,15,27,45,84,36,52,31,95, 400,1]
minimize_absolute(L)
print median(L)