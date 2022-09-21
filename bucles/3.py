# 3. Realizar un algoritmo que pida al usuario su Peso y su Altura de n personas. Calcule el IMC
# (índice de masa corporal), muestre por cada persona que se ingresa, el mensaje correspondiente (ver tabla). Además, debe mostrar la cantidad de personas que está en cada
# categoría
# Formula
# IMC = masa [kg] / (estatura [m])2

# Si este da menor que 18.5 es CATEGORÍA 1 .
# Si da entre 18.5 y 25 da CATEGORÍA 2.
# Si da entre 25 y 30 es CATEGORÍA 3.
# Si da mayor a 30 es CATEGORÍA4.

import math
 
peso = float(input("Ingrese su peso en Kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))
 
IMC = round(peso/math.pow(estatura,2),1)
 #Pow return x**y (x to the power of y).

print("Su IMC es de "+str(IMC))
if IMC < 18.5:
    print('CATEGORÍA 1')
elif IMC >= 18.5 and IMC < 25:
    print('CATEGORÍA 2')
elif IMC >= 25 and IMC < 30:
    print('CATEGORÍA 3')
elif IMC > 30:
    print('CATEGORÍA 4')
 
 
