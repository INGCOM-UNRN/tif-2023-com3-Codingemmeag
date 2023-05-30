import cal_classica as cclass
import cal_fraction as cfrac
import cal_conversion as cconv

def la_calculadoreishon():
    inter = 0
    while inter != 1:
        try:
            menu = int(input("Ingrese 1 para entrar en la calculadora clasica \n2 para la calcuradora de fracciones\n3 para la calculadora de conversiones\no 4 para apagar: \n"))
            inter = 1
        except ValueError:
            print("El valor ingresado no es valido")
    inter = 0
    while menu != 4:
        if menu == 1:
            cclass.cal_classica()
        elif menu == 2:
            cfrac.cal_fracciones()
        elif menu == 3:
            cconv.cal_conversiones()
        while inter != 1:
            try:
                menu = int(input("Ingrese 1 para entrar en la calculadora clasica \n2 para la calcuradora de fracciones\n3 para la calculadora de conversiones\no 4 para apagar: \n"))
                inter = 1
            except ValueError:
                print("El valor ingresado no es valido")
        inter = 0    
    print("apagado")
    
la_calculadoreishon()