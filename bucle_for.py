# Pedir al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra ingresada por el usuario a mayúsculas
user_word = user_word.upper()

# Devorar las vocales de la palabra ingresada por el usuario
for letra in user_word:
    if letra in ['A', 'E', 'I', 'O', 'U']:
        continue  # Omitir las vocales y pasar a la siguiente iteración
    else:
        print(letra)