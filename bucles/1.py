# 1. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:

# a. La cantidad de valores ingresados negativos.
# b. La cantidad de valores ingresados positivos.
# c. La cantidad de múltiplos de 15.
# d. El valor acumulado de los números ingresados que son pares.

negativos = 0
positivos = 0
multiplos15 = 0
acumulados_pares = 0
for i in range(10):
    numero = int(input("Ingrese el numero: "))
    if numero < 0:
        negativos = negativos +1
    elif numero >= 0:
        positivos = positivos +1
    if numero % 15 == 0:
        multiplos15 = multiplos15 + 1
    if numero % 2 == 0:
        acumulados_pares = acumulados_pares + 1


print("Cantidad de negativos")
print(negativos)
print("Cantidad de positivos")
print(positivos)
print('Multiplos de 15')
print(multiplos15)

