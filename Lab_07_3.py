# Ejercicio N° 15
def binario(x):
    a=0
    cont=0
    b=len(x)-1
    for i in range(len(x)):
        if ("1"==x[b]):
            a=a+(2**cont)
        b-=1
        cont+=1
    print (a)
x=""
x=input("ingrese el numero que desea convertir\n")
binario(x)
