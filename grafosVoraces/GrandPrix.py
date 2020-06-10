def select_min(distances, visit):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distances)):
        if not visit[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index


# Complexity: O(V^2)
def dijkstra(origin, graph):
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

    return distances

N, M, T=map(int, input().strip().split())
g = []
for i in range(N):
    g.append([])
for i in range(M):
    h1, h2, d=map(int, input().strip().split())
    g[h1].append((h1, h2, d))
    g[h2].append((h2, h1, d))

distancias = dijkstra(0, g)
distancias.sort()
i=0
n=len(distancias)
tiempoUtilizado=0
for dis in distancias:
    i+=1
    tiempoUtilizado+=dis
if tiempoUtilizado>T:
    print('Somos un fraude')
else:
    print(tiempoUtilizado)