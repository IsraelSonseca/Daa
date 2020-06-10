nEnemigos=int(input().strip())
nivelEnemigo=input().strip().split()
puntos=[0]
p=0
for i in nivelEnemigo:
    p=p+int(i)
    puntos.append(p)
#for i in range(nEnemigos):
    #nivelEnemigo[i]=int(nivelEnemigo[i])
nPruebas=int(input().strip())
nivelCaballero=[]
for i in range(nPruebas):
    nivelCaballero.append(input().strip())


def calcularIndice(listaNiveles,inicio,fin,nuevo):
    long=fin-inicio
    mid= (long//2)+inicio
    if int(listaNiveles[mid])<=nuevo:
        if long==1:
            return mid+1
        else:
            return calcularIndice(listaNiveles,mid,fin,nuevo)
    elif int(listaNiveles[mid])>nuevo:
        if long==1:
            return mid
        else:
            return calcularIndice(listaNiveles,inicio,mid,nuevo)


for i in nivelCaballero:
    indice=calcularIndice(nivelEnemigo,0,nEnemigos,int(i))
    #puntos=0
    #for i in range(indice):
    #    puntos+=int(nivelEnemigo[i])
    print(indice, end=' ')
    print(puntos[indice])