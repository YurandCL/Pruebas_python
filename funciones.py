def yurand():
    a=0
    b=0
    a=int(input("ingrese un valor\n"))
    b=int(input("ingrese otro valor\n"))
    print(a*b)
def coloma():
    a=0
    b=0
    for a in range (6):
        for b in range (6):
            if ((a>=2 and a<=4)and (b>=2 and b<=4)):
                print (" ")
                continue
            print("*")
    print ("\n")
#yurand()
coloma()
print("gracias")
