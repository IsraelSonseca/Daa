nNiveles=int(input().strip())
listaNiveles=input().strip().split()
nJugadores=int(input().strip())
listaJugadores=input().strip().split()


def calcularIndice(listaNiveles,inicio,fin,nuevo):
    long=fin-inicio
    mid= (long//2)+inicio
    if int(listaNiveles[mid])<nuevo:
        if long==1:
            return mid,mid+1
        else:
            return calcularIndice(listaNiveles,mid,fin,nuevo)
    elif int(listaNiveles[mid])>nuevo:
        if long==1:
            return mid-1,mid
        else:
            return calcularIndice(listaNiveles,inicio,mid,nuevo)
    else:
        return mid-1,mid+1


for i in listaJugadores:
    menor,mayor=calcularIndice(listaNiveles,0,nNiveles,int(i))
    if menor< 0:
        menor = 'X'
    else:
        menor = listaNiveles[menor]
    if mayor >= nNiveles:
        mayor = 'X'
    else:
        mayor = listaNiveles[mayor]

    print(menor,end=' ')
    print(mayor)
