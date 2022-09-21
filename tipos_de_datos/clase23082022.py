# 1. Imprimir la cadena de texto (string): “¡Hola mundo!”

#print("hola mundo")

#2. Solicitar al usuario por consola su nombre e imprimirlo con el siguiente formato:
#“Hola %nombre!”. Donde nombre es el nombre que el usuario introdujo. (Buscar
#cómo obtener datos ingresados por consola y formateo de cadenas de texto).

#nombre = input("Ingresa tu nombre: ")
#print('Hola',nombre)

#3. Almacenar la cadena “¡Hola mundo!” en una variable e imprimir

# var = 'hola mundo'
# print(var)

# 4. Escribir un programa que pregunte el nombre del usuario en la consola y un número
# entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
# como el número introducido.

# nombre = input("Ingresa tu nombre: ")
# veces = int(input("Ingresa un numero "))
# print((nombre + "\n") * veces)

# 5. Crear la variable que contenga tu primer nombre.
# Luego:
# A. Imprimir la variable por pantalla.
# B. Imprimir el ID por pantalla.
# C. Pasar ese nombre a mayúsculas e imprimirlo por pantalla.

# nombre = 'juan'
# print(nombre)
# print(id(nombre))
# print((nombre.upper()))

# 6.Realizar la siguiente operación aritmética e imprimir su resultado por pantalla.
# También imprimir el tipo de dato resultante y su id.

# operacion = ((3+2)/(2*5))**2
# print(operacion)
# print(id(operacion))

# 7. Pregunte el nombre del usuario en la consola y después de que el usuario lo
# introduzca muestre por pantalla <NOMBRE> tienen> letras, donde <NOMBRE> es el
# nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

# nombre = input('Ingresa tu nombre: ')
# n = len(nombre)
# print(f"{nombre.upper()} tiene {n} letras")

# 8. Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión
# donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por
# ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de
# teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo
# y la extensión

# telefono = input('Ingrese su numero de teléfono: ')
# print(telefono[4:13])

# 9. Solicitar al usuario la cantidad de horas que trabaja en el día, y el coste por hora.
# Después mostrar por consola la paga que le corresponde.

# cantidad_horas = int(input('Ingrese la cantidad de horas trabajadas: '))
# costo_hora = int(input('Ingrese el costo por hora: $ '))
# print('El pago correspondiente será de $',cantidad_horas*costo_hora)

# 10. Un vivero tiene mucho éxito en dos de sus plantas: monsteras y suculentas. Suele
# hacer venta por correo y la empresa de logística les cobra por peso de cada paquete
# así que deben calcular el peso de las plantas que saldrán en cada paquete a
# demanda. Cada monstera pesa 1,5kg y cada suculenta 300g. Escribir un programa
# que lea el número de monsteras y suculentas vendidas en el último pedido y calcule
# el peso total del paquete que será enviado. El peso de las monsteras sera ingresado
# en kg, el de las suculentas en gramos y el peso resultante debe ser impreso por
# consola en kg hasta dos decimales.

# mosteras = int(input('Ingrese el peso de monsteras vendidas: '))
# suculentas = int(input('Ingrese el peso de suculentas vendidas: '))

# total = mosteras + suculentas / 1000
# print('%.2f' % total)


# 11. Escribir un programa que lea por teclado 3 números y los guarde en una lista. Luego
# debe mostrar la suma y el producto de los elementos. Aquí tendrás que usar el
# método input()
# lista = []
# uno = int(input('1 - Ingresa un numero: '))
# dos = int(input('2 - Ingresa un numero: '))
# tres = int(input('3 - Ingresa un numero: '))

# lista = [uno,dos,tres]
# suma = lista[0]+lista[1]+lista[2]
# producto = lista[0]*lista[1]*lista[2]

# print('La lista',lista)
# print('Suma',suma)
# print('Producto',producto)

# 12. Dada la siguiente lista
# candidatos = ['De Gasperi', 'Nenni', 'Brosio', 'Giannini', 'Pacciardi']

# A. Imprimir el primer elemento.
# B. Imprimir el segundo elemento.
# C. Imprimir el último elemento.

# print(candidatos[0],'-',candidatos[1],'-',candidatos[-1])


# 13. Crear un diccionario a partir de las siguientes listas donde anio sea la clave y
# porcentaje sea el valor.
# anio = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
# porcentaje = [2314, 84, 17.5, 7.4, 3.9, 1.6 , 0.1, 0.3, 0.7, -1.2]

# inflacion = zip(anio,porcentaje)
# print(tuple(inflacion))

# 14. Crear un diccionario con 5 personas, cuya clave sea el DNI y el dato sea el nombre de
# la persona.
# A. Obtener los DNI de las personas
# B. Obtener los nombres de las personas.
# C. Obtener los DNI y los nombres de las personas

# personas = {28901511 : 'Cristian', 15625084 : 'Maria', 32973434 : ' Laura', 92734591: 'Claudio',29876432: 'Jose'}

# print(personas.keys())
# print(personas.values())
# print(personas.items())

# 15. Dado el siguiente diccionario
poblacion = {'Caba' : 2890151, 'Pba' : 15625084, 'Catamarca' :
367828, 'Cordoba': 3308876}
# A. Eliminar la clave Caba.
# B. Modificar el valor de la clave Pba.
# C. Agregar la clave ‘Corrientes’ y asignarle el valor 992525.
del poblacion['Caba']
poblacion['Pba'] = 1
poblacion['Corrientes'] = 992525

# print(poblacion)

# 16. Dado el siguiente diccionario anidado:
candidatos = {
  "CandidatoA" : {
    "nombre" : "Tony",
    "apellido": "Blair",
    "anio" : 1953
  },
  "CandidatoB" : {
    "nombre" : "William",
    "apellido": "Hague",
    "anio" : 1961
  },
  "CandidatoC" : {
    "nombre" : "Charles",
    "apellido": "Kennedy",
    "anio" : 1959
  }
} 

# A. Imprimir el nombre del candidato A.
# B. Imprimir el año de nacimiento del candidato B.
# C. Imprimir el apellido del candidato C.
# D. Imprimir el año de nacimiento del candidato A.
# E. Imprimir el apellido del Candidato D. Manejar el error si este no existe.
# F. Sumar los años de nacimiento de los tres candidatos y guardarlos en una variable.
# Luego imprimirlo.

# print(candidatos['CandidatoA']['nombre'])
# print(candidatos['CandidatoB']['anio'])
# print(candidatos['CandidatoC']['apellido'])
# print(candidatos['CandidatoA']['anio'])
# print(candidatos.get("CandidatoD","No existe ese candidato"))
# anios = candidatos['CandidatoA']['anio']+candidatos['CandidatoB']['anio']+candidatos['CandidatoC']['anio']
# print(anios)

# 17. Declarar un diccionario con la cantidad de votos que recibió cada candidato de las
# elecciones del 2019. Crear un programa en el que el usuario ingrese el nombre del
# candidato, y muestre la cantidad de votos del mismo. Si el candidato no existe, debe
# devolver un error. (La función .get() puede resultar útil)


# votos = {'Fernandez' : 12946037, 'Macri' : 10811586, 'Lavagna' : 1649322, 'del Canio' : 579288, 'Gomez Centurio' : 457956, 'Espert' : 394207}
# nombre = input('Ingrese el nombre del candidato: ').capitalize()

# if nombre in votos:
#     print(votos[nombre])
# else: print('Ese candidato no existe') 

# print(votos.get(nombre,'Ese candidato no existe'))