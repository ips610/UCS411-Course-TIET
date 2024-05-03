def up(state):
    new_state = [row[:] for row in state]
    blank_row, blank_col = find_blank(new_state)
    if blank_row > 0:
        new_state[blank_row][blank_col], new_state[blank_row - 1][blank_col] = new_state[blank_row - 1][blank_col], new_state[blank_row][blank_col]
        return new_state
    else:
        return None

def down(state):
    new_state = [row[:] for row in state]
    blank_row, blank_col = find_blank(new_state)
    if blank_row < 2:
        new_state[blank_row][blank_col], new_state[blank_row + 1][blank_col] = new_state[blank_row + 1][blank_col], new_state[blank_row][blank_col]
        return new_state
    else:
        return None

def left(state):
    new_state = [row[:] for row in state]
    blank_row, blank_col = find_blank(new_state)
    if blank_col > 0:
        new_state[blank_row][blank_col], new_state[blank_row][blank_col - 1] = new_state[blank_row][blank_col - 1], new_state[blank_row][blank_col]
        return new_state
    else:
        return None

def right(state):
    new_state = [row[:] for row in state]
    blank_row, blank_col = find_blank(new_state)
    if blank_col < 2:
        new_state[blank_row][blank_col], new_state[blank_row][blank_col + 1] = new_state[blank_row][blank_col + 1], new_state[blank_row][blank_col]
        return new_state
    else:
        return None

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal_state(state, goal_state):
    return state == goal_state

# Function to calculate the cost (number of misplaced tiles)
def cost(state, goal_state):
    cost = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                cost += 1
    return cost

def solve(start_state, goal_state):
    lets_start = [(start_state, [])]
    explored = set()
    print(f'Initial state: {start_state}')
    print(f'Goal state: {goal_state}')
    while lets_start:
        state, path = lets_start.pop(0)
        current_cost = cost(state, goal_state)
        print(f'Current state: {state}')
        print(f'Current path: {path}')
        print(f'Cost: {current_cost}')
        if is_goal_state(state, goal_state):
            return path
        explored.add(tuple(map(tuple, state)))
        for action in [up, down, left, right]:
            new_state = action(state)
            if new_state and tuple(map(tuple, new_state)) not in explored:
                lets_start.append((new_state, path + [action.__name__]))
    return None

start_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
goal_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
solution = solve(start_state, goal_state)
if solution:
    print("Solution found in", len(solution), "steps:", solution)
else:
    print("No solution found.")
