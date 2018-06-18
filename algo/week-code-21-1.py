# x1,v1,x2,v2 = raw_input().strip().split(' ')
# x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]




# answer = ''
# if (v1 <= v2):
# 	answer = 'NO'
# else:
# 	remainder = (x2 - x1)%(v1-v2)
# 	if (remainder == 0):
# 		answer = 'YES'
# 	else:
# 		answer = 'NO'

# print answer

totalLuck = 0
importantTest = []
N, K = [int(x) for x in raw_input().split()]
for i in range(N):
	L, T = [int(x) for x in raw_input().split()]

	if (T == 0):
		totalLuck += L
	else:
		importantTest.append(L)
importantTest = sorted(importantTest, reverse=True)
totalLuck = totalLuck + sum(importantTest[:K]) - sum(importantTest[K:])



print totalLuck