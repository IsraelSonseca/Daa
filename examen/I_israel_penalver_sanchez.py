import copy

def inicializarDatos():
    nAlimentos, tamanio = map(int, input().strip().split())
    volumenes=[]
    valores=[]
    for i in range(nAlimentos):
        name, vol, value = input().strip().split()
        volumenes.append(int(vol))
        valores.append(int(value))
    datos = {}
    datos['N'] = nAlimentos
    datos['W'] = tamanio
    datos['Peso'] = volumenes
    datos['Valor'] = valores
    return datos

def inicializarSolucion(datos):
    solucion = {}
    solucion['Objetos'] = [0]*datos['N']
    solucion['Peso'] = 0
    solucion['Valor'] = 0
    return solucion

def esSolucion(solucion,datos):
    return solucion['Peso'] + min(datos['Peso']) > datos['W']

def mejor(sol1,sol2):
    if sol1['Valor'] > sol2['Valor']:
        mejor = copy.deepcopy(sol1)
    else:
        mejor = copy.deepcopy(sol2)
    return mejor

def esFactible(solucion,datos, i):
    a=solucion['Peso'] + datos['Peso'][i] <= datos['W']
    b=solucion['Objetos'][i]==0
    return a and b

def asignar(solucion,i,datos):
    solucion['Objetos'][i] += 1
    solucion['Peso'] += datos['Peso'][i]
    solucion['Valor'] += datos['Valor'][i]
    return solucion

def borrar(solucion,i,datos):
    solucion['Objetos'][i] -= 1
    solucion['Peso'] -= datos['Peso'][i]
    solucion['Valor'] -= datos['Valor'][i]
    return solucion

def mochilaVA(solucion, mejorSol, datos, k):
    if esSolucion(solucion, datos):
        mejorSol = mejor(mejorSol, solucion)
    else:
        for i in range(k, datos['N']):
            if esFactible(solucion, datos, i):
                solucion = asignar(solucion, i, datos)
                mejorSol = mochilaVA(solucion, mejorSol, datos, i)
                solucion = borrar(solucion, i, datos)
    return mejorSol

# Prog Ppal
datos = inicializarDatos()
solucion = inicializarSolucion(datos)
mejorSol = inicializarSolucion(datos)
mejorSol = mochilaVA(solucion,mejorSol,datos,0)
print(mejorSol['Valor'])





