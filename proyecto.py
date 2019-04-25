#nombre_variable.capitalize() para poner mayuscula a la primera letra de un string
#nombre_variable.lower() para volver minuscula un string

def restaurarValores():
    archivo=open("usuarios.txt","w")
    u1="Juan:020399\n"
    u2="Alex:281216\n"
    u3="Jhon:271147\n"
    archivo.write(u1)
    archivo.write(u2)
    archivo.write(u3)
    archivo.close()
    archivo=open("base_de_datos.txt","w")
    a="Nro:1\nProducto:Aceite\nCantidad:12\nPrecio:10\n"
    b="Nro:2\nProducto:Leche\nCantidad:50\nPrecio:3\n"
    c="Nro:3\nProducto:Detergente\nCantidad:20\nPrecio:4\n"
    d="Nro:4\nProducto:Yogurt1Lt\nCantidad:6\nPrecio:6\n"
    archivo.write(a)
    archivo.write(b)
    archivo.write(c)
    archivo.write(d)
    archivo.close()
    usuario()

def existe():
    try:
        archivo=open("usuarios.txt","x")
        u1="Juan:020399\n"
        u2="Alex:281216\n"
        u3="Jhon:271147\n"
        archivo.write(u1)
        archivo.write(u2)
        archivo.write(u3)
        archivo.close()
    except:
        print("Vamos a empezar")
    try:
        archivo=open("base_de_datos.txt","x")
        a="Nro:1\nProducto:Aceite\nCantidad:12\nPrecio:10\n"
        b="Nro:2\nProducto:Leche\nCantidad:50\nPrecio:3\n"
        c="Nro:3\nProducto:Detergente\nCantidad:20\nPrecio:4\n"
        d="Nro:4\nProducto:Yogurt1Lt\nCantidad:6\nPrecio:6\n"
        archivo.write(a)
        archivo.write(b)
        archivo.write(c)
        archivo.write(d)
        archivo.close()
    except:
        usuario()
        return
    usuario()
    return

def usuario():
    a=""
    b=""
    c=""
    c=input("¿Tiene Cuenta en esta tienda? escriba \"si\" o \"no\"\n")
    c=c.lower()
    if(c=="no"):
        a=input("Ingrese su nombre de usuario\n")
        a=a.capitalize()
        b=input("Ingrese su contraseña \"asegurese de que sea mayor a cuatro caracteres)\"\n")
        temp=""
        tmp=""
        archivo=open("usuarios.txt","r")
        lin=archivo.readlines()
        for i in range(len(lin)):
            temp=lin[i]
            tmp=""
            for j in range(len(temp)):
                if(temp[j]==":"):
                    if(tmp==a):
                        print("El nombre de usuario ya existe pruebe con otro")
                        archivo.close()
                        usuario()
                        return
                else:
                    tmp=tmp+temp[j]
                    #print(tmp)
        archivo.close()
        if(len(b)>=5):
            try:
                d=int(input("Ingrese el codigo que le dio el gerente\n"))
            except:
                print("asegurese que haya anotado bien el codigo dado")
            if(d==70412138):
                archivo=open("usuarios.txt","a")
                archivo.write(a)
                archivo.write(":")
                archivo.write(b)
                archivo.write("\n")
                archivo.close()
                print("el usuario fue añadido correctamente")
            inicio()
            return
        else:
            print("su contraseña debe ser mayor a cuatro caracteres\nVuelva a intentar")
            usuario()
            return
    elif(c=="si"):
        archivo=open("usuarios.txt","r")
        a=input("Ingrese su nombre de usuario\n")
        b=input("Ingrese su contraseña\n")
        a=a.capitalize()
        lin=archivo.readlines()
        for i in range(len(lin)):
            if a+":"+b+"\n"==lin[i]:
                archivo.close()
                inicio()
                return
        print("asegurese que su contraseña y su ID esten bien escritos")
        usuario()
        return
    else:
        print("error al introducir datos\nasegurese de escribir \"si\" o \"no\"")
        usuario()
        return
        
def inicio():
    nro=0
    try:
        nro=int(input("Ingrese el Nro del producto a buscar o\nSi desea añadir un objeto aprete otro numero\nSi desea salir aprete cualquier tecla\n"))
    except:
        g=input("¿Está seguro que quiere salir? \"si\" o \"no\"\n")
        if(g=="si"):
            return
        else:
            inicio()
            return
    Nro(nro)
    
