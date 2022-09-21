# 2. En una playa de estacionamiento “Apart Car MicroCentro” se cobra de la siguiente manera: los 10 minutos son gratis, los siguientes 30 minutos tiene un valor de $ 25.00 y la hora $45.00. Se
# desea escribir un programa que, para 5 vehículos, reciba tanto minutos como horas y
# muestre lo que debe cancelar cada cliente. Tomando en cuenta que si es Martes o Sábado se
# hace un descuento del 20% sobre el monto total. Al finalizar el ingreso de los 5 vehículos, el
# programa debe mostrar cuántos vehículos permanecieron menos de media hora.

hora_precio = 45
menos_media_hora = 0
lista_clientes = []
for i in range(5):
    horas = 0
    minutos = 0
    dia = input(f'Ingrese dia para el vehiculo {i+1}: ').upper()
    
    auto_horas = int(input(f'Ingrese horas de permanencia para el vehiculo {i+1}: '))
    horas = horas + auto_horas
    
    auto_minutos = int(input(f'Ingrese minutos de permanencia para el vehiculo {i+1}: '))
    minutos = minutos + auto_minutos
    
    ##Calculo la cantidad de minutos totales
    total_minutos = minutos + (horas*60)
    ##Calculo los autos que estuvieron menos de media hora
    if total_minutos < 30:
        menos_media_hora = menos_media_hora + 1
    
    
    if total_minutos <= 10:
        lista_clientes.append(0)
    elif total_minutos > 10 and total_minutos <= 30:
        lista_clientes.append(25)
    else:
        lista_clientes.append(total_minutos/60 * hora_precio)

print(f'La cantidad de autos que estuvieron menos de media hora es/son ',menos_media_hora)
for i in range(len(lista_clientes)):
    print(f'Hola Cliente {i+1}')
    if (dia == 'MARTES' or dia == 'SABADO'):
        print(f'Debe pagar $ {round(lista_clientes[i]*0.80,2)}')
    else:
        print(f'Debe pagar $ {round(lista_clientes[i],2)}')
