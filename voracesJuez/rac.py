def isFeasible(data, actividad, caso, lastTimeOccupied):
    return data['inicios'][caso][actividad]>=lastTimeOccupied


def getListActivitiesBestInit(data, caso):
    actividades=[]
    for i in range(data['nActividades'][caso]):
        actividades.append((data['finalizaciones'][caso][i],i))
    actividades.sort()
    return actividades



nCasos = int(input().strip())
data = {
    'nActividades': [],
    'inicios': [],
    'finalizaciones': []
}





for caso in range(nCasos):
    data['nActividades'].append(int(input().strip()))
    lineaLeida=input().strip().split()
    data['inicios'].append([])
    data['finalizaciones'].append([])
    for i in range(data['nActividades'][caso]):
        data['inicios'][caso].append(int(lineaLeida[i*2]))
        data['finalizaciones'][caso].append(int(lineaLeida[(i*2)+1]))




for i in range(nCasos):
    nActividadesRealizadas=0
    lastTimeOccupied=0
    actividadesOrdenadas=getListActivitiesBestInit(data, i)
    for actividad in actividadesOrdenadas:
        if isFeasible(data, actividad[1], i,lastTimeOccupied):
            lastTimeOccupied=data['finalizaciones'][i][actividad[1]]
            nActividadesRealizadas+=1
    print(nActividadesRealizadas)