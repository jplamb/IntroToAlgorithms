#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the square of the difference
# between each element in L and x: SUM_{i=0}^{n-1} (L[i] - x)^2
# 
# Your code should run in Theta(n) time
# 
#from Less4statistics import median
def minimize_square(L):
    return (1.0*sum(L)/len(L))

    

#L = [5,10,15,27,45,84,36,52,31,95, 1]
L = [2,2,3,4]
print 'min', minimize_square(L)
