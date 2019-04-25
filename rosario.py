def rezar_rosario(i):
  if (i==0):
    print ("haga la señal de la cruz\nseguidamente rezaremos el credo")
    print("ahora empezaremos")
    i+=1
  print("anunciamos el",i,"º misterio")
  cont=0
  print ("rezamos el",i,"º padre nuestro")
  for j in range(10,0,-1):
    a=input("apreta enter para continuar")
    if (i<6):
      if (a==""):
        print("rezar ",j," avemarias restantes")
        if (j==1):
          print("ahora rezaremos el gloria junto con la jaculatoria")
          print("(pueden cantar si desean)")
        cont+=1
        if cont==10:
          if (i==5):
            print("REZAMOS EL \"SALVE\"\ny terminamos con la señal de la cruz")
            return
          else:
            rezar_rosario(i+1)
   
  return
print("si empezara el rosario recien escriba \"cero\" en numeros \"0\"")
r=int(input("sino el misterio en el que se quedo\n"))
rezar_rosario(r)
