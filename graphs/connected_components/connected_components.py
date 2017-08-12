import sys
from collections import defaultdict

def getGraph(file):
	edges = defaultdict(list)
	with open(file) as f:
		for line in f.readlines():
			src, trg = int(line.split()[0])-1, int(line.split()[1])-1
			edges[src].append(trg)
	print("Edge dictionary created with ", len(edges), " vertices with outgoing edges")
	return edges

if __name__ == "__main__":
	getGraph(sys.argv[1])
