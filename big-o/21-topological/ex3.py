def dfs(key, graph, visited, result, visiting):
  # print(graph)
  visited.add(key)
  visiting.add(key)

  if key in graph:
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

  for key in graph.keys():
    if key not in visited:
      if dfs(key, graph, visited, result, visiting) == False:
        return False

  result.reverse()
  return True


def main():
  n = int(input())

  graph = {}

  cur = input()
  for _ in range(1, n):
    nxt = input()

    i = 0
    j = 0
    while i < len(cur) and j < len(nxt) and cur[i] == nxt[j]:
      i += 1
      j += 1

    if i != len(cur) and j != len(nxt):
      if cur[i] not in graph:
        graph[cur[i]] = []

      graph[cur[i]].append(nxt[j])
      cur = nxt

    # If i is not the end, but j is the end, meaning nn and n
    elif i != len(cur) and j == len(nxt):
      print('Impossible')
      return

  result = []
  if topologicalSort(graph, result):
    a = ord('a')
    ans = []
    resultSet = set(result)
    for i in range(26):
      # In the result set but not the first one
      if chr(a+i) in resultSet:
        if result[0] == chr(a+i):
          ans.extend(result)
      else:
        ans.append(chr(a+i))

    print(''.join(ans))

  else:
    print('Impossible')


main()
