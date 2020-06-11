def esFactible(lab, f, c):
    return f >= 0 and f < len(lab) and c >= 0 and c < len(lab[0]) and lab[f][c] == 0


def todasRecorridas(laberinto):
    todasRecorridas = True
    i = 0
    while i < len(laberinto) and todasRecorridas:
        j = 0
        while j < len(laberinto[0]) and todasRecorridas:
            if laberinto[i][j] == 0:
                todasRecorridas = False
            j+=1
        i += 1
    return todasRecorridas


def salirDelLaberinto(laberinto, f, c, k):
    if f == len(laberinto) - 1 and c == len(laberinto[0]) - 1 and todasRecorridas(laberinto):
        esSol = True
    else:
        esSol = False
        mov = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        i = 0
        while not esSol and i < len(mov):
            if esFactible(laberinto, f + mov[i][0], c + mov[i][1]):
                laberinto[f + mov[i][0]][c + mov[i][1]] = k
                [laberinto, esSol] = salirDelLaberinto(laberinto, f + mov[i][0], c + mov[i][1], k + 1)
                if not esSol:
                    laberinto[f + mov[i][0]][c + mov[i][1]] = 0
            i += 1
    return [laberinto, esSol]


N = int(input().strip())
laberinto = []
for i in range(N):
    fila = list(map(int, input().strip().split()))
    laberinto.append([])
    for j, estado in enumerate(fila):
        laberinto[i].append(estado)
Xini = 0
Yini = 0
paso = 1
laberinto[Xini][Yini] = paso
[laberinto, esSol] = salirDelLaberinto(laberinto, Xini, Yini, paso + 1)

if esSol:
    print('SI')
else:
    print('NO')