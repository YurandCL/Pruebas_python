usuarios=set()
administradores=set()
usuarios={"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores={"Juan", "Marta"}
lista=list(administradores)
lista[0]="Marcos"
administradores=set(lista)
print("============USUARIOS y/o ADMINISTRADORES===========")
print("¿Marta es administradora?","Marta" in administradores)
print("¿David es administrador?","David" in administradores)
print("¿Elvira es administradora?","Elvira" in administradores)
print("¿Juan es administrador?","Juan" in administradores)
print("¿Marcos es administrador?","Marcos" in administradores)
print("============USUARIOS y/o ADMINISTRADORES==========")