def Nro(x):
    archivo=open("base_de_datos.txt","r")
    temp=0
    cont=0
    lin=archivo.readlines()
    for l in lin:
        cont+=1
    temp=int(cont/4)
    archivo.close()
    if x>0 and x<=temp:
        objetos(x)
        return
    elif x>temp or x<=0:
        crear(temp)
        return
    
def crear(num):
    agrega=input("introduzca aqui el nombre del nuevo producto\n")
    agrega=agrega.capitalize()
    agrega=agrega+"\n"
    try:
        x=int(input("¿Cuantos tendra en stock?\n"))
        y=int(input("¿A cuanto lo vendera?\n"))
    except:
        print("no introdujo un valor numerico vuelva a intentar")
        crear(x)
        return
    temp=""
    num+=1
    temp=temp+str(num)+"\n"
    x=str(x)+"\n"
    y=str(y)+"\n"
    archivo=open("base_de_datos.txt","a")
    archivo.write("Nro:")
    archivo.write(temp)
    archivo.write("Producto:")
    archivo.write(agrega)
    archivo.write("Cantidad:")
    archivo.write(x)
    archivo.write("Precio:")
    archivo.write(y)
    archivo.close()
    print("Nuevo elemento Creado satisfactoriamente")
    inicio()
    return
    
def objetos(x):
    print("¿Comprará o venderá algun objeto?")
    temp=input("Escriba \"si\" para comprar o vender o \"no\" para actualizar sus datos\n")
    temp=temp.lower()
    if temp=="si":
        CompraVenta(x)
        return
    elif temp=="no":
        lectura(x)
        return
    else:
        print("Tuvo un error al momento de introducir los datos\nVuelva a intentar")
        print("Asegurese de no anotar mas que solo una de estas dos palabras\n\"si\" o \"no\"")
        objetos(x)
        return

def lectura(a):
    x=input("¿Desea modificar alguna caracteristica de este producto o elimarlo por completo? \"si\" o \"no\"\n")
    if(x=="si"):
        try:
            y=int(input("Uno \"1\" para modificar y dos \"2\" para eliminar\n"))
        except:
            print("no introdujo un valor numerico\nVuelva a intentar")
            lectura(a)
            return
        if(y==1):
            modificar(a)
            return
        elif(y==2):
            eliminar(a)
            return
        else:
            print("Puso un número incorrecto\nVUelva a intentar")
            lectura(a)
            
    temp=""
    archivo=open("base_de_datos.txt","r")
    lin=archivo.readlines()
    temp="Nro:"+str(a)+"\n"
    for i in range(len(lin)-1):
        if(temp==str(lin[i])):
            print(" ",lin[i],lin[i+1],lin[i+2],lin[i+3])
    inicio()
    return

