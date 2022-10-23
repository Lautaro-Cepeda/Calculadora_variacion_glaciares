repetir = "S"
while (repetir == "S" or repetir == "s"): 
    validar = int(input("\nSeleccione un glaciar: Descubierto(1) | Rocoso(2): "))
    while not (validar == 1 or validar ==2):
        print("\n¡Error! Opción invalida")
        validar = int(input("Seleccione un glaciar: Descubierto(1) | Rocoso(2): "))
    cantDecimales = int(input("Ingrese la cantidad de decimales que desea ver en cada resultado: "))
    def espesorMetros(superficie):
        espesor = (28.5 * (superficie)**0.357)
        return round(espesor,cantDecimales)
    def volumenKmCubico(superficie):
        volumen = (28.5 * (superficie**1.357)) / 1000
        return round(volumen,cantDecimales)
    def equivalenteH2OKmCubicoGlaciarDescubierto():
        equivH2O = volumenKmCubico(superf) * 0.85
        return round(equivH2O,cantDecimales)
    def equivalenteH2OKmCubicoGlaciarRocoso():
        equivH2O = volumenKmCubico(superf) * 0.50
        return round(equivH2O,cantDecimales)
    superf = float(input("\nIngrese la superfice en Kilometros cuadrados: "))
    print("\n\n*Espesor =",espesorMetros(superf),"Metros")
    print("*Superficie =",superf,"Km²")
    print("*Volumen =",volumenKmCubico(superf),"Km³")
    if validar == 1:
        print("*Equivalente de H₂O (glaciar descubierto) =",equivalenteH2OKmCubicoGlaciarDescubierto(),"Km³\n\n")
    elif validar == 2:
        print("*Equivalente de H₂O (glaciar rocoso) =",equivalenteH2OKmCubicoGlaciarRocoso(),"Km³\n\n")
    repetir = input("Desea ingresar otro glaciar? Si(S) | No(N): ")
input("Presione la tecla enter para cerrar")