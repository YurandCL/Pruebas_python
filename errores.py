def nameError():
  try:
    a=int(input("ingrese un numero\n"))
    b=int(input("ingrese otro numero\n"))
    print(a+b)
  except Exception as e:
        print("tipo de error: ",type(e).__name__)
        print()
nameError()
def agregar_una_vez(numeros,a):
  try:
    for i in range(len(numeros)):
      if a==numeros[i]:
        raise ValueError
    numeros.append(a)
    print(numeros)
  except ValueError:
    print("imposible añadir elementos duplicados ==>", a)

#lista=[1,2,3,4,5]
#a=int(input("ingrese un valor\n"))
#agregar_una_vez(lista,a)

def sumas():
    try:
       resultado=12+"13"
       print("la suma entre estos dos numeros es ",resultado)
    except Exception as e:
        print("tipo de error: ",type(e).__name__)
        print("no ingreso un numero\nvuelva a intentar")
def diccionario():
    while (True):
        try:
            colores={"rojo":"red","verde":"green","negro":"blak"}
            color=input("¿que color desea traducir?\n")
            print(colores[color])
            break
        except Exception as e:
            print("tipo de error: ",type(e).__name__)
            print("este color no esta registrado\nintente otra vez")
def listas():
    while(True):
        try:
            lista=[1,2,3,4,5]
            n=int(input("ingrese la pocicion a buscar\n"))
            print("la pocicion ",n," contiene al numero ",lista[n])
            break
        except Exception as e:
            print("tipo de error: ",type(e).__name__)
            print("esta pocicion no existe\nintente otra vez")
def division():
    while (True):
        try:
            n=int(input("ingrese un numero\n"))
            n1=int(input("ingrese otro numero\n"))
            a=0
            a=n/n1
            a=int(a)
            print("la division ",n,"/",n1," es igual a: ",a)
            break
        except Exception as e:
            print("tipo de error: ",type(e).__name__)
            print("no se puede dividir un numero entre cero\nintente otra vez")