def modificar(a):
    try:
        cual=int(input("¿Qué caracteristica desea modificar?\nProducto \"1\" , Precio \"2\" ,  Cantidad \"3\"  o Todo \"4\"\n"))
    except:
        print("No ingreseo un numero entero asegurese de introducir los datos correctamente")
        modificar(a)
        return
    if(cual==1):
        archivo=open("base_de_datos.txt","r")
        lin=archivo.readlines()
        pdct=""
        nro=""
        temp=""
        cambio=input("Escriba aqui el nombre del nuevo producto\n")
        cambio=cambio.capitalize()+"\n"
        for i in range(len(lin)):
            nro="Nro:"+str(a)+"\n"
            if(nro==lin[i]):
                pdct=str(lin[i+1])                
                archivo.close()
                break
        
        temp=""
        tmp=""
        archivo=open("base_de_datos.txt","r+")
        lin=archivo.readlines()
        for w in range(len(lin)):
            if(pdct==lin[w]):
                for k in range(w,len(lin)-1):
                    temp=temp+lin[k+1]
                break
            else:
                tmp=tmp+lin[w]
        archivo.close()
        archivo=open("base_de_datos.txt","w")
        archivo.write(tmp)
        archivo.write("Producto:")
        archivo.write(cambio)
        archivo.write(temp)
        archivo.close()
        print("Cambio Realizado Satisfactoriamente")                
        archivo.close()
        x=input("¿Hará mas cambios? \"si\" o \"no\"\n")
        if(x=="si"):
            try:
                y=int(input("Ingrese el número del producto al que modificará\n"))
            except:
                print("no ingresó un numero entero\nVuelva a intentar")
                inicio()
                return
            archivo=open("base_de_datos.txt","r")
            temp=0
            cont=0
            lin=archivo.readlines()
            for l in lin:
                cont+=1
            temp=int(cont/4)
            archivo.close()
            if(y<0 or y>temp):
                print("El valor ingresado no está registrado")
                inicio()
                return
            else:
                modificar(y)
                return
        else:
            inicio()
            return
    elif(cual==2):
        archivo=open("base_de_datos.txt","r")
        lin=archivo.readlines()
        precio=""
        nro=""
        cambio=float(input("Escriba aqui el nuevo precio del producto\n"))
        cambio=str(cambio)+"\n"
        for i in range(len(lin)):
            nro="Nro:"+str(a)+"\n"
            if(nro==lin[i]):
                precio=str(lin[i+3])                
                archivo.close()
                break
        
        temp=""
        tmp=""
        archivo=open("base_de_datos.txt","r")
        lin=archivo.readlines()
        for w in range(len(lin)):
            if(precio==lin[w]):
                for k in range(w,len(lin)-1):
                    temp=temp+lin[k+1]
                break
            else:
                tmp=tmp+lin[w]
        archivo.close()
        archivo=open("base_de_datos.txt","w")
        archivo.write(tmp)
        archivo.write("Precio:")
        archivo.write(cambio)
        archivo.write(temp)
        archivo.close()
        print("Cambio Realizado Satisfactoriamente")                
        archivo.close()
        x=input("¿Hará mas cambios? \"si\" o \"no\"\n")
        if(x=="si"):
            try:
                y=int(input("Ingrese el número del producto al que modificará\n"))
            except:
                print("no ingresó un numero entero\nVuelva a intentar")
                inicio()
                return
            archivo=open("base_de_datos.txt","r")
            temp=0
            cont=0
            lin=archivo.readlines()
            for l in lin:
                cont+=1
            temp=int(cont/4)
            archivo.close()
            if(y<0 or y>temp):
                print("El valor ingresado no está registrado")
                inicio()
                return
            else:
                modificar(y)
                return
        else:
            inicio()
            return

    if(cual==3):#modificar este elmento
        archivo=open("base_de_datos.txt","r")
        lin=archivo.readlines()
        pdct=""
        nro=""
        temp=""
        try:
            cambio=int(input("Escriba aqui la nueva cantidad de elementos que tendrá el producto\n"))
        except:
            print("El caracter ingresado no es correcto vuelva a intentar")
            modificar(a)
            return
        for i in range(len(lin)):
            nro="Nro:"+str(a)+"\n"
            if(nro==lin[i]):
                pdct=str(lin[i+2])                
                archivo.close()
                break
        cambio=str(cambio)+"\n"
        temp=""
        tmp=""
        archivo=open("base_de_datos.txt","r+")
        lin=archivo.readlines()
        for w in range(len(lin)):
            if(pdct==lin[w]):
                for k in range(w,len(lin)-1):
                    temp=temp+lin[k+1]
                break
            else:
                tmp=tmp+lin[w]
        archivo.close()
        archivo=open("base_de_datos.txt","w")
        archivo.write(tmp)
        archivo.write("Cantidad:")
        archivo.write(cambio)
        archivo.write(temp)
        archivo.close()
        print("Cambio Realizado Satisfactoriamente")
        archivo.close()
        x=input("¿Hará mas cambios? \"si\" o \"no\"\n")
        if(x=="si"):
            try:
                y=int(input("Ingrese el número del producto al que modificará\n"))
            except:
                print("no ingresó un numero entero\nVuelva a intentar")
                inicio()
                return
            archivo=open("base_de_datos.txt","r")
            temp=0
            cont=0
            lin=archivo.readlines()
            for l in lin:
                cont+=1
            temp=int(cont/4)
            archivo.close()
            if(y<0 or y>temp):
                print("El valor ingresado no está registrado")
                inicio()
                return
            else:
                modificar(y)
                return
        else:
            inicio()
            return
        
    elif(cual==4):
        producto=input("Ingrese el nuevo nombre del producto\n")
        producto=producto.capitalize()
        precio=float(input("Ingrese el nuevo precio del producto\n"))
        cantidad=int(input("Ingrese la cantidad de stok que tendrá de este producto\n"))
        archivo=open("base_de_datos.txt","r")
        lin=archivo.readlines()
        temp=""
        tmp=""
        for i in range(len(lin)):
            tmp=tmp+lin[i]
            if("Nro:"+str(a)+"\n"==lin[i]):
                for k in range(i+3,len(lin)-1):
                    temp=temp+lin[k+1]
                break
        producto=producto+"\n"
        precio=str(precio)+"\n"
        cantidad=str(cantidad)+"\n"
        archivo.close()
        archivo=open("base_de_datos.txt","w")
        archivo.write(tmp)
        archivo.write("Producto:")
        archivo.write(producto)
        archivo.write("Cantidad:")
        archivo.write(cantidad)
        archivo.write("Precio:")
        archivo.write(precio)
        archivo.write(temp)
        archivo.close()
        x=input("¿Desea cambiar algun otro producto?  \"si\" o \"no\"\n")
        if(x=="si"):
            try:
                y=int(input("Ingrese el Nro del producto que desea cambiar\n"))
            except:
                print("No introdujo un valor numerico")
                inicio()
                return
            archivo=open("base_de_datos.txt","r")
            temp=0
            cont=0
            lin=archivo.readlines()
            for l in lin:
                cont+=1
            temp=int(cont/4)
            archivo.close()
            if(y<0 or y>temp):
                print("El valor ingresado no está registrado")
                inicio()
                return
            else:
                modificar(y)
                return
        else:
            inicio()
            return
    else:
        print("No ingresó uno de estos tres datos \"1\"  , \"2\"  o \"3\" \nVuelva a intentar")
        modificar(a)
        return
    
