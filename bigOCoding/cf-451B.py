n = int(input())
arr = list(map(int, input().split()))

inSegment = False
start = 0
end = 0
answer = 'yes'

for i in range(1, n, 1):
  if (arr[i] < arr[i - 1] and not inSegment):
    start = i - 1
    inSegment = True

  if (arr[i] > arr[i - 1] and inSegment):
    end = i - 1
    break

  # special case
  # 3 2 1
  if (i == n - 1 and inSegment):
    end = n - 1

# reverse start and end inclusive
# for i in range(start, end, 1):
#   if (i > (end + start)//2):
#     break
#   arr[i], arr[start + end - i] = arr[start + end - i], arr[i]
# arr[start:end+1] = sorted(arr[start:end+1])

arr[start:end+1] = arr[end:start-1:-1])

#Check if the whole array is sorted
for i in range(1, n, 1):
  if (arr[i] < arr[i - 1]):
    answer = 'no'
    break

print(answer)
if (answer == 'yes'):
  print(start + 1, end + 1)
