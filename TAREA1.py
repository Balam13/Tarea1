from random import randint

from ModuloTarea1.PiedraPapelTijeta import juego


print ('Juegas sí(s)/no(n)')
eleccion = str(input())


while eleccion == 's' :

    print('Elije opcion:')
    print('1) piedra')
    print('2) papel')
    print('3) tijera')

    seleccion = int(input())
    numero = randint(0, 2)

    opciones = ['piedra', 'papel', 'tijera']

    tu_seleccion = opciones[seleccion - 1]
    print('Tu selección fue: ', tu_seleccion)


    seleccion_pc = opciones[numero]
    print('La PC jugó con : ',seleccion_pc)

    juego(seleccion, numero)

    print('Juegas sí(s)/no(n)')
    eleccion = str(input())


