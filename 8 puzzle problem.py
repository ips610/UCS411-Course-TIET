# 8 puzzle problem
import copy

def find_blank_tile(problem_state):
    for i in range(3):
        for j in range(3):
            if problem_state[i][j] == 0:
                return i, j
            

def cost(initial_state, final_state):
    cost = 0
    for i in range(3):
        for j in range(3):
            if initial_state[i][j] != final_state[i][j]:
                cost += 1
    return cost

def printing_state(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j], end=' ')
        print()
    print()
    

def move_up(problem_state, i, j):
    if i == 0:
        return problem_state
    else:
        new_state = copy.deepcopy(problem_state)
        new_state[i][j] = new_state[i-1][j]
        new_state[i-1][j] = 0
        return new_state

def move_down(problem_state, i, j):
    if i == 2:
        return problem_state
    else:
        new_state = copy.deepcopy(problem_state)
        new_state[i][j] = new_state[i+1][j]
        new_state[i+1][j] = 0
        return new_state
    
def move_left(problem_state, i, j):
    if j == 0:
        return problem_state
    else:
        new_state = copy.deepcopy(problem_state)
        new_state[i][j] = new_state[i][j-1]
        new_state[i][j-1] = 0
        return new_state
    
def move_right(problem_state, i, j):
    if j == 2:
        return problem_state
    else:
        new_state = copy.deepcopy(problem_state)
        new_state[i][j] = new_state[i][j+1]
        new_state[i][j+1] = 0
        return new_state
    

def main():
    
    initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    final_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
    intermediate_state = copy.deepcopy(initial_state)
    comparison = 0

    printing_state(initial_state)
    printing_state(final_state)
    print(f'Cost is: {cost(initial_state, final_state)}')

    while (cost(initial_state, final_state) != 0 and comparison < 100):
        i, j = find_blank_tile(intermediate_state)
        
        intermediate_state = move_up(intermediate_state, i, j)
        intermediate_state = move_down(intermediate_state, i, j)
        intermediate_state = move_left(intermediate_state, i, j)
        intermediate_state = move_right(intermediate_state, i, j)
        final_state = intermediate_state[:]
        comparison += 1
    
    if comparison == 100 and cost(initial_state, final_state) != 0:
        print('No solution')
    else:
        print(f'No of Comparisons: {comparison}')

if __name__ == "__main__":
    main()