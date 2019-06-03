# Backtracking: implicit tree
# Visit step by step


def R_solve_maze_helper(maze, start, finish, visited, path):
  if start == finish:
    path.insert(0, start)
    return True

  visited.add(start)
  for neighbor in maze[start]:
    if neighbor not in visited:
      # Found a path among all the neighbors
      if R_solve_maze_helper(maze, neighbor, finish, visited, path):
        path.insert(0, start)
        return True
  return False


def R_solve_maze(maze, start, finish):
  # Backtracking recursion
  visited = set()
  solution_path = []
  R_solve_maze_helper(maze, start, finish, visited, solution_path)
  return solution_path
