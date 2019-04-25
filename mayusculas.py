#ejercicio Nº 14

def mayusculas(un_string):
  cont=0
  for i in range(len(un_string)):
    if (un_string[i]=="A" or un_string[i]=="D" or un_string[i]=="B" or un_string[i]=="C"):
      cont+=1
    elif(un_string[i]=="E" or un_string[i]=="F" or un_string[i]=="G" or un_string[i]=="H"):
      cont+=1
    elif(un_string[i]=="I" or un_string[i]=="J" or un_string[i]=="K" or un_string[i]=="L"):
      cont+=1
    elif(un_string[i]=="M" or un_string[i]=="N" or un_string[i]=="Ñ" or un_string[i]=="O"):
      cont+=1
    elif(un_string[i]=="P" or un_string[i]=="Q" or un_string[i]=="R" or un_string[i]=="S"):
      cont+=1
    elif(un_string[i]=="T" or un_string[i]=="U" or un_string[i]=="V" or un_string[i]=="W"):
      cont+=1
    elif(un_string[i]=="X" or un_string[i]=="Y" or un_string[i]=="Z"):
      cont+=1
  return cont

mi_string=input("ingrese el texto a analizar\n")
print ("hay ",mayusculas(mi_string),"mayusculas en este texto")
