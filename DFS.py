# DFS

def DFS(graph, start):
    stack = [start]
    visited = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for i in graph[vertex]:
                stack.append(i)
    print(visited)
    
def main():
    graph = {'A': ['S', 'B', 'C'], 'S': ['E','B','A'], 'B': ['S','A','D'], 'D': ['C','B'], 'C': ['A','D'], 'E': ['S']} # graph represented as dictionary
    
    DFS(graph, 'E')
    
if __name__ == "__main__":
    main()