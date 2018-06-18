n = int(raw_input())

M = []
for line in range(n):
	row = map(int, list(raw_input()))
	M.append(row)

X = []
if n > 2:

	for i in range(1,n-1):
		for j in range(1,n-1):
			a = M[i][j]
			if (a > M[i][j-1] and a > M[i][j+1] and a > M[i-1][j] and a > M[i+1][j]):
				X.append([i,j])				
for i in X:
	M[i[0]][i[1]] = "X"

string = ""
for i in range(n):
	print "".join(map(str,M[i]))
