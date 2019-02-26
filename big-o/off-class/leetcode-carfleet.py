

def carFleet(self, target, position, speed):
  """
  :type target: int
  :type position: List[int]
  :type speed: List[int]
  :rtype: int
  """
  cars = sorted(zip(position, speed), reverse=True)

  counter = 0
  previous = 0
  current = 0

  for p, s in cars:
    current = (target - p)*1.0/s

    # Need more time to arrive
    if current > previous:
      counter += 1
      previous = current

  return counter


def carFleet2(self, target, pos, speed):
  # print(sorted(zip(pos, speed)))
  time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
  res = cur = 0
  # print(time)
  for t in time[::-1]:
    if t > cur:
      res += 1
      cur = t
  return res


print(carFleet(1, 12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
print(carFleet2(1, 12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
print(carFleet(1, 10, [8, 3, 7, 4, 6, 5], [4, 4, 4, 4, 4, 4]))
print(carFleet2(1, 10, [8, 3, 7, 4, 6, 5], [4, 4, 4, 4, 4, 4]))
print(carFleet(1, 10, [2, 4], [3, 2]))
print(carFleet2(1, 10, [2, 4], [3, 2]))
print(carFleet(1, 20, [6, 2, 17], [3, 9, 2]))
print(carFleet2(1, 20, [6, 2, 17], [3, 9, 2]))
print(carFleet(1, 31, [5, 26, 18, 25, 29, 21, 22, 12, 19, 6], [7, 6, 6, 4, 3, 4, 9, 7, 6, 4]))
print(carFleet2(1, 31, [5, 26, 18, 25, 29, 21, 22, 12, 19, 6], [7, 6, 6, 4, 3, 4, 9, 7, 6, 4]))
print(carFleet(1, 31, [26, 29], [6, 3]))
print(carFleet2(1, 31, [26, 29], [6, 3]))
print(carFleet(1, 31, [0, 4, 2], [2, 1, 3]))
print(carFleet2(1, 31, [0, 4, 2], [2, 1, 3]))
