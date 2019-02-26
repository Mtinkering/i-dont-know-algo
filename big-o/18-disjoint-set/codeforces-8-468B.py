# class UnionFind:
#   def __init__(self, n):
#     # self.nums = nums
#     self.parent = [i for i in range(n)]
#     self.rank = [0 for i in range(n)]
#     self.setNumber = [-1 for i in range(n)]

#   def union(self, u, v):
#     up = self.find(u)
#     vp = self.find(v)

#     if up == vp:
#       return

#     if self.rank[up] == self.rank[vp]:
#       self.parent[up] = vp
#       self.rank[vp] += 1
#       self.setNumber[up] = self
#     elif self.rank[up] < self.rank[vp]:
#       self.parent[up] = vp
#     else:
#       self.parent[vp] = up

#   def find(self, u):
#     if u != self.parent[u]:
#       self.parent[u] = self.find(self.parent[u])

#     return self.parent[u]


# n, a, b = map(int, input().split())

# nums = list(map(int, input().split()))

# numToIndex = {}

# for i, num in enumerate(nums):
#   numToIndex[num] = i


# # numSet = set(nums)

# uf = UnionFind(n)

# for i, num in enumerate(nums):
#   complA = a - num
#   if complA in numToIndex:
#     uf.union(i, numToIndex[complA])

#   complB = b - num
#   if complB in numToIndex:
#     uf.union(i, numToIndex[complB])

# counter = 0
# for i in range(n):
#   if i == uf.find(i):
#     counter += 1

# if counter <= 2:
#   print('YES')
# else:
#   print('NO')
# # ans = []
# # for num in nums:
# #   if numToSet[num] != -1:
# #     ans.append(numToSet[num])
# #   else:
# #     break

# # if len(ans) != n:
# #   print(len(ans))
# #   print('NO')
# # else:
# #   print('YES')
# #   print(*ans)


# def find(u):
#     global par
#     if u != par[u]:
#         par[u] = find(par[u])
#     return par[u]


# def union(u, v):
#     u = find(u)
#     v = find(v)
#     par[u] = v


# n, a, b = map(int, input().split())
# p = list(map(int, input().split()))
# mp = dict()
# for i in range(n):
#     mp[p[i]] = i + 1
# par = [i for i in range(n + 2)]

# for i in range(n):
#     union(i + 1, mp.get(a - p[i], n + 1))
#     union(i + 1, mp.get(b - p[i], 0))

# A = find(0)
# B = find(n + 1)

# if A != B:
#     print('YES')
#     print(' '.join(['1' if find(i) == B else '0' for i in range(1, n + 1)]))
# else:
#     print('NO')

# # 6 11 10
# # 3 6 7 8 2 5

# # total 10: 3,7 . 8, 2
# # total 11: 6,5


# # total 11: 8,3 .  6,5
# # left out: 7 and 2
def find(u):
  global par
  if u != par[u]:
    par[u] = find(par[u])
  return par[u]


def union(u, v):
  u = find(u)
  v = find(v)
  par[u] = v


n, a, b = map(int, input().split())
p = list(map(int, input().split()))
mp = dict()
for i in range(n):
  mp[p[i]] = i + 1
par = [i for i in range(n + 2)]

for i in range(n):
  union(i + 1, mp.get(a - p[i], n + 1))
  union(i + 1, mp.get(b - p[i], 0))

A = find(0)
B = find(n + 1)
print(A)
print(B)
if A != B:
  print('YES')
  print(' '.join(['1' if find(i) == B else '0' for i in range(1, n + 1)]))
else:
  print('NO')
