variables = []  # Lista para almacenar las variables ingresadas

# Solicitar tres variables una por una
for i in range(3):
    entrada = input("Ingrese la variable {}: ".format(i+1))
    variables.append(entrada)

# Imprimir las variables ingresadas
print("Las variables ingresadas son:", variables)