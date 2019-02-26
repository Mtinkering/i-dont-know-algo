# https: // leetcode.com/problems/course-schedule/


class Solution:
  def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
    def dfs(src, courses, visited, cluster):
      if visited[src] == True:
        return
      visited[src] = True
      cluster.add(src)

      for node in courses[src]:
        if node in cluster:
          return False

        if dfs(node, courses, visited, cluster) == False:
          return False

      # Smart idea here is to add and remove the src in one DFS
      cluster.remove(src)
      return True

    courses = [[] for i in range(numCourses)]
    visited = [False for i in range(numCourses)]
    for u, v in prerequisites:
      courses[u].append(v)

    for i in range(numCourses):
      if visited[i] == False:
        if dfs(i, courses, visited, set()) == False:
          return False

    return True
