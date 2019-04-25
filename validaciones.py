def validar(n,r,lista):
    assert n>=0, "n tiene que ser mayor igual que cero"
    assert r<9, "r tiene que ser menor que 9"
    assert ordenada(lista), "la lista tiene que ser ordenada"
    assert (r+n)>=13, "la suma de estos dos numeros tiene que ser mayor a 13"
    assert (r/n)<=2, "la division de estos numeros tiene que ser menor igual a 0"
    print("validacion exitosa")

def ordenada(lista):
    for i in range(0,len(lista)-1):
        if lista[i]>lista[i+1]:
            return False
    return True

validar(8,8,[4,5,6,7,8,9])

