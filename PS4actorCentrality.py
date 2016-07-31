# Problem Set 4 Actor Centrality
# 7/30/16

#Initially tripped up because graph contains actors and movies as nodes. We only need to evaluate the actors.
#So the program was returning bad values because it was including movies in the top k
#Fixed that problem by creating seperate dictionaries for actors and movies and looping through the keys of actors
#The real key to this problem was combining multiple concepts from lectures and reworking several of the algorithms to
#use dictionaries instead of lists

import re
import random

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def create_actor_graph():
    G = {}
    actors = {}
    movies = {}
    with open("imdb-1.txt") as f:
        for line in f:
            link = re.split(r'\t+', line.rstrip('\t'))
            actor = link[0]
            movie = ' '.join(link[1:])
            actors[actor] = 1
            movies[movie] = 1
            G = make_link(G, actor, movie)
    return (G, actors, movies)
            
def average_centrality(G,v):
    dist_from_start = {}
    open_list = [v]
    dist_from_start[v] = 0
    while len(open_list) > 0:
        curr = open_list[0]
        del open_list[0]
        for neighbor in G[curr].keys():
            if neighbor not in dist_from_start:
                dist_from_start[neighbor] = dist_from_start[curr] + 1
                open_list.append(neighbor)
    return (sum(dist_from_start.values())+0.0)/len(dist_from_start)

def partition(L,v):
    small = {}
    equal ={}
    big = {}
    for x in L.keys():
        if L[x] < L[v]:
            small[x] = L[x]
        if L[x] > L[v]:
            big[x] = L[x]
        if L[x] == L[v]:
            equal[x] = L[x]
    return (small, equal, big)

def top_k(L,k):

    if len(L.keys()) > 0:
        #v = L[random.randrange(len(L))]
        v = random.choice(L.keys())
    else:
        return []
    (left,middle,right) = partition(L,v)
    
    if len(left) >= k:
        return top_k(left, k)
    elif len(left) + len(middle) >= k:
        return v
    else:
        return top_k(right, k - len(left)-len(middle))
    # if len(left) == k:
    #     return left
    # if len(left)+1 == k:
    #     return left + L[v]
    # if len(left) > k:
    #     return top_k(left, k)
    # return left + L[v] + top_k(right,k-len(left)-1)

def top_k_actors(topk):
    (G, actors, movies) = create_actor_graph()

    centrality = {}
    for actor in actors.keys():
        centrality[actor] = average_centrality(G,actor)  

    twenty = top_k(centrality, topk)

    print twenty
    print centrality[twenty]
    return twenty
    
def test(ans):
    assert ans == 'Tatasciore, Fred'

ans = top_k_actors(1)

test(ans)