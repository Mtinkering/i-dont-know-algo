T = int(raw_input())


for times in range(T):
	N,M = [int(x) for x in raw_input().split()]
	X = [int(x) for x in raw_input().split()]

	D = [int(x) for x in raw_input().split()]

	# recursive version
	# cache = {}
	# def max_moves(position,M):
	# 	if (M == 0): return 0
	# 	pos = tuple(position)
	# 	if ((pos,M) in cache): return cache[(pos,M)]
	# 	possible_moves = 0
	# 	M -= 1
	# 	for i in range(N):
	# 		if (D[i] == 1): continue
	# 		elif (position[i] == 1):
	# 			newPosition = position[:]
	# 			newPosition[i] += 1
	# 			if (M == 0): possible_moves += 1
	# 			possible_moves += max_moves(newPosition,M)
				
	# 		elif (position[i] == D[i]):
	# 			newPosition = position[:]
	# 			newPosition[i] -= 1
	# 			if (M == 0): possible_moves += 1
	# 			possible_moves += max_moves(newPosition,M)
	# 		else:
				
	# 			newPosition1 = position[:]
	# 			newPosition2 = position[:]
	# 			newPosition1[i] += 1
	# 			newPosition2[i] -= 1
	# 			if (M == 0): possible_moves += 2
	# 			possible_moves += 	max_moves(newPosition1,M) + max_moves(newPosition2,M)
			
	# 	cache[(pos,M)] = possible_moves
	# 	return possible_moves
	# print max_moves(X,M)


	#bottom up
	# P = [[ ]]*(M+1)
	# def find_moves(array):
	# 	positions = []
	# 	for position in array:

	# 		for i in range(N):
	# 			if (D[i] == 1): continue
	# 			elif (position[i] == 1):
	# 				newPosition = position[:]
	# 				newPosition[i] += 1
	# 				positions.append(newPosition)
	# 			elif (position[i] == D[i]):
	# 				newPosition = position[:]
	# 				newPosition[i] -= 1
	# 				positions.append(newPosition)
	# 			else:
					
	# 				newPosition1 = position[:]
	# 				newPosition2 = position[:]
	# 				newPosition1[i] += 1
	# 				newPosition2[i] -= 1
	# 				positions.append(newPosition1)
	# 				positions.append(newPosition2)


	# 	return positions

	# P[0].append(X[:])
	# for i in range(1,M+1):
	# 	P[i] = find_moves(P[i-1])
	# 	P[i-1] = []
	# # print P
	# for i in P:
	# 	print i
	# print len(P[-1])
	# M =  2
	def find_moves(obj):
		newObj = {}
		for position in obj:
			# print position
			position_list = list(position)
			for i in range(N):
				if (D[i] == 1): continue
				elif (position[i] == 1):
					newPosition = position_list[:]
					newPosition[i] += 1
					newPosition_tuple = tuple(newPosition)
					if newPosition_tuple in newObj:
						newObj[newPosition_tuple] += 1
					else:
						newObj[newPosition_tuple] = 1
				elif (position[i] == D[i]):
					newPosition = position_list[:]
					newPosition[i] -= 1
					newPosition_tuple = tuple(newPosition)
					if newPosition_tuple in newObj:
						newObj[newPosition_tuple] += 1
					else:
						newObj[newPosition_tuple] = 1
				else:
					
					newPosition1 = position_list[:]
					newPosition2 = position_list[:]
					newPosition1[i] += 1
					newPosition2[i] -= 1
					newPosition1_tuple = tuple(newPosition1)
					newPosition2_tuple = tuple(newPosition2)

					if newPosition1_tuple in newObj:
						newObj[newPosition1_tuple] += 1
					else:
						newObj[newPosition1_tuple] = 1
					if newPosition2_tuple in newObj:
						newObj[newPosition2_tuple] += 1
					else:
						newObj[newPosition2_tuple] = 1


		return newObj

	S = {}
	S[tuple(X)] = 0
	# print S
	for i in range(1,M+1):
		S = find_moves(S)
		if (i == M): print sum([S[x] for x in S])
	# print S
	# for i in P:
		# print i
	# print len(P[-1])






