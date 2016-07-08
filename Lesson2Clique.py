# Intro to Algorithms 
# Lesson 2 Clique Graphs Quiz

# How many edges in a complete graph on n nodes?

def clique(n):
	m = 0
	while n > 0:
		m += n-1
		n -= 1
	return m
	
print clique(5)