#Ejercicio 17

def edades(a):
    b=0
    cont=0
    for b in range(10):
      a=int(input("ingrese su edad\n"))
      if (a>20):
        cont+=1
    print("la cantidad de personas que tienen la edad mayor a 20 años son: ",cont)
a=0
edades(a)
