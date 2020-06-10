from collections import deque


def bfsAux(g, visited, v):
    q = deque()
    visited[v] = True
    print(v, end=" ")
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                print(adj, end=" ")
                q.append(adj)


def bfs(g):
    n = len(g)
    visited = [False] * n
    for v in range(1, n):
        if not visited[v]:
            bfsAux(g, visited, v)





N, M= map(int, input().strip().split())
g=[]
maximoA=[]
posiblesRaices=set()
for i in range(N):
    g.append([])
    maximoA.append([])
    posiblesRaices.add(i)
for i in range(M):
    a, b, c = map(int, input().strip().split())
    g[a].append((b, c))
    posiblesRaices.remove(b)


largestDistance=0


def bfsGreatestDistance(g, i):
    pass
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

for i in posiblesRaices:
    longestFromI=bfsGreatestDistance(g,i)
    if longestFromI>largestDistance:
        largestDistance=longestFromI
print (largestDistance)