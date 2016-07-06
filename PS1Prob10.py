# Intro to Algorithms Problem Set 1
# Problem 10
# Find a Eulerian Tour
# JPLAMB 7/5/16

# Find Eulerian Tour
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
	for node in graph:
		tour = [node[0]]
		burned = []

		skip = []

		cnt = 1

		while len(burned) < len(graph):
			print tour

			if not tour:
				tour = [node[cnt]]
				cnt += 1
			
			t, edge = next_node(graph,tour, burned, skip)

			#if t == -1:
			#	tour.pop()
			#	skip = burned.pop()
			#else:
			#	tour.append(t)
			#	burned.append(edge)
			tour.append(t)
			burned.append(edge)
		if None not in tour:
			return tour
		else:

			print tour
			return None

def next_node(graph,tour,burned,skip):

	current = tour[-1]

	for edge in graph:
		if edge[1] == current and not get_burned(edge,burned) and not is_previous(edge, skip):
			return edge[0], edge

		if edge[0] == current and not get_burned(edge,burned) and not is_previous(edge, skip):
			return edge[1],edge

	return -1, ()

def get_burned(edge,burned):

	return edge in burned

def is_previous(edge, prev):

	if not prev:
		return False

	if edge == prev:
		return True

	if (edge[1],edge[0]) == prev:
		return True

	return False

def get_rem_degrees(graph, burned, node):

	deg = 0
	burn = 0

	for edge in graph:
		if edge[0] == node or edge[1] == node:
			deg += 1

	for edge in burned:
			if edge[0] == node or edge[1] == node:
				burn += 1

	return deg-burn

def test():

	#graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]

	graph = [(1, 2), (2, 3), (3, 1)]

	print find_eulerian_tour(graph)

test()