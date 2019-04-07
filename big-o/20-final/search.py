arr[integers]

smallest positive number that does not exist in the array


arr = [-5, 9, -7, 1]

[1, 2, 3] = > 4

ans = 1


minVal = min(arr)
maxval = max


arr = > set of numbers
if minVal < 0:
  from 1 -> increase until it''s not in the set, and positive

[1, 2, 3, 4, 5, 6, 7, 10, 8, 9] = > a set
time: O(N)
space: O(N)


time O(N)
space O(1)

arr = [0, 9, 0, 2, 1]  # cant sort
3 positive numbers

[-5, 8, 9, 10]
[1, maxVal + 1]


arr = [-5, 9, -7, 5]


[1, N + 1]
# . [1-4]
# arr = [0,0,0,0]
# ans = max(arr) + 1


# [3, 5, 4] [1-3]
arr = [0, 2, 3]

arr = [0, -2, -3]

# arr [integers]

# smallest positive number that does not exist in the array


# arr = [-5, 9, -7, 1]

# [1,2,3] => 4

# ans = 1


# minVal = min(arr)
# maxval = max


# arr => set of numbers
# if minVal < 0: from 1 -> increase until it''s not in the set, and positive

# [1,2,3,4,5,6,7,10,8,9] => a set
# time: O(N)
# space: O(N)


# time O(N)
# space O(1)

# arr = [0, 9, 0, 2, 1] # cant sort
# 3 positive numbers

# [ -5,8,9,10]
# [1, maxVal + 1]


arr = [-5, 9, -7, 5]
arr = [1, 1, 1]
arr = [1, 2, 3, 4, 5, 6, 7, 10, 8, 9]

# [1, N + 1]
# arr = [0,][3, 5, 4]


class Solution:
  def firstMissingPositive(self, arr: List[int]) -> int:
    n = len(arr)

    for i in range(n):
      if arr[i] < 1 or arr[i] > n:
        arr[i] = 0

    for i in range(n):
      index = arr[i] - 1
      tmp = arr[index]

      while tmp != arr[i] and arr[i] != 0:
        arr[index] = arr[i]
        arr[i] = tmp
        index = arr[i] - 1
        tmp = arr[index]

    cnt = 1
    for i in range(n):
      if arr[i] != cnt:
        return cnt
      cnt += 1

    return cnt


print(main(arr))

https: // leetcode.com/problems/missing-number/

int Solution:: firstMissingPositive(vector < int > &A) {
    int n = A.size()
    for (int & x: A) {
        if (x <= 0 | | x > n) {
            x = 0
        }
    }

    for (int & x: A) {
        int y = x
        if (y > n) {
            y -= n + 1
        }
        if (y > 0) {
            if (A[y - 1] <= n) {
                A[y - 1] += n + 1
            }
        }
    }
    int res = n + 1
    for (int i=1
         i <= n
         + +i) {
        if (A[i - 1] <= n) {
            res = i
            break
        }
    }
    return res
}

[5, 3, 2, 1]

[true, true, false, false]
[0, 3, 2, 1]

[1, 2, 3, 0]
