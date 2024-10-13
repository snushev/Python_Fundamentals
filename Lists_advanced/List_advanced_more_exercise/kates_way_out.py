from collections import deque

# Input number of rows
n = int(input())

# Input the maze as a list of lists
maze = [list(input().strip()) for _ in range(n)]

# Find Kate's starting position
start_row = start_col = -1
for r in range(n):
    for c in range(len(maze[r])):
        if maze[r][c] == 'k':
            start_row, start_col = r, c
            break
    if start_row != -1:
        break

# BFS setup
queue = deque([(start_row, start_col, 0)])  # (row, col, moves)
visited = [[False for _ in range(len(maze[0]))] for _ in range(n)]
visited[start_row][start_col] = True

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
exit_distances = []

# BFS to explore all possible paths
while queue:
    row, col, moves = queue.popleft()

    # Check if Kate is on the boundary (i.e., she can escape)
    if (row == 0 or row == n - 1 or col == 0 or col == len(maze[0]) - 1) and (maze[row][col] != 'k'):
        exit_distances.append(moves + 1)  # Record the distance to this exit

    # Explore all 4 directions
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < n and 0 <= new_col < len(maze[0]) and not visited[new_row][new_col]:
            if maze[new_row][new_col] in [' ', 'k']:  # Move to empty spaces or start position
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, moves + 1))

# Check if any exits were found
if exit_distances:
    max_moves = max(exit_distances)  # Get the maximum moves to an exit
    print(f"Kate got out in {max_moves} moves")
else:
    print("Kate cannot get out")
