
def neighbors(self, u):
	res = []
	for i in range(4):
		s1 = u[0:i] + str((int(u[i])+1) % 10) + u[i+1:]
		res.append(s1)

		s2 = u[0:i] + str((int(u[i])-1) % 10) + u[i+1:]
		res.append(s2)
	return res


def openLock(self, deadends, target):
	front = set()
	back = set()
	visited = set()
	start = '0000'

	for deadend in deadends:
		if deadend == start:
			return -1
		visited.add(deadend)

	front.add(start)
	back.add(target)

	if start == target:
		return 0

	length = 0

	while len(front) != 0:
		nextToVisit = set()

		for item in front:
			if item in back:
				print(item)
				return length
			if item not in visited:
				visited.add(item)

				directions = neighbors(1, item)

				for direction in directions:
					if direction not in visited:
						nextToVisit.add(direction)

		front = nextToVisit

		#Optimize
		if len(front) > len(back):
			front, back = back, front
		print('front', len(front))
		print('back', len(back))
		length += 1

	return -1


# print(openLock(1, ["0000"], "0009"))
# print(openLock(1, ["0001"], "0000"))
# print(openLock(1, ["8888"], "0009"))
print(openLock(1, ["0201", "0101", "0102", "1212", "2002"], "0202"))
# print(openLock(1, ["8887", "8889", "8878", "8898",
#                    "8788", "8988", "7888", "9888"], "8888"))
