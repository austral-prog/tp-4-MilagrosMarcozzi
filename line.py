def line():
    print("TO DO")
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))
    
    recta = f"\tY = {A}X + {B}"
    
    y1 = (A*X1) + B
    y2 = (A*X2) + B
    
    P1 = f"({X1}, {y1})"
    P2 = f"({X2}, {y2})"
    
    distancia = math.sqrt(((X2 - X1)**2) + ((y2 - y1)**2))



    print (f"El coeficiente A de su ecuación de la recta es: {A}")
    print (f"El coeficiente B de su ecuación de la recta es: {B}")
    print (f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print (f"El coeficiente X2 de su ecuación de la recta es: {X2}\n")
    
    print ("Para la siguiente ecuación:")
    print (f"{recta}\n")
    
    print ("Dados los siguientes puntos:")
    print (f"\tP1 {P1}")
    print (f"\tP2 {P2}\n")
    
    print(f"La distancia entre ellos es: {distancia}")
