# Partitioning example from lesson 4

# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#

def partition(L, v):
    P = []
    left = []
    right = []
    
    for x in L:
        if x < v: 
            left.append(x)
        else:
            right.append(x)
    
    P = left + [v] + right
    return P

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos


