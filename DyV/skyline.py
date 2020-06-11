def merge(first, second, output):
    k = f = s = 0
    while f < len(first) and s < len(second):
        if first[f] <= second[s]:
            output[k] = first[f]
            f += 1
        else:
            output[k] = second[s]
            s += 1
        k += 1

    # if we run out of elements either in "first"
    # or "second" then we copy the remaining elements
    r = f if s == len(second) else s
    remaining = first if s == len(second) else second
    for i in range(r, len(remaining)):
        output[k] = remaining[i]
        k += 1


solucion = []
nEdificios = int(input().strip())
edificiosIni = []
edificiosFin = []
for i in range(nEdificios):
    left, high, right = map(int, input().strip().split())
    edificiosIni.append((left, high, right, i, 1))
    edificiosFin.append((right, high, left, i, 0))

edificios = edificiosIni + edificiosFin
edificios.sort()

edificiosTratandose = []
i = 0

ult = -1

max = 0

while i < nEdificios * 2:
    pos = edificios[i][0]

    stop = False
    while not stop and i < nEdificios * 2:
        if edificios[i][0] == pos:
            operacion = edificios[i]
            edificio = (operacion[1], operacion[3], operacion[2])
            if operacion[4] == 1:
                if len(solucion) > 0:
                    anadir=True
                    q=0
                    eliminar=[]
                    while anadir and q<len(edificiosTratandose):
                        if edificio[0]<=edificiosTratandose[q][0] and edificio[2]<=edificiosTratandose[q][2]:
                            anadir=False
                        if edificio[0]>edificiosTratandose[q][0] and edificio[2]>edificiosTratandose[q][2]:
                            eliminar.append(edificiosTratandose[q])
                        q+=1
                    for elimin in eliminar:
                        edificiosTratandose.remove(elimin)
                    if anadir:
                        edificiosTratandose.append(edificio)
                else:
                    edificiosTratandose.append(edificio)
            else:
                edificio = (operacion[1], operacion[3], operacion[0])
                if edificiosTratandose.__contains__(edificio):
                    edificiosTratandose.remove(edificio)
                    if edificiosIni[ult][1]==max:
                        max=0
            i += 1
        else:
            stop = True

    for edificio in edificiosTratandose:
        if edificio[0] > max:
            max = edificio[0]
            hasta = edificio[2]
            ult = edificio[1]
    if len(solucion) == 0:
        solucion.append(pos)
        solucion.append(max)
    elif solucion[len(solucion) - 1] != max:
        solucion.append(pos)
        solucion.append(max)

print(' '.join(map(str, solucion)))
