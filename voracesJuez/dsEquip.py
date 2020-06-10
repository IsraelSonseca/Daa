def getBestEquip(data, candidates):
    bestCandidate = 0
    bestRatio = 0
    for candidate in candidates:
        newRatio = data['valores'][candidate] / data['pesos'][candidate]
        if newRatio > bestRatio:
            bestCandidate = candidate
            bestRatio = newRatio
    return bestCandidate


def isFactible(data, bestEquip):
    return data['freeWeight'] > data['pesos'][bestEquip]


def greedyDSEquip(data):
    candidates = set()
    for i in range(data['nObjetos']):
        candidates.add(i)
    sol = [0] * data['nObjetos']
    isSol = False
    while candidates and not isSol:
        bestEquip = getBestEquip(data, candidates)
        if isFactible(data, bestEquip):
            data['freeWeight'] -= data['pesos'][bestEquip]
            candidates.remove(bestEquip)
            sol[bestEquip] = 1
        else:
            sol[bestEquip] = data['freeWeight'] / data['pesos'][bestEquip]
            isSol = True

    return sol


N = int(input().strip())
M = int(input().strip())
modo = str(input().strip())
if modo == 'ligero':
    MAXWEIGHT = M / 2
elif modo == 'medio':
    MAXWEIGHT = M * 3 / 4
elif modo == 'pesado':
    MAXWEIGHT = M

data = {
    'nObjetos': N,
    'freeWeight': MAXWEIGHT,
    'objetos': [],
    'pesos': [],
    'valores': []
}
for i in range(N):
    objeto, peso, valor = input().strip().split()
    data['objetos'].append(objeto)
    data['pesos'].append(int(peso))
    data['valores'].append(int(valor))

equipamentoOptimo = greedyDSEquip(data)

valor = 0
for i, cantidad in enumerate(equipamentoOptimo):
    valor += data['valores'][i]*cantidad
print( "{:.2f}".format(valor) )

objetosAEquipar=[]
for i,cantidad in enumerate(equipamentoOptimo):
    if cantidad>0:
        objetosAEquipar.append(data['objetos'][i])
objetosAEquipar.sort()
for i in objetosAEquipar:
    print(i)