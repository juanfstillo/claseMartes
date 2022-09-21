# 1) Hacer una función que invocada como expo(x,n) devuelva el valor de x a la n.

def expo(x,n):
    return x**n

print(expo(2,2))

# 2) Hacer una función que dado un número indique si es par o impar, devolviendo True
# si es par o False si es impar.

def par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(par_impar(10))

# 3) Escribir una función que:
# a. Reciba 3 notas y calcule el promedio.
# b. Devuelva el promedio (return).

def promedio(a,b,c):
    total = (a+b+c)/3
    return total

print(promedio(4,6,8))

# 4) Utilizando la función anterior, hacer que imprima por pantalla si el alumno
# aprueba o no, siendo que se aprueba con un promedio mayor o igual a 7.

if promedio(7,8,9) >= 7:
    print("Aprobado")
else:
    print("Desaprobado")


