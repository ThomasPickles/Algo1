import random, math, timeit, csv

def readFile():
	"""Converts the TSV file provided by Coursera into a list of edges"""
	nodeList = []
	with open('kargerMinCut.txt','r') as f:
		reader=csv.reader(f,delimiter='\t')
		for row in reader:
			if row:
				idx = int(row[0])-1
				# i<j to prevent double counting of edges
				nodeList.extend([[idx,int(nd)-1] for nd in row[1:] if nd and int(nd)-1 > idx])
	return nodeList


#edgeList = [[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[4,5]]

def contractEdge(edgeList):
	"""Returns a new edge list where a random edge has been contracted"""
	flatList = [i for edge in edgeList for i in edge]
	ndNew = max(flatList)+1
	selEdge = random.choice(edgeList)
	return [[nd1 if nd1 not in selEdge else ndNew, nd2 if nd2 not in selEdge else ndNew] for nd1,nd2 in edgeList if not (nd1 in selEdge and nd2 in selEdge)]

def getCut(edgeList):
	"""Returns a cut of the graph - the remaining edges after only two nodes of the graph remain"""
	numDistinctEdges = len(set([i for edge in edgeList for i in edge]))
	for edgeCount in range(numDistinctEdges,2,-1):
		edgeList = contractEdge(edgeList)
	return edgeList

def run(iterations=1):
	"""Returns the smallest cut from the runs"""
	edgeList = readFile()
	minCut = math.inf
	for i in range(iterations):
		thisCut = len(getCut(edgeList))
		print(thisCut)
		minCut = min(minCut, thisCut)
	print("MinCut is ", minCut)

run(10)
