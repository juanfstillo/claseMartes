# 1-Realizar una función que aplique el nuevo IVA a un precio dado y otra que aplique un descuento.
# Finalmente, realizar una tercera que reciba un diccionario con precios y porcentajes de un carrito de compras y una de las funciones anteriores. Dicha función debe utilizar alguna de las funciones pasadas para aplicar IVA o descuento a los productos del carrito y devolver el precio final.

def descuento(precio, descuento):
    return precio - precio * descuento / 100

def iva(precio,iva):
    iva = 21
    return precio + precio * iva / 100

def total(carrito,function):
    total = 0
    for precio, descuento in carrito.items():
        total += function(precio, descuento)
    return total

#print('Precio con descuentos sin IVA: ', total({500:30, 700:5, 900:25}, descuento))
#print('Precio final sin descuento y con IVA: ', total({500:30, 700:5, 900:25}, iva))

# 2- Simular una calculadora científica que nos deje calcular
# Seno
# Coseno
# Tangente
# Exponencial

#  La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla el resultado.

from math import sin, cos, tan, exp

def funciones_calculadora():
    resp = input('Introduce la función a aplicar (seno, coseno, tangente, exponencial):').lower()
    n = int(input('Introduce un entero positivo: '))
    if resp == "seno":
        return sin(n)
    elif resp == "coseno":
        return cos(n)
    elif resp == "tangente":
        return tan(n)
    elif resp == "exponencial":
        return exp(n)

print(funciones_calculadora())
    
# 3- Crear un diccionario con las notas de los alumnos de la materia Física. Posteriormente, guardarlos en un archivo txt en tu computadora. Ver File handling.



