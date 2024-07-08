year = int(input("Introduzca un año "))
if year < 1582:
    print("No esta dentro del periodo del calendario Gregoriano")
else:
    if year % 4 != 0:
      print("Año Comun")
    elif year % 100 !=0:
       print("Año Bisiesto")
    elif year % 400 != 0:
       print("Año Comun")
    else:
       print("Año Bisiesto")
