import sys
import itertools
V = 4

def TSP(graph, source):
    vertex = []
    for i in range(V):
        if i!=source :
            vertex.append(i)
            
    min_path = sys.maxsize
    next_permutation = list(itertools.permutations(vertex))
    print(next_permutation)
    
    for i in next_permutation:
        current_pathweight = 0
        k = source
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][source]
        min_path = min(min_path, current_pathweight)
        
    return min_path



# Driver Code 
if __name__ == "__main__": 

	# matrix representation of graph 
	graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
			[15, 35, 0, 30], [20, 25, 30, 0]] 
	source = int(input("Enter Source Node: "))
	print(TSP(graph, source - 1))
