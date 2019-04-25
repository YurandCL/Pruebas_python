def cdecimal(x):
    i = 1
    v=5
    x=10
    l=50
    c=100
    d=500
    m=1000
    cont=0
    b=len(x-1)
    a=0
    for i in range(len(x)):
        if("M"==x[cont] or "m"==x[cont]):
            a = 1000
            cont+=1
        elif("D"==x[b] or "d"==x[b]):
            a = 500
        elif("C"==x[b] or "c"==x[b]):
            a = 100
        elif("L"==x[b] or "l"==x[b]):
            a = 50
        elif("X"==x[b] or "x"==x[b]):
            a = 10
        elif("V"==x[b] or "v"==x[b]):
            a = 5
        elif("I"==x[b] or "i"==x[b]):
            a = 1

def cromano:
    #a decimal
    
