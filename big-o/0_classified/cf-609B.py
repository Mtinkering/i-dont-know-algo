n, m = map(int, input().split())

books = list(map(int, input().split()))

cBooks = [0]*m

for book in books:
  cBooks[book-1] += 1

answer = 0

for i in range(m):
  for j in range(i+1, m, 1):
    answer += cBooks[i]*cBooks[j]


print(answer)
