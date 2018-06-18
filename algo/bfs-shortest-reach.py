T = int(raw_input())

def walk_the_nodes(s,V,U):
	next_node = [s]
	# level = {s:0}
	L=[-1 for _ in range(n+1)]
	L[s]=0
	i = 6
	print V
	while len(next_node) > 0:

		for node in next_node:
			next_node = []
			if node not in V: continue
			for v in V[node]:

				if v not in L:
					L[v] = i
					next_node.append(v)
		i +=  6
	distance = []
	for j in U:
		if (j in L):
			distance.append(L[j])
		else:
			distance.append(-1)
	for d in distance:

		if (d != 0): print d,
	print

for test in range(T)[:1]:
	U,M = [int(x) for x in raw_input().split()]
	V = {}
	for i in range(M):
		a,b = [int(x) for x in raw_input().split()]
	if a not in V:
			V[a] = []
		if b not in V:
			V[b] = []
		if b not in V[a]: V[a].append(b)
		if a not in V[b]: V[b].append(a)
	s = int(raw_input())

	walk_the_nodes(s,V,list(range(1,U+1)))





# import sys

# def solve(n,r,s):
# 	G=[[] for _ in range(n+1)]
# 	for [i,j] in r:
# 		if not((i in G[j]) | (i==j)):
# 			G[i].append(j)
# 			G[j].append(i)
# 	done=[]
# 	ndone=[s]
# 	todo=G[s]
# 	L=[-1 for _ in range(n+1)]
# 	L[s]=0
# 	for i in G[s]:
# 		L[i]=1
# 	while ndone!=done:
# 		done=list(ndone)
# 		ntodo=[]
# 		for i in todo:
# 			for j in G[i]:
# 				if not((j in done) | ((j in ntodo) | (j in todo))):
# 					L[j]=L[i]+1
# 					ntodo.append(j)
# 		ndone+=list(todo)
# 		todo=list(ntodo)
# 	st=""
# 	for i in (L[1:s]+L[s+1:]):
# 		if i!=-1:
# 			st+=str(6*i)+" "
# 		else:
# 			st+=str(i)+" "
# 	return st





# T=int(raw_input())
# for _ in range(T):
#     [n,m]=map(int,raw_input().strip().split())
#     r=[]
#     for _ in range(m):
#         r.append(map(int,raw_input().strip().split()))
#     s=int(raw_input())
#     print(solve(n,r,s))