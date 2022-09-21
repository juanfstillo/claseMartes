# 5) Tres candidatos obtienen valores que representan la opinión que tienen ciertas
# personas sobre ellos.
# Candidato 1: 75, 40, 15, 14, 9, 42, 73, 40, 29, 17, 78, 24, 89, 40, 53, 67, 65, 3, 27, 65
# Candidato 2: 81, 96, 95, 30, 46, 4, 46, 60, 1, 39, 59, 76, 65, 57, 18, 42, 2, 16, 47, 69
# Candidato 3: 87, 81, 55, 72, 72, 11, 1, 59, 72, 95, 92, 41, 77, 93, 24, 34, 62, 49, 18, 36
# Realizar una función que calcule y devuelva lo siguiente para cada candidato.
# a. Mínimo
# b. Máximo
# c. Media
# d. Moda
# e. Mediana
# f. Varianza
# g. Primer cuartil
# h. Tercer cuartil

candidato_1 = [75,40, 15, 14, 9, 42, 73, 40, 29, 17, 78, 24, 89, 40, 53, 67, 65, 3, 27, 65]
candidato_2 = [81, 96, 95, 30, 46, 4, 46, 60, 1, 39, 59, 76, 65, 57, 18, 42, 2, 16, 47, 69]
candidato_3 = [87, 81, 55, 72, 72, 11, 1, 59, 72, 95, 92, 41, 77, 93, 24, 34, 62, 49, 18, 36]

# a. Mínimo

def minimo_lista(lista):
    minimo = min(lista)
    return f'El numero minimo es {minimo}'

print(minimo_lista(candidato_1))
print(minimo_lista(candidato_2))
print(minimo_lista(candidato_3))
print('-----------------------')

# b. Máximo

def maximo_lista(lista):
    maximo = max(lista)
    return f'El numero maximo es {maximo}'

print(maximo_lista(candidato_1))
print(maximo_lista(candidato_2))
print(maximo_lista(candidato_3))
print('-----------------------')

# c. Media

def media(lista):
    return f'La media es {sum(lista)/len(lista)}'

print(media(candidato_1))
print(media(candidato_2))
print(media(candidato_3))
print('-----------------------')

# d. Moda

def moda(lista):
    repeticiones = 0

    for i in lista:
        n = lista.count(i)
        if n > repeticiones:
            repeticiones = n

    moda = [] #Arreglo donde se guardara el o los valores de mayor frecuencia 

    for i in lista:
        n = lista.count(i) # Devuelve el número de veces que x aparece en la lista.
        if n == repeticiones and i not in moda:
            moda.append(i)

    if len(moda) != len(lista):
        print('Moda: ', moda)
    else:
        print ('No hay moda')

moda(candidato_1)
moda(candidato_2)
moda(candidato_3)
print('-----------------------')

import statistics


print(statistics.median(candidato_1))
print(statistics.median(candidato_2))
print(statistics.median(candidato_3))
print('-----------------------')

# f. Varianza

print(statistics.variance(candidato_1))
print(statistics.variance(candidato_2))
print(statistics.variance(candidato_3))
print('-----------------------')


