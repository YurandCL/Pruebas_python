archivo=open("mi_texto.txt","r")
print("Lectura Realizada Correctamente:")
cont=0
for linea in archivo:
    cont+=1
    print(linea,"\n")
print(cont)
archivo.close()
