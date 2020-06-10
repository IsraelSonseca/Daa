from collections import deque

def bfsAux(g, greatWAY, v):
    q = deque()
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if greatWAY[adj[0]]< greatWAY[aux]+adj[1]:
                greatWAY[adj[0]]=greatWAY[aux]+adj[1]
            q.append(adj[0])

def bfsGreatestDistance(g, i):
    n = len(g)
    greatWay = [0] * n
    bfsAux(g, greatWay, i)
    return max(greatWay)

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
    if b in posiblesRaices:
        posiblesRaices.remove(b)


largestDistance=0




for i in posiblesRaices:
    longestFromI=bfsGreatestDistance(g,i)
    if longestFromI>largestDistance:
        largestDistance=longestFromI
print (largestDistance)