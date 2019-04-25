def desordenar(lista):
  i = len(lista)
  while i > 1:
    i = i - 1
    j = randrange(i)  # 0 < = j <= i-1
    lista[j], lista[i] = lista[i], lista[j]
  return

def error():
  print ("la lista no esta ordenada")
  return

def verificar(lista):
  cont=0
  for i in range(0,len(lista)-2):
    if lista[i]>lista[i+1]:
      error()
      return
  desordenar(lista)
  return

#quitar el comentario (#) segun la lista que deseamos verificar
#lista=[5, 17, 3, 2, 7, 11, 13]
lista=[1,5,9,12,15,26,30]
from random import randrange
verificar(lista)
print(lista)
