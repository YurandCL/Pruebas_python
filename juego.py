nombre=""
nombre=input("pongale un nombre a su personaje\n")
print("ahora veremos sus caracteristicas en este orden:")
print("========= vida, ataque, defensa, alcance =========")
avatares=[]
a={"Clase":"Caballero", "vida":80, "ataque":15, "defensa":32, "alcance":3}
avatares.append(a)

a={"Clase":"Guerrero", "vida":40, "ataque":30, "defensa":16, "alcance":6}
avatares.append(a)

a={"Clase":"Arquero", "vida":40, "ataque":30, "defensa":8, "alcance":12}
avatares.append(a)

for a in avatares:
    print(a["Clase"], nombre, a["vida"],a["ataque"],a["defensa"],a["alcance"])
print("============= decide con sabiduria =============")

