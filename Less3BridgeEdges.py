# Problem set 3 Challenge Question
# 7/19/16

# Runs fine locally
# Unfortunately, the grader won't accept this due to a type error

# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs 
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
# 
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1}, 
#      'b': {'a': 1, 'd': 1}, 
#      'c': {'a': 1, 'd': 1}, 
#      'd': {'c': 1, 'b': 1, 'e': 1}, 
#      'e': {'d': 1, 'g': 1, 'f': 1}, 
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1} 
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'}, 
#      'b': {'a': 'green', 'd': 'red'}, 
#      'c': {'a': 'green', 'd': 'green'}, 
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'} 
#      }
#

def create_rooted_spanning_tree(G, root):
    S = G
    open_list = [root]
    
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        
        for neighbor in S[current].keys():
            if S[current][neighbor] == 1:
                if neighbor in open_list:
                    S[current][neighbor] = 'red'
                    S[neighbor][current] = 'red'
                else:
                    open_list.append(neighbor)
                    S[current][neighbor] = 'green'
                    S[neighbor][current] = 'green'
        
    return S

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'}, 
                 'b': {'a': 'green', 'd': 'red'}, 
                 'c': {'a': 'green', 'd': 'green'}, 
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }

###########
#doesn't match test case because f and g are childless and at the same level so their post orders are interchangeable
def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    open_list = [root]
    po = {}
    low = 1
    high = len(S)
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in S[current].keys():
            if sum(x == 'green' for x in S[neighbor].values())-1 == 0 and neighbor not in po:
                po[neighbor] = low
                low += 1
            elif neighbor not in po:
                po[current] = high
                high -= 1
                open_list.append(neighbor)
        if high == low:
            po[current] = high

    return po


# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}

##############

def number_of_descendants(S, root, po):
    nod = {}
    #po = post_order(S, root)
    for node in sorted(po.items(), key = lambda x: x[1]):
        desc = 1
        for neighbor in S[node[0]].keys():
            if po[neighbor] < po[node[0]] and S[neighbor][node[0]] == 'green':
                desc += nod[neighbor]
        nod[node[0]] = desc
        
    return nod

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    po = post_order(S, 'a')
    nd = number_of_descendants(S, 'a', po)
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

###############

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    poLow = {}
    
    for node in sorted(po.items(), key = lambda x: x[1]):
        poLow[node[0]] = po[node[0]]
        for neighbor in S[node[0]].keys():
            if not (S[neighbor][node[0]] == 'green' and po[neighbor] > po[node[0]]) and po[neighbor] < poLow[node[0]]:
                poLow[node[0]] = po[neighbor]
                for redNeighbor in S[neighbor].keys():
                    if S[redNeighbor][neighbor] == 'red' and po[redNeighbor] < poLow[node[0]]:
                        poLow[node[0]] = po[redNeighbor]
                
    return poLow

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}


################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    poHigh = {}
    
    for node in sorted(po.items(), key = lambda x: x[1]):
        poHigh[node[0]] = po[node[0]]
        for neighbor in S[node[0]].keys():
            if not (S[neighbor][node[0]] == 'green' and po[neighbor] > po[node[0]]) and po[neighbor] > poHigh[node[0]]:
                poHigh[node[0]] = po[neighbor]
                for redNeighbor in S[neighbor].keys():
                    if S[redNeighbor][neighbor] == 'red' and po[redNeighbor] > poHigh[node[0]]:
                        poHigh[node[0]] = po[redNeighbor]
    #print sorted(poHigh.items(), key = lambda x: x[0])             
    return poHigh

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
    
#################

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    nod = number_of_descendants(S, root, po)
    poHigh = highest_post_order(S, root, po)
    poLow = lowest_post_order(S, root, po)
    
    bridge = []
    
    for node in sorted(po.items(), key = lambda x: x[1]):
        for neighbor in S[node[0]].keys():
            if (poHigh[neighbor] <= po[neighbor] and poLow[neighbor] > (po[neighbor] - nod[neighbor]) 
                and S[neighbor][node[0]] == 'green' and (neighbor,node[0]) not in bridge
                and po[node[0]] > po[neighbor]):
                #print (node[0], neighbor)
                #print str(poHigh[neighbor]) + ' <= ' + str(po[neighbor]) + ' and ',
                #print str(poLow[neighbor]) + ' > (' + str(po[neighbor]) + ' - ' + str(nod[neighbor]) 
                bridge.append((node[0],neighbor))
    #print bridge
    return bridge

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]
    
test_bridge_edges()
