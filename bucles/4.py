# 4.Escribir un programa que pida números enteros hasta que se introduzca un cero. Debe
# imprimir la suma y el promedio de todos los números introducidos.

suma= 0
promedio = 0
cantidad= 0
nro= int(input("Ingrese un valor entero, pulse 0 si desea salir: "))
while nro >0:
    suma=suma+nro
    cantidad = cantidad + 1
    promedio= suma / cantidad
    nro= int(input("Ingrese un valor entero, pulse 0 si desea salir: "))
print ("Hasta luego")
print ("El promedio es ",promedio)
print ("La suma es ",suma)