def CompraVenta(a):
    try:
        x=int(input("Si va a registrar mas productos ponga uno \"1\" para veder ponga dos \"2\"\n"))
    except:
        print("no ingresó un número entero Vuelva a intentar")
        CompraVenta(a)
    if x==1:
        compra(a)
        return
    elif x==2:
        venta(a)
        return
    else:
        print("Error al ingresar datos, asegurese de poner uno o dos")
        CompraVenta(a)
        return
    
def compra(a):
    try:
        compro=int(input("¿Cuantos Productos va a adquirir de este tipo?\n"))
    except:
        print("No ingreseo un numero entero asegurese de introducir los datos correctamente")
        compra(a)
        return
    archivo=open("base_de_datos.txt","r")
    lin=archivo.readlines()
    ctd=""
    pdct=""
    temp=""
    cambio=""
    for i in range(len(lin)):
        pdct="Nro:"+str(a)+"\n"
        if(pdct==lin[i]):
            ctd=str(lin[i+2])
            for j in range(len(ctd)-1):
                if(temp==":"):
                    cambio=cambio+ctd[j]
                    continue
                if(temp=="\n"):
                    break
                if (ctd[j]==":" or ctd[j]=="\n"):
                    temp=ctd[j]
            archivo.close()
            break
    cambio=int(cambio)
    cambio=cambio+compro
    cambio=str(cambio)+"\n"
    temp=""
    tmp=""
    archivo=open("base_de_datos.txt","r+")
    lin=archivo.readlines()
    for w in range(len(lin)):
        if(ctd==lin[w]):
            for k in range(w,len(lin)-1):
                temp=temp+lin[k+1]
            break
        else:
            tmp=tmp+lin[w]
    archivo.close()
    archivo=open("base_de_datos.txt","w")
    archivo.write(tmp)
    archivo.write("Cantidad:")
    archivo.write(compro)
    archivo.write(temp)
    archivo.close()
    print("Los elemntos an sido añadidos correctamente")
    print("Ahora la nueva cantidad será: ",compro)
    archivo.close()
    x=input("¿Hará mas compras? \"si\" o \"no\"\n")
    if(x=="si"):
        try:
            y=int(input("Ingrese el número del producto al cual se le añadirán elementos\n"))
        except:
            print("no ingresó un numero entero\nVuelva a intentar")
            inicio()
            return
        compra(y)
        return
    else:
        inicio()
        return

