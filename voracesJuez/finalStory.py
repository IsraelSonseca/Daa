import math


def getListBestDeaths(data, candidates, iCombate):
    vivos = []
    for i in candidates:
        turnos = math.ceil(data['vidaRivales'][iCombate][i] / data['ataque'][iCombate])
        vivos.append((turnos / data['ataqueRivales'][iCombate][i], i))
    vivos.sort()
    return vivos


nCombates = int(input().strip())
data = {
    'ataque': [],
    'nRivales': [],
    'ataqueRivales': [],
    'ataqueConjunto': [],
    'vidaRivales': []
}
for iCombate in range(nCombates):
    data['ataque'].append(int(input().strip()))
    data['nRivales'].append(int(input().strip()))
    a = input().strip().split()
    data['ataqueRivales'].append([])
    data['ataqueConjunto'].append(0)
    b = input().strip().split()
    data['vidaRivales'].append([])
    for iEnemigo in range(data['nRivales'][iCombate]):
        data['ataqueRivales'][iCombate].append(int(a[iEnemigo]))
        data['ataqueConjunto'][iCombate] += int(a[iEnemigo])
        data['vidaRivales'][iCombate].append(int(b[iEnemigo]))

for iCombate in range(nCombates):

    danio = 0
    candidates = set()
    for i in range(data['nRivales'][iCombate]):
        candidates.add(i)
    enemigosOrdenadosAMorir = getListBestDeaths(data, candidates, iCombate)
    for enemigo in enemigosOrdenadosAMorir:
        turnosEnMorir = math.ceil(data['vidaRivales'][iCombate][enemigo[1]] / data['ataque'][iCombate])
        danio += turnosEnMorir * data['ataqueConjunto'][iCombate]
        data['ataqueConjunto'][iCombate] -= data['ataqueRivales'][iCombate][enemigo[1]]
    print(danio)
