from collections import deque

def bfsAux(g, visited, v):
    q = deque()
    visited[v] = True
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)


def bfsNumCompConexas(g):
    nComConexa=0
    n = len(g)
    visited = [False] * n
    for v in range(0,n):
        if not visited[v]:
            nComConexa+=1
            bfsAux(g, visited, v)
    return nComConexa


n,m=map(int,input().strip().split())
g=[]
for i in range(n):
    g.append([])
for i in range(m):
    a, b = map(int, input().strip().split())
    g[a].append(b)
    g[b].append(a)

print(bfsNumCompConexas(g))
