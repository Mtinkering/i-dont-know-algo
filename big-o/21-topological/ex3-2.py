def dfs(key, graph, visited, result, visiting):
  visited.add(key)
  visiting.add(key)

  for v in graph[key]:
    if v in visiting:
      return False

    if v not in visited:
      if dfs(v, graph, visited, result, visiting) == False:
        return False

  result.append(key)
  visiting.remove(key)
  return True


def topologicalSort(graph, result):
  '''
    return true: possible
    return false: not possible
  '''
  visited = set()
  visiting = set()

  for i in range(len(graph)):
    if i not in visited:
      if dfs(i, graph, visited, result, visiting) == False:
        return False

  result.reverse()
  return True


def main():
  n = int(input())

  graph = [[] for i in range(26)]

  cur = input()
  for _ in range(1, n):
    nxt = input()

    i = 0
    j = 0
    while i < len(cur) and j < len(nxt) and cur[i] == nxt[j]:
      i += 1
      j += 1

    if i != len(cur) and j != len(nxt):
      graph[ord(cur[i]) - ord('a')].append(ord(nxt[j]) - ord('a'))
      cur = nxt

    # If i is not the end, but j is the end, meaning nn and n
    elif i != len(cur) and j == len(nxt):
      print('Impossible')
      return

  result = []

  if topologicalSort(graph, result):
    print(''.join(map(lambda x: chr(x + 97), result)))
  else:
    print('Impossible')


main()
