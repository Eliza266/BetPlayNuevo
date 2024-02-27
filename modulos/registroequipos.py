import os
from tabulate import tabulate
def titulo():
    titulo= """
        ++++++++++++++++++++++++++++
        +     LIGA BETPLAY MENU    +
        ++++++++++++++++++++++++++++
        """
    print(titulo)
#-------------------------------------------------------------------------------------
# Registro de equipos
def requipos(listEquipos: dict):
    nombre = input(f"Ingrese el nombre del equipo: {len(listEquipos) + 1}\n")
    
    nuevoEquipo = {
        'nombre_equipo': nombre,
        'PJ': 0,
        'PG': 0,
        'PP': 0,
        'PE': 0,
        'GF': 0,
        'GC': 0,
        'TP': 0
    }
    
    listEquipos[nombre] = nuevoEquipo

# Seleccionar equipo
def SelecEquipo(listEquipos: dict, mensaje: str):
    SequipoBool = True
    while SequipoBool:
        print('*******EQUIPOS REGISTRADOS******')
        for equipo in listEquipos:
            print(f'{equipo}')

        opcion = input(f'\nSeleccione el equipo {mensaje}(ingrese el nombre del equipo): ')
        if opcion in listEquipos:
            equipoSeleccionado = opcion
            print(f'\nEl equipo seleccionado es: {equipoSeleccionado}')
            SequipoBool = False
        else:
            print(f'\nEl equipo "{opcion}" no se encuentra registrado.')
            input('Presiona Enter para continuar...')
            os.system('cls')

    return equipoSeleccionado

# Registro de fechas
def registFechas(listEquipos: dict, fechas: dict):
    fecha = int(input('Escriba la fecha que se le asignara al partido: '))

    equipoLocal = SelecEquipo(listEquipos, 'local')
    equipoVisitante = SelecEquipo(listEquipos, 'visitante')

    localGoles = int(input(f"Ingresa los Goles del equipo Local '{equipoLocal}': "))
    visitanteGoles = int(input(f"Ingresa los Goles del equipo Visitante '{equipoVisitante}': "))

    # PJ 
    listEquipos[equipoLocal]["PJ"] += 1
    listEquipos[equipoVisitante]["PJ"] += 1
    #GF
    listEquipos[equipoLocal]["GF"] += localGoles
    listEquipos[equipoVisitante]["GF"] += visitanteGoles
    #GC
    listEquipos[equipoLocal]["GC"] += visitanteGoles
    listEquipos[equipoVisitante]["GC"] += localGoles

    if (localGoles>visitanteGoles):
        listEquipos[equipoLocal]['PG'] +=1  #PG local
        listEquipos[equipoLocal]['TP'] +=3  #TP local
        listEquipos[equipoVisitante]['PP'] +=1  #PP para visitante
    elif(localGoles<visitanteGoles):
        listEquipos[equipoVisitante]['PG'] +=1  #PG visitante
        listEquipos[equipoVisitante]['TP'] +=3  #TP visitante
        listEquipos[equipoLocal]['PP'] +=1  #PP local
    else:
        listEquipos[equipoLocal]['PE'] +=1  #PE local
        listEquipos[equipoVisitante]['PE'] +=1  #PE visitante
        listEquipos[equipoLocal]['TP'] +=1  #TP local
        listEquipos[equipoVisitante]['TP'] +=1  #TP visitante

   
    fechas[fecha] = {"local": {**listEquipos[equipoLocal]}, "visitante": {**listEquipos[equipoVisitante]}}
    os.system('pause')

def mayorGoles(listEquipos:dict):
    mayor = 0
    nombre = ''
    for equipo, i in listEquipos.items():
        goles = i['GF']

        if goles > mayor:
            mayor = goles
            nombre = i['nombre_equipo']

    print(f'El equipo con el mayor número de goles es {nombre} con {mayor} goles.')
    os.system('pause')
    

def mayorPuntos(listEquipos:dict):
    mayor=0
    nombre=''
    for equipo,i in listEquipos.items():
        puntos= i['TP']
        if puntos > mayor:
            mayor = puntos
            nombre = i['nombre_equipo']
    print(f'El equipo con el mayor numero de Puntos es {nombre} con {mayor} Puntos ')
    os.system('pause')
    

def mayorPartidosGanados(listEquipos:dict):
    mayor=0
    nombre=''
    for equipo,i in listEquipos.items():
        puntos= i['PG']
        if puntos > mayor:
            mayor = puntos
            nombre = i['nombre_equipo']
    print(f'El equipo con el mayor numero de Partidos ganados es  {nombre} con {mayor} Partidos ')
    os.system('pause')
    
def totalGoles(listEquipos:dict):
    tGoles=0

    for equipo, i in listEquipos.items():
        tGoles += i['GF']
        print(f'El total de goles de todos los partidos es: {tGoles}')
    os.system('pause')

def promedioGoles(listEquipos):
    tgoles = 0
    tpartidos = 0

    for equipo, i in listEquipos.items():
        tgoles += i['GF']
        tpartidos += i['PJ']

    if tpartidos == 0:
        return 0  # division etre cero 

    promedio = tgoles / tpartidos
    print(f'El promedio de goles anotados por partido en el Torneo es: {promedio}')
    os.system('pause')
from tabulate import tabulate

def mostrarTabla(listEquipos):
    if not listEquipos:
        print("No hay equipos registrados.")
        return

    headers = ["Equipo", "PJ", "PG", "PP", "PE", "GF", "GC", "TP"]

    filas = []
    for equipo, estadisticas in listEquipos.items():
        fila = [
            estadisticas['nombre_equipo'],
            estadisticas['PJ'],
            estadisticas['PG'],
            estadisticas['PP'],
            estadisticas['PE'],
            estadisticas['GF'],
            estadisticas['GC'],
            estadisticas['TP']
        ]
        filas.append(fila)

    tabla = tabulate(filas, headers=headers, tablefmt="fancy_grid")
    print(tabla)
    os.system('pause')


    



    

    
   
    