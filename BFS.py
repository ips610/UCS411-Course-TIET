# BFS

def BFS(graph, start):
    queue = [start]
    visited = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            for i in graph[vertex]:
                queue.append(i)
    print(visited)
    
def main():
    graph = {'A': ['S', 'B', 'C'], 'S': ['E','B','A'], 'B': ['S','A','D'], 'D': ['C','B'], 'C': ['A','D'], 'E': ['S']} # graph represented as dictionary
    
    BFS(graph, 'A')
    
if __name__ == "__main__":
    main()