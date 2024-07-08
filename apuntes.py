#Listas: son coleecion de datos ordenados y modificables. []

numeros = [1,2,3,4,5,6,7,8,9]
nombres = ["Raul", "Pedro", "Cosme Fulanito"]
mixta = [1,"Cosme Fulanito", True, 1.4]
print(numeros)
print(numeros[6])
print(numeros[-1])

#Tuplas: colecciones de datos ordenados e inmutables. ()

coordenadas = (10,20)
meses = ("Enero","Febrero","Marzo")
print(meses)
print (meses[-1])

#Conjuntos: son datos desordenados y no indexados, de elementos unicos, se definen utilizando llaves {} o la funcion set()

#conjunto de numeros

numerosPrimos = {2,3,5,7,11}

#conjunto de letras

lenguaje= set("Python3")
#Agregar elementos a un conjunto
numerosPrimos.add(13) # agregar un elemento a un conjunto
print(numerosPrimos)

#Eliminar datos de un conjunto 
numerosPrimos.remove(3)
print(numerosPrimos)

lenguaje.remove("3")
print(lenguaje)

#Diccionarios: son colecciones de datos pares, clave: valor {}

alumno = {
    "Nombre": "Juanito",
    "Edad": 30,
    "Beca": True,
    "Ciudad": "Puerto Montt",
    "Provincia": "Llanquihue",
    "Comuna": "Llanquihue",

}
print(alumno)
#Imprimir datos especificos de un diccionario
print(alumno["Beca"])
#Modificar un dato especifico de un diccionario
alumno["Edad"]=50
print(alumno)
#Agregar una nueva clave: valor
alumno["Altura"]=1.20
alumno["Nombre"]="Miguelito"
print(alumno)

#Como saber de que tipo es una variable con type

print (type(numerosPrimos))
print (type(alumno))

#Obtener un dato del usuario

datoUsuario= int(input("Ingrese un numerillo "))

print(datoUsuario)
print (type(datoUsuario))

#Numeros complejos 

numeroComplejo = 5j #Crea un numero con parte real 5 y la parte imaginaria seria j

#Datos de tipo rango o range
#Crea un rango desde el 0 al 8

rango = range(9)
#mostras rango 
print(rango)
#Mostra tipo de dato 
print(type(rango))

"""
frozenset: Es un tipo de coleccion similiar a un set() regular, con la diferencia 
que los datos no se pueden modificar, eliminar o actualizar (inmutables)

"""

frutas = frozenset({"Arandanos","Manzana","Sandia"})
print(frutas)
print(type(frutas))

"""
Bytes: Es un tipo de dato inmutable, 
representa un tipo de dato desde 0 a 255, se puede crear desde una 
cadena de caracteres, una lista, enteros o un objeto byte existente.
Principalmente se utiliza para almacenar datos binarios como archivos o 
datos de red.

"""
#Crear un objeto byte a partrir de una cadena de caracteres.
#Crear un objeto byte a partir de una cadena utilizando la codificacion utf-8

tipoByte = bytes("Holis", "utf-8")
print(tipoByte)
print (type(tipoByte))


#Crear un objeto bytes a partir de numero enteros.

objetoByte = bytes([72,111,108,97])
print(objetoByte)

"""
Abecedario en Byte
A: 65
B: 66
C: 67
D: 68
E: 69
F: 70
G: 71
H: 72
I: 73
J: 74
K: 75
L: 76
M: 77
N: 78
O: 79
P: 80
Q: 81
R: 82
S: 83
T: 84
U: 85
V: 86
W: 87
X: 88
Y: 89
Z: 90

a: 97
b: 98
c: 99
d: 100
e: 101
f: 102
g: 103
h: 104
i: 105
j: 106
k: 107
l: 108
m: 109
n: 110
o: 111
p: 112
q: 113
r: 114
s: 115
t: 116
u: 117
v: 118
w: 119
x: 120
y: 121
z: 122

"""

"""
ByteArray: Un tipo de dato mutable, lo que significa que su contenido puede
ser modificado.
0-25
se utiliza cuando tenemos que manipular datos de forma dinamica como en
lectura y escriturade flujo datos.
"""
#Crear un bytearray ()
byteArray = bytearray("Holiwi", "utf-8")   
print(byteArray)  
print(type(byteArray))

byteArray[0]= 115
byteArray[5]= 122
print(byteArray)

"""
¿qué es utf-8?
UTF-8 es un formato de codificación de caracteres Unicode e ISO 10646 
que utiliza símbolos de longitud variable.

"""
#Memoryview: es un tipo de dato que nos permite acceder y manipular de forma eficiente la memoria subyacente de un objeto

#Crear un vista de memoria (memoryview)

vista = memoryview(byteArray)
print(vista)
#Imprimir el primer elemento del array
print(vista[0])
#Modificar un elemento del array
vista[0]=74
print(vista[0])
print(byteArray)

#None : es un tipo de dato que representa la ausencia de valor.

variableNone = None
print(variableNone)

#Funciones def
nombre = "Diego"
def saludar(): 
    return "!Hola" + nombre +"!"

#Mensaje de saludo personalizar
mensajeSaludo = saludar("Estudiante")
print(mensajeSaludo)

"""
Actividad: Crear 2 archivos distintos nuevos con .py
1- solicitar dato del usuario de temperatura y el programa 
debera convertirlo de F° a C° e imprimir un mensaje 
por consola.
2- calculadora con funciones, basicas + , -, * y /
"""