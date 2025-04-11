def leap_year():
    año = int(input("Ingrese un año: "))
    año_centenario = (año/100 == año//100) 
    if (año/4 == año//4) and (not año_centenario):
        print(f"El año {año} es bisiesto")
    elif año_centenario and (año/400 == año//400):
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
