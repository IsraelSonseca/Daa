def esFactible(lab, f, c):
    return f >= 0 and f < len(lab) and c >= 0 and c < len(lab[0]) and lab[f][c] == -1





def llegarAdestino(laberinto, f, c, Xdes, Ydes, k,movimientos,mejorRespuesta):
    if f == Xdes and c == Ydes:
        mejorRespuesta=min(k,mejorRespuesta)
    else:
        for i in range(len(movimientos)):
            if k < mejorRespuesta:
                if esFactible(laberinto, f + movimientos[i][0], c + movimientos[i][1]):
                    laberinto[f + movimientos[i][0]][c + movimientos[i][1]] = k+1
                    mejorRespuesta = llegarAdestino(laberinto, f + movimientos[i][0], c + movimientos[i][1], Xdes, Ydes, k + 1,movimientos,mejorRespuesta)
                    laberinto[f + movimientos[i][0]][c + movimientos[i][1]] = 0
    return mejorRespuesta


Xini, Yini = map(int, input().strip().split())
Xdes, Ydes = map(int, input().strip().split())
laberinto = []
N=5
for i in range(N):
    laberinto.append([])
    for _ in range(N):
        laberinto[i].append(-1)


paso = 0
laberinto[Xini][Yini] = paso
movimientos=[(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
mejorRespuesta=10000
mejorRespuesta = llegarAdestino(laberinto, Xini, Yini, Xdes, Ydes, paso,movimientos,mejorRespuesta)
print(mejorRespuesta)