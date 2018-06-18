N, K = [int(x) for x in raw_input().split()]
C  = sorted([int(x) for x in raw_input().split()], reverse=True)
cost = 0
x = 0
j = 0
for i in range(0,N):
	cost += (x+1)*C[i]
	j += 1
	if (j == K):
		j = 0
		x += 1

print cost



# code snippet illustrating input/output methods 
# N, K = raw_input().split()
# N = int(N)
# K = int(K)
# C = []

# numbers = raw_input()

# i = 0
# for number in numbers.split():
#    C.append( int(number) )
#    i = i+1

# result = 0
# print result
