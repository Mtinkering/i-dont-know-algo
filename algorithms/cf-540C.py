'''
' Steven June 19 2018
' http://codeforces.com/contest/540/problem/C
' BFS
'''
n, m = map(int, input().split())

arr = [None]*n

for i in range(n):
  arr[i] = list(input())

r1, c1 = map(lambda x: int(x) - 1, input().split())
r2, c2 = map(lambda x: int(x) - 1, input().split())

def bfs(maze, x, y, r2, c2):
  q = [(x, y)]

  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  while len(q) != 0:
    nextLevel = []

    for x, y in q:
      for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        # Crack the ice that went through
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == '.':
          maze[new_x][new_y] = 'X'
          nextLevel.append((new_x, new_y))
        
        # If there is a way to go to it and it's cracking, it's the answer
        elif new_x == r2 and new_y == c2 and maze[new_x][new_y] == 'X':
            return True

    q = nextLevel
  return False


answer = bfs(arr, r1, c1, r2, c2)

print('YES' if answer == True else 'NO')
