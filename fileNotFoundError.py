#Cuando el archivo no existe o a ruta esta mal declarada
# w = escribir 
try:
    archivo = open("archivo-que-no-existe.txt","r")
except FileNotFoundError:
    print("No existe tal archivo")




