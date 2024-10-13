# Define the maze
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Define directions: North, East, South, West
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_names = ['North', 'East', 'South', 'West']

def solve_maze(maze, start, end):
    stack = [(start, [])]
    visited = set()
    
    print(f"Start at ( {start[0]} , {start[1]} )")
    
    while stack:
        (current_x, current_y), path = stack.pop()
        current = (current_x, current_y)
        
        if current == end:
            print(f"{' '.join(path)} Leaving at ( {current_x} , {current_y} )")
            return True
        
        if current in visited:
            continue
        
        visited.add(current)
        
        neighbors = []
        for i, (dx, dy) in enumerate(directions):
            next_x, next_y = current_x + dx, current_y + dy
            if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == 0 and (next_x, next_y) not in visited:
                neighbors.append((i, (next_x, next_y)))
        
        if not neighbors:
            print(f"{' '.join(path)} Stuck at ( {current_x} , {current_y} )")
            if stack:
                back_x, back_y = stack[-1][0]
                print(f"Back to ( {back_x} , {back_y} )")
        else:
            for i, (next_x, next_y) in reversed(neighbors):
                new_path = path + [direction_names[i]]
                stack.append(((next_x, next_y), new_path))
    
    return False

# Solve the maze
start = (2, 0)
end = (11, 13)
solve_maze(maze, start, end)