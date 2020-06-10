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

n, m = map(int, input().strip().split())
g = []
costeRefuerzo = []
candidatos = set()
criticos = set()
for i in range(n):
    valor = input().strip()
    costeRefuerzo.append(valor)
    candidatos.add(i)
    g.append([])

for i in range(m):
    a, b = map(int, input().strip().split())
    g[a].append(b)
    g[b].append(a)


def eliminarNodoi(grafoSin_i, g, i):
    for indice, nodo in enumerate(g):
        grafoSin_i.append([])
        if not i == indice:
            for ady in nodo:
                if not ady == i:
                    grafoSin_i[indice].append(ady)


for i in range(n):
    grafoSin_i = []
    eliminarNodoi(grafoSin_i, g, i)
    if bfsNumCompConexas(grafoSin_i) > 2:
        criticos.add(i)
costeReforzarNodosCriticos = 0
for i in criticos:
    costeReforzarNodosCriticos += int(costeRefuerzo[i])
print(costeReforzarNodosCriticos)
