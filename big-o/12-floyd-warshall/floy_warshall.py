def FloyWarshall(graph, dist):

  for i in range(n):
    for j in range(n):
      for k in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]


adjacency matrix
