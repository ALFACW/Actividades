nom= input("Ingrese el nombre del empleado ")
rut= input("Ingrese su rut ")
horasTrabajadas = int(input("Ingrese las horas trabajadas "))
valorHora= int(input("Ingrese el valor de la hora de trabajo "))
colacion = int(5500)
movilizacion= int(3000)
resultado = (valorHora*horasTrabajadas)+colacion+movilizacion
print(f"----------Liquidaciones de trabajador ----------")
print(f"NOMBRE DEL EMPLEADO: {nom}")
print(f"RUT EMPLEADO: {rut}")
print(f"MOVILIZACION: {movilizacion}")
print(f"ALIMENTACION: {colacion}")
print(f"PAGO EMPLEADO: {resultado}")
