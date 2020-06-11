def inicializarSolucion(N):
    return [0] * N


def esFactible(solucion, fila, columna):
    factible = True
    i = 1
    while factible and i <= fila:
        factibleColumna = solucion[fila - i] != columna
        factibleDiag1 = solucion[fila - i] != columna - i
        factibleDiag2 = solucion[fila - i] != columna + i
        factible = factibleColumna and factibleDiag1 and factibleDiag2
        i += 1
    return factible


def NReinasVA(solucion, fila):
    N = len(solucion)
    if fila >= N:
        esSol = True
    else:
        esSol = False
        columna = 0
        while not esSol and columna < N:
            if esFactible(solucion, fila, columna):
                solucion[fila] = columna
                [solucion, esSol] = NReinasVA(solucion, fila + 1)
                if not esSol:
                    solucion[fila] = 0
            columna += 1
    return solucion, esSol


N, M = map(int,input().strip().split())
posiciones=[]
if M>0:
    posiciones = list(map(int, input().strip().split()))
solucion = inicializarSolucion(N)
for i, pos in enumerate(posiciones):
    solucion[i] = pos

[solucion, exito] = NReinasVA(solucion, M)

if exito:
    print('ADELANTE')
else:
    print('VUELVE A EMPEZAR')
