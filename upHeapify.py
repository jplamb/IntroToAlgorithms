# Problem Set 4
# Up Heapify
# 7/27/16

# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done
#

def up_heapify(L, i):
    #
    if parent(i) < 0: #what if node is inserted at root? is that an up heapify problem or a down heapify?
        return
    if L[parent(i)] <= L[i]:
        return
    if L[parent(i)] > L[i]:
        (L[parent(i)], L[i]) = (L[i],L[parent(i)])
        up_heapify(L,parent(i))
    return

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def test():
    L = [2, 4, 3, 5, 9, 7, 7]
    L.append(1)
    up_heapify(L, 7)
    assert 1 == L[0]
    assert 2 == L[1]

test()