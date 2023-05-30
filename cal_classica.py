menu = 1
if menu == 1:
    #calculadora clasica
    print ("cal.classic")
    print ("INGRESAR simbolo para operar: \"+\", \"-\", \"*\", \"/\"")
    opsimb = input()
    resigual = int(input())
    while opsimb != "=": 
        #suma
        if opsimb == "+":
            print ("INGRESAR siguiente operando:")
            sumopnumb = int(input())
            resigual = resigual + sumopnumb
            print ("INGRESAR simbolo para contiunar operarando: \"+\", \"-\", \"*\", \"/\" ")
            print ("o INGRESAR \"=\" para calcular todas las operaciones")
            opsimb = input()
        #resta    
        elif opsimb == "-":
            print ("INGRESAR siguiente operando:")
            minopnumb = int(input())
            resigual = resigual - minopnumb
            print ("INGRESAR simbolo para contiunar operarando: \"+\", \"-\", \"*\", \"/\" ")
            print ("o INGRESAR \"=\" para calcular todas las operaciones")
            opsimb = input()
        #multiplicacion    
        elif opsimb == "*":
            print ("INGRESAR siguiente numero operando:")
            multopnumb = int(input())
            resigual = resigual * multopnumb
            print ("INGRESAR simbolo para contiunar operarando: \"+\", \"-\", \"*\", \"/\" ")
            print ("o INGRESAR \"=\" para calcular todas las operaciones")
            opsimb = input()
        #division    
        elif opsimb == "/":
            print ("INGRESAR siguiente numero operando:")
            divopnumb = int(input())
            resigual = resigual / divopnumb
            print ("INGRESAR simbolo para continuar operando: \"+\", \"-\", \"*\", \"/\" ")
            print ("o INGRESAR \"=\" para calcular todas las operaciones")
            opsimb = input()
    print (f"El resultado total de las operaciones: {resigual}")