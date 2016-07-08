# Intro to Algorithms 
# Lesson 2 Clique Graphs Quiz

# How many edges in a complete graph on n nodes?

# my initial solution
# (n-1)!
def clique(n):
	m = 0
	while n > 0:
		m += n-1
		n -= 1
	return m

# Provided solution
# n*(n-1)/2
def cliqueAns(n):
	return n*(n-1)/2

# Test case
for x in range(1000):
	if clique(x) <> cliqueAns(x):
		print 'False: ', clique(x), ' ', cliqueAns(x)
		
# interesting that these two algorithms both work despite have different mathematic formulae