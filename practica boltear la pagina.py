def cuenta_libro(i,paginas,nombre):
  #darle vuelta para leer las paginas del libro
  if i==0:
    print(nombre)
    a=input("aprete enter para continuar")
    if a=="":
      cuenta_libro(i+1,paginas,nombre)
  else:
    print("contenido de la pg",i,"\n..........")
    if i==paginas:
      print("fin del libro")
    else:
      a=input("enter para darle vuelta a la pagina")
      if a=="":
        if i<paginas:
          cuenta_libro(i+1,paginas,nombre)
        else:
          return
def libro():
    libros={"las memorias de un gato tonto":178,"la culpa es de la vaca":124,
            "Diez dias que estremecieron al mundo":136,
            "jorge el hijo del pueblo":221}
    nombreLibro=input("elija el libro que desea leer\n")
    paginas=libros[nombreLibro]
    pag=0
    pag=int(input("ingrese la pagina en la que se quedo\n"))
    cuenta_libro(pag,paginas,nombreLibro)
    x=input("desea leer otro libro   SI/NO\n")
    x=x.lower()
    if x=="si":
      libro()
    else:
      print("lo esperamos pronto\ngracias por su preferencia")
      return
libro()
