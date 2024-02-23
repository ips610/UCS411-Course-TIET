def uniform_cost_search(graph, start, goal, cost = 0):

    if start[-1] == goal:
        return start
    
    all_path_cost = {}
    
    for i in graph[start[-1]]:
        path = start
        path += i
        cost += graph[start[-1]][i]
        path= uniform_cost_search(graph, path, goal, cost)
        # print(path, cost)
        all_path_cost[path] = cost
        path = start
        cost = 0
        
    print(all_path_cost)
def main():
    
    graph = {'S': {'A': 1, 'B': 5, 'C': 15}, 'A': {
    'G': 10}, 'B': {'G': 5}, 'C': {'G': 1}} # graph represented as dictionary
    
    uniform_cost_search(graph, 'S', 'G')
    

if __name__ == "__main__":
    main()