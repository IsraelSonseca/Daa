def select_min(distances, visit):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distances)):
        if not visit[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index


# Complexity: O(V^2)
def dijkstra(origin, destination, graph):
    # distances from origin to all other
    distances = [float('inf')] * len(graph)
    visit = [False] * len(graph)

    distances[origin] = 0
    visit[origin] = True
    for start, end, weight in graph[origin]:
        distances[end] = weight

    for i in range(2, len(graph)):
        next_node = select_min(distances, visit)
        visit[next_node] = True
        for start, end, weight in graph[next_node]:
            distances[end] = min(distances[end], distances[start] + weight)

    return distances[destination]


T, O, P = map(int, input().strip().split())
N, M = map(int, input().strip().split())
grafo = []
for i in range(N+1):
    grafo.append([])
atenuaciones = list(map(int, input().strip().split()))
for i in range(M):
    a, b = map(int, input().strip().split())
    grafo[a].append((a, b, atenuaciones[b-1]))
    grafo[b].append((b, a, atenuaciones[a-1]))

dolorCausado=P + atenuaciones[O-1] - dijkstra(T, O, grafo)
if dolorCausado<0:
    print(0)
else:
    print(dolorCausado)