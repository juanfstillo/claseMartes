# 6. En la Cámara de Diputados se levanta una encuesta con todos los integrantes con el fin de
# determinar qué porcentaje de los n diputados está a favor de modificar el mínimo no imponible del Impuesto a las Ganancias, qué porcentaje está en contra y qué porcentaje se abstiene de opinar.
numero_bancas = 257
numero_diputados_afirmativa = int(input('Ingrese numero de diputados a favor: '))
numero_diputados_negativa = int(input('Ingrese numero de diputados en contra: '))
numero_diputados_abstenciones = int(input('Ingrese numero de diputados que abstruvieron de opinar: '))



print(f'A favor % {round((numero_diputados_afirmativa/numero_bancas)*100,2)}')
print(f'En contra % {round((numero_diputados_negativa/numero_bancas)*100,2)}')
print(f'Abstenciones % {round((numero_diputados_abstenciones/numero_bancas)*100,2)}')
