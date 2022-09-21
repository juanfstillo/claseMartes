# 5. Se definen los números triangulares como los obtenidos de sumar los números naturales
# sucesivos 1, 2, 3.... Es decir, los primeros números triangulares son 1, 3, 6, 10, etc. Escribir un
# programa que muestre los N primeros números triangulares.

x = int(input('Números triangulares deseados '))
total_numeros, i, aux = 0, 1, 2

while total_numeros < x:
 print(i)
 i = i + aux
 aux += 1
 total_numeros += 1