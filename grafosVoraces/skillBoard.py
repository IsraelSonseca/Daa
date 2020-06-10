from random import randint



def selectMin(shortest_edges, visited):
    vertex = None
    weight = float('inf')
    for i in range(1, len(shortest_edges)):
        if not visited[i] and shortest_edges[i] < weight:
            vertex = i
            weight = shortest_edges[i]
    return (vertex, weight)


def prim(graph):
    initial = 1
    visited = [False] * len(graph)
    mst = 0
    visited[initial] = True
    shortest_edges = [float('inf')] * len(graph)
    for start, end, weight in graph[initial]:
        shortest_edges[end] = weight
    for i in range(2, len(graph)):
        nextNode, cost = selectMin(shortest_edges, visited)
        if cost < float('inf'):
            visited[nextNode] = True
            mst += cost
            for edge in graph[nextNode]:
                start, end, weight = edge
                if not visited[end]:
                    shortest_edges[end] = min(shortest_edges[end], weight)
    return mst

N, M = map(int, input().strip().split())
grafo=[]
for i in range(N+1):
    grafo.append([])
for i in range(M):
    x, y, z = map(int, input().strip().split())
    grafo[x].append((x, y, z))
    grafo[y].append((y, x, z))

print(prim(grafo))
