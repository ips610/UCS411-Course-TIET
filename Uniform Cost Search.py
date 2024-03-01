all_path_cost = {}


def uniform_cost_search(graph, start, goal, cost=0):
    if start[-1] == goal:
        all_path_cost[start] = cost
        return start, cost

    for i in graph[start[-1]]:
        new_path = start + i
        new_cost = cost + graph[start[-1]][i]
        returned_path, returned_cost = uniform_cost_search(
            graph, new_path, goal, new_cost)

    return start, cost


def optimal_path(graph):
    min_cost = min(all_path_cost.values())
    for path in all_path_cost:
        if all_path_cost[path] == min_cost:
            print(f"Optimal path: {path} with cost: {min_cost}")


def main():
    graph = {'S': {'A': 1, 'B': 5, 'C': 15}, 'A': {
        'G': 10}, 'B': {'G': 5}, 'C': {'G': 1}}

    uniform_cost_search(graph, 'S', 'G')
    print(all_path_cost)
    optimal_path(graph)


if __name__ == "__main__":
    main()
