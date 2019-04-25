
def quicksort(lista,izq,der):
    i=izq
    j=der
    k=int((izq+der)/2)
    x=lista[k]
    while( i <= j ):
        while lista[i]<x and j<=der:
            i=i+1
        while x<lista[j] and j>izq:
            j=j-1
        if i<=j:
            aux = lista[i]; lista[i] = lista[j]; lista[j] = aux;
            i=i+1;  j=j-1;
        if izq < j:
          quicksort( lista, izq, j );
    if i < der:
        quicksort( lista, i, der );
def imprimeLista(lista,tam):
    for i in range(0,tam):
        print (lista[i])
def leeLista():
    lista=[]
    cn=int(input("Cantidad de numeros a ingresar: "))
    for i in range(0,cn):
        lista.append(int(input("Ingrese numero %d : " % i)))
    return lista
def listas():
    A=leeLista()
    quicksort(A,0,len(A)-1)
    imprimeLista(A,len(A))
    salir()
def salir():
    e=input("¿Desea Salir?    Si/No\n")
    if (e=="si"):
        print("Hasta Luego Vuelva Pronto")
        return
    else:
        listas()
listas()
