ingresoAnual = float(input("Introduce su ingreso anual "))
if ingresoAnual < 85528:
    tax = ingresoAnual * 0.18 - 556.02
else:
    tax= (ingresoAnual - 85528) * 0.32 + 14839.02 
if tax < 0.0:
    tax=0.0
tax=round(tax,0)
print("El impuesto es: ", tax ," pesos")