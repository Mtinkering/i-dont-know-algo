import sys

def solve(n,r,s):
    print 
    G=[[] for _ in range(n+1)]
    for [i,j] in r:
        if not((i in G[j]) | (i==j)):
            G[i].append(j)
            G[j].append(i)
    done=[]
    ndone=[s]
    todo=G[s]
    print G
    L=[-1 for _ in range(n+1)]
    L[s]=0
    for i in G[s]:
        L[i]=1
    while ndone!=done:
        done=list(ndone)
        ntodo=[]
        for i in todo:
            for j in G[i]:
                if not((j in done) | ((j in ntodo) | (j in todo))):
                    L[j]=L[i]+1
                    ntodo.append(j)
        ndone+=list(todo)
        todo=list(ntodo)
    st=""
    for i in (L[1:s]+L[s+1:]):
        if i!=-1:
            st+=str(6*i)+" "
        else:
            st+=str(i)+" "
    return st





T=int(raw_input())
for _ in range(T)[:1]:
    [n,m]=map(int,raw_input().strip().split())
    r=[]
    for _ in range(m):
        r.append(map(int,raw_input().strip().split()))
    s=int(raw_input())
    print(solve(n,r,s))