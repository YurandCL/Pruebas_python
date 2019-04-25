agrega=input("introduzca aqui el nombre del nuevo producto\n")
try:
    x=int(input("¿Cuantos tendra en stock?\n"))
    y=(input("¿A cuanto lo vendera?\n"))
except:
    print("no introdujo un valor entero vuelva a intentar")
temp=0
archivo=open("yo.txt","r+")
archivo.seek(0,1)
archivo.write("Nro:",temp,"\nProducto:",agrega,"\nCantidad:",x,"\nPrecio:",y,"\n")
print("producto agregado satisfactoriamente")
print("no se pudo agregar el producto")
archivo.close()
