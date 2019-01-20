class Solution:
  def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
      return []

    m = len(matrix)  # row
    n = len(matrix[0])  # col

    arr = []
    visited = [[False]*n for i in range(m)]
    i = 0
    j = 0
    arr.append(matrix[i][j])
    visited[i][j] = True
    while len(arr) != m*n:
      for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        while True:
          i += x
          j += y
          if 0 <= j < n and 0 <= i < m and visited[i][j] == False:
            arr.append(matrix[i][j])
            visited[i][j] = True
          else:
            break
        j -= y
        i -= x
    return arr


sol = Solution()
sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