def venta(a):
    try:
        vendi=int(input("¿Cuantos Productos vendera de este tipo?\n"))
    except:
        print("No ingreseo un numero entero asegurese de introducir los datos correctamente")
        venta(a)
        return
    archivo=open("base_de_datos.txt","r")
    lin=archivo.readlines()
    ctd=""
    pdct=""
    temp=""
    cambio=""
    for i in range(len(lin)):
        pdct="Nro:"+str(a)+"\n"
        if(pdct==lin[i]):
            ctd=str(lin[i+2])
            for j in range(len(ctd)-1):
                if(temp==":"):
                    cambio=cambio+ctd[j]
                    continue
                if(temp=="\n"):
                    break
                if (ctd[j]==":" or ctd[j]=="\n"):
                    temp=ctd[j]
            archivo.close()
            break
    cambio=int(cambio)
    vende=cambio-vendi
    if(vende<0):
        print("no tenemos sufucientes suministros de este tipo, pruebe con una cifra mas baja")
        venta(a)
        return
    vende=str(vende)+"\n"#15-5=101
    temp=""
    tmp=""
    archivo=open("base_de_datos.txt","r+")
    lin=archivo.readlines()
    for w in range(len(lin)):
        if(ctd==lin[w]):
            for k in range(w,len(lin)-1):
                temp=temp+lin[k+1]
            break
        else:
            tmp=tmp+lin[w]
    calcular(a,vendi)
    archivo.close()
    archivo=open("base_de_datos.txt","w")
    archivo.write(tmp)
    archivo.write("Cantidad:")
    archivo.write(vende)
    archivo.write(temp)
    archivo.close()
    print("Transaccion Realizada Satisfactoriamente\nGracias por su compra\n")
    print("Ahora la nueva cantidad será: ",vende)
    archivo.close()
    x=input("¿Hará mas compras? \"si\" o \"no\"\n")
    if(x=="si"):
        try:
            y=int(input("Ingrese el número del producto al cual se le añadirán elementos\n"))
        except:
            print("no ingresó un numero entero\nVuelva a intentar")
            inicio()
            return
        compra(y)
        return
    else:
        inicio()
        return
def calcular(a,b):
    paga=float(input("Ingrese la cantidad de dinero con la que pagara el cliente\n"))
    vuelto=0
    precio=""
    temp=""
    cambio=""
    archivo=open("base_de_datos.txt","r")
    lin=archivo.readlines()
    for i in range(len(lin)):
        if("Nro:"+str(a)+"\n"==lin[i]):
            precio=lin[i+3]
            for j in range(len(precio)):
                if(temp==":"):
                    cambio=cambio+precio[j]
                    continue
                if(temp=="\n"):
                    break
                if (precio[j]==":" or precio[j]=="\n"):
                    temp=precio[j]
    b=int(b)
    paga=int(paga)
    cambio=int(cambio)*b
    vuelto=int(paga)-int(cambio)
    print("El vuelto del cliente es ",vuelto)
    return

def eliminar(a):
    x=input("¿Está seguro de eliminar este Producto de la tienda? \"si\"   \"no\"\n")
    if(x=="si"):
        archivo=open("base_de_datos.txt","r")
        lin=archivo.readlines()
        tmp=""
        temp=""
        nro="Nro:"+str(a)+"\n"
        t=""
        num=""
        cont=4
        tp=""
        for i in range(len(lin)):
            if(nro==lin[i]):
                for j in range(i+4,len(lin)):
                    if(cont==4):
                        num=lin[j]
                        for k in range(4,len(num)-1):
                            t=""
                            t=t+num[k]
                            t=int(t)
                            t=t-1
                            t=str(t)
                            tp="Nro:"+t+"\n"
                            temp=temp+tp
                            cont=1
                    else:
                        temp=temp+lin[j]
                        cont+=1
                archivo.close()
                break
            else:
                tmp=tmp+lin[i]
        archivo=open("base_de_datos.txt","w")
        archivo.write(tmp)
        archivo.write(temp)
        archivo.close()
        print("El archivo ah sido removido correctamente y sus datos han sido actualizados")
        x=input("¿Desea remover otro producto? \"si\"  o  \"no\"\n")
        if(x=="si"):
            y=int(input("Escriba el número del producto que desea eliminar"))
            eliminar(y)
            return
        else:
            inicio()
            return
    else:
        inicio()
        return

existe() 


