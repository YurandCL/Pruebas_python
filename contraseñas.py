pasword ="a"
intento=input("ingrese su clave\n")
cont=0
while intento != pasword:
  cont+=1
  if (cont==3):
    break
  intento =input("Error ingrese su contraseña nuevamente\n")
if (cont==3):
  print("No seas sapo")
else:
  print("Bienvenido")
