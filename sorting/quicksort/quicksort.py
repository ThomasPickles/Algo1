import math

def getArray():
	data = []
	with open("coursera_wk2_integers.txt",'r') as file:
		for line in file:
			data.append(int(line.strip()))
	return data
	
	
#myArray = [5,6,7,2,10,15,35,44,11,34,3,4,9,8,1]
numberOfComparisons = 0

def partitionArray(A, l, r):
	global numberOfComparisons 
	numberOfComparisons += r-l-1
	p = A[l] # take first element as pivot.  If doing something clever, we've already swapped pivot to here
	i = l+1 # boundary between partitions
	for j in range(l+1,r):
		if (A[j] < p):
			A[j], A[i] = A[i], A[j] # swap elements
			i+=1 # partition boundary moves along
	A[l], A[i-1] = A[i-1], A[l] # pivot in its rightful place just to left of boundary
	return i-1

def quickSort(A,l,r, pivot="first"):    
	if(r-l <= 1):
    # base case - nothing to do
		return A
	else:
	# partition array
		if(pivot == "last"):
			A[l], A[r-1] = A[r-1], A[l]
		if(pivot == "median"):
			mid = math.floor((l+r-1)/2)
			pivots = [A[l], A[mid], A[r-1]] # median of three
			median = sorted(pivots)[1] # using native list.sort() method, but not in place
			if (median == pivots[1]):
				A[l], A[mid] = A[mid], A[l]
			if (median == pivots[2]):
				A[l], A[r-1] = A[r-1], A[l]			
		boundary = partitionArray(A,l,r)
    # recurse on left half
		quickSort(A,l,boundary, pivot)
    # recurse on right half 
		quickSort(A,boundary+1,r, pivot)
	return A
  
def run(mode):
	array = getArray()
	quickSort(array,0,len(array),mode)
	print(numberOfComparisons)

if __name__ == "__main__":
	import sys
	run(sys.argv[1])
	



