cont=0
archivo=open("mi_archivo.txt", "r+")
lin=archivo.readlines()
for i in lin:
    cont+=1
lin[0].write("cambio")
print("Archivo creado!!")
archivo.close()
