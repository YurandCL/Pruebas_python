archivo=open("mi_texto.txt","r")
print("Lectura realizada correctamente:")
lista=archivo.readlines()
print("Imprimiendo la tercera linea: ",lista[2])
archivo.close()
