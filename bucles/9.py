# 9. Ingresar dos números enteros. Verificar si el primero es menor que el segundo. En caso
# afirmativo mostrar todos los números comprendidos entre ellos en secuencia ascendente, incluyendo los extremos. En caso contrario mostrar un cartel.

a = int(input("A-Ingresa un numero: "))

b = int(input("B-Ingresa otro numero: "))

if(a<b):
    while a <= b:
        print(a)
        a += 1
else:
    print("La variable a no es menor que la variable b")
