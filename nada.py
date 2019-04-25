while (True):
    try:
        a=float(input("ingrese un numero\n"))
        b=float(input("ingrese otro numero\n"))
        c=a/b
        print("la division de estos numeros es: ",c)
        break
    except ArithmeticError as e:
        print("tipo de error: ",type(e).__name__)
        print("no inserto un numero o escribio cero vuelva a intentar")
    except ValueError as e:
        print("tipo de error: ",type(e).__name__)
        print("no ingreso un numero vuelva a intentar")
    except Exception as e:
        print("tipo de error", type(e).__name__)
        raise

