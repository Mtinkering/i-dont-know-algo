# // UVA 429
# Word transform
# spice -> stock
# spice ->slice -> slick -> stick -> stock

import queue


def onlyOneCharDiff(source, word):
  if len(source) != len(word):
    return False

  diff = 0

  for i in range(len(source)):
    if source[i] != word[i]:
      diff += 1
  return diff == 1


# def getNeighbors(source, words):
#   # get the words that is only one character different
#   results = []

#   for word in words:
#     if onlyOneCharDiff(source, word):
#       results.append(word)

#   return results


def bfs(source, destination, graph):
  distance = {}
  q = queue.Queue()

  q.put(source)
  distance[source] = 0

  while not q.empty():
    first = q.get()

    if first == destination:
      return distance[first]
    for neighbor in graph.get(first, []):
      if neighbor not in distance:
        q.put(neighbor)
        distance[neighbor] = distance[first] + 1

  return distance.get(destination, None)
# https://www.udebug.com/UVa/429


def solve():
  words = []

  s = input()
  while s != '*':
    words.append(s)
    s = input()

  pairs = []

  temp = input().split()

  while len(temp) != 0:
    pairs.append((temp[0], temp[1]))

    try:
      temp = input().split()
    except EOFError:
      temp = []

  graph = {}
#   print(words)
  for index, word in enumerate(words):
    for index_neighbor in range(index):
      if onlyOneCharDiff(word, words[index_neighbor]):
        neighbor = words[index_neighbor]

        if word in graph:
          graph[word].append(neighbor)
        else:
          graph[word] = [neighbor]

        if neighbor in graph:
          graph[neighbor].append(word)
        else:
          graph[neighbor] = [word]

  for index, pair in enumerate(pairs):
    result = bfs(pair[0], pair[1], graph)
    print(pair[0], pair[1], result)


test = int(input())
input()

for t in range(test):
  solve()

  if (t < (test - 1)):
    print()
