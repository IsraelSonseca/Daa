def getBest(data, candidates):
    bestRatio = 0
    best = 0
    for c in candidates:
        ratio = data['importanciasRelativas'][c]
        if ratio > bestRatio:
            bestRatio = ratio
            best = c
    return best

def isFeasible(data,best,freePags):
    return data['nPags'][best]<freePags


def greedy(data,caso):
    n = data['nProgramas']
    candidates = set()
    for i in range(n):
        candidates.add(i)
    freePags = data['maxPags'][caso]
    sol = [0]*n
    isSol = False
    while not isSol and candidates:
        bestItem = getBest(data, candidates)
        candidates.remove(bestItem)
        if isFeasible(data, bestItem, freePags):
            sol[bestItem] = 1.0
            freePags -= data['nPags'][bestItem]
        else:
            sol[bestItem] = freePags / data['nPags'][bestItem]
            isSol = True
    return sol


nProgramas, nPruebas = map(int, input().strip().split())
data = {
    'nProgramas':nProgramas,
    'nPruebas':nPruebas,
    'importancias':[],
    'nPags':[],
    'importanciasDeseadas':[],
    'maxPags':[],
    'importanciasRelativas':[]

}
for i in range(nProgramas):
    importancia, nPaginas = map(int, input().strip().split())
    data['importancias'].append(importancia)
    data['nPags'].append(nPaginas)
    data['importanciasRelativas'].append(importancia/nPaginas)
for i in range(nPruebas):
    importanciaDeseada, maxPags =map(int, input().strip().split())
    data['importanciasDeseadas'].append(importanciaDeseada)
    data['maxPags'].append(maxPags)
for i in range(nPruebas):
    solucion=greedy(data,i)
    valorConseguido=0
    for index,elem in enumerate(solucion):
        valorConseguido+=elem*data['importancias'][index]
    if valorConseguido>=data['importanciasDeseadas'][i]:
        print('PUEDE')
    else:
        print('TOS')