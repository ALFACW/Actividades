print("-----Minimarket Diego's-----")
print("---Ingresa los datos de la venta---")
cliente = input("Ingrese el nombre del cliente: ")


entrada1 = input("Ingrese el nombre del producto, su valor y cantidad separados por una coma: ")
entrada2 = input("Ingrese el nombre del segundo producto, su valor y cantidad separados por una coma: ")
entrada3 = input("Ingrese el nombre del tercer producto, su valor y cantidad separados por una coma: ")


nombre_producto1, valor_producto1, cantidad_producto1 = entrada1.split(',')
nombre_producto2, valor_producto2, cantidad_producto2 = entrada2.split(',')
nombre_producto3, valor_producto3, cantidad_producto3 = entrada3.split(',')

valor_producto1 = int(valor_producto1)
cantidad_producto1 = int(cantidad_producto1)
valor_producto2 = int(valor_producto2)
cantidad_producto2 = int(cantidad_producto2)
valor_producto3 = int(valor_producto3)
cantidad_producto3 = int(cantidad_producto3)


impuesto = 0.19
total_bruto = int(valor_producto2*cantidad_producto1)+int(valor_producto2*cantidad_producto2)+int(valor_producto3*cantidad_producto3)
iva= int(total_bruto*impuesto)
total = int(total_bruto+iva)


print("")
print("CLIENTE:", cliente)
print("TOTAL BRUTO:", total_bruto)
print("IVA:", iva)
print("TOTAL:", total)
