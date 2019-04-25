def depende(a,b,d):
  cont=1
  if (a=="paga"):
    print("ELIJE UNA DE ESTAS CANCIONES QUE TENEMOS PARA TI\n",b)
    c=input("desea salir   si/no \n")
    c=c.lower()
    if (c=="si"):
      print("adios amigo vuelve pronto")
      return
    else:
      cont+=1
      depende("paga",b,d)
  elif (a=="gratuito"):
    print ("haz clic en aleatorio  (si deseas elgir vulvete premium)\n===ALEATORIO===\n")
    print("ESTAS CANCIONS SE REPRODUCIRAN DE MANERA RANDOM\n",d,"\n")
    print("RECUERDA QUE SI TE VUELVES PREMIUM PUEDES ESCOGER MAS CANCIONES Y ESCUCHAR SIN ANUNCIOS")
    c=input("DESEAS VOLVERTE PREMIUM???   si/no\n")
    c=c.lower()
    if (c=="si"):
      print("pagara $10 por mes    \"puede canelar la subscripcion cuando quiera\" ")
      depende("paga",b,d)
      return
    c=input("DESEA SALIR??   si/no\n")
    c=c.lower()
    if (c=="si"):
      print("adios amigo vuelve pronto")
      return
    else:
      cont+=1
      depende("gratuito",b,d)

usuario=input("escriba su nombre de usuario\n")
usuario=usuario.lower()
lista=["despacito","el amante","traicionera","andaz en mi cabeza",
       "vacaciones","tienes la sonrisa","subeme la radio",
       "don't wana know","shape of you"]
lista2=["despacito","greenlight","let me love you",
        "la bicicleta","andas en mi cabeza","frijolero"]
dicionario=dict()
diccionario={"yurand":"paga","jorge":"gratuito","carmen":"gratuito","mayte":"paga"}
u=diccionario[usuario]
depende(u,lista,lista2)


