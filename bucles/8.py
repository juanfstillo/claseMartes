tabla_desde = 1 #desde el 1...
tabla_hasta = 7 #...al 10
desde = 1 #multiplicaciones desde el 1...
hasta = 10 #...hasta el 10

for i in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {i}:') #mostramos una cabecera para cada tabla
	for j in range(desde, hasta + 1):
		print(f'{i} x {j} = {i * j}')
	print() #línea en blanco al final de cada tabla