print("-----Minimarket Diego's-----")
print("---Ingresa los datos de la venta---")
cliente= input("Ingrese el nombre del cliente: ")
"""
precio1= int(input("Ingrese el precio del producto 1: "))
tipoProducto1= input("Ingrese el nombre del producto: ")
cantidad1= int(input("Ingrese la cantidad que lleva: "))
"""
precio1,tipoProducto1,cantidad1 = input("Ingresar los 3 datos ").split
print(f"precio1,tipoProducto1,cantidad1")
precio2= int(input("Ingrese el precio del producto 2: "))
tipoProducto2= input("Ingrese el nombre del producto: ")
cantidad2= int(input("Ingrese la cantidad que lleva: "))
precio3= int(input("Ingrese el precio del producto 3: "))
tipoProducto3= input("Ingrese el nombre del producto: ")
cantidad3= int(input("Ingrese la cantidad que lleva: "))


totalBruto= (precio1*cantidad1)+(precio2+cantidad2)+(precio3*cantidad3)
iva = round(totalBruto*0.19)
total= (totalBruto+iva)

print(f"CLIENTE: {cliente}")
print(f"TOTAL BRUTO: {totalBruto}")
print(f"IVA: {iva}")
print(f"TOTAL: {total}")


