import random
secret_number = random.randint(1,100)
print(secret_number)
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")


while True:
    usuario_number = int(input("Ingrese un numero "))  
   
    if usuario_number > secret_number:
        print("¡JA,JA!, ¡Estas atrapado en mi bucle!, intenta con un numero ¡Mas Bajo!")

    elif usuario_number < secret_number:
        print("¡JA,JA!, ¡Estas atrapado en mi bucle!, intenta con un numero ¡Mas Alto!")
        
    else:
    
        print("Bien hecho, muggle! Eres libre ahora.")
        break
  