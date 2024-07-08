print ("Bienvendio al mundo de la programacion")
nom = input("Para comenzar, ingrese tu nombre: ")
print(f"Bienvenido", nom)
x = int(input("Ingrese un valor para la variable x: "))
print(int((x**2)+(3*x)+1)/4)
codigo_de_area = str(+569)
prefijo= "@"

nombre = input("Ingrese su nombre: ")
nombre= nombre.upper()
edad= input("Ingrese su edad: ")
rut= input("Ingrese su RUT: ")
correo = input("Ingrese su correo: ")
correo = correo.upper ()
telefono = input("Ingrese su numero telefonico: " + codigo_de_area)


print(f"NOMBRE: {nombre}")
print(f"EDAD:  {edad}")
print(f"RUT: {rut}")
print(f"E-MAIL: {correo}")
print(f"TELEFONO: (+569) {telefono}")