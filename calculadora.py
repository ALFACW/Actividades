def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1/num2
   
def mostrar_menu():

    print("Seleccione la operación que desea realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == "1":
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("El resultado de la suma es:", suma(num1, num2))
    elif opcion == "2":
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("El resultado de la resta es:", resta(num1, num2))
    elif opcion == "3":
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
    elif opcion == "4":
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número (distinto de cero): "))
        print("El resultado de la división es:", division(num1, num2))
    elif opcion == "5":
        print("Has salido del programa")
        break
    else:
        print("Escoge una opcion valida ")
    




