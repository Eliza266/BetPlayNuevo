import os
def crearMenuReportes():
    listMenu=['A','B','C','D','E','F']
    opciones=[" A.Equipo goleador \n B.Equipo con mayor puntaje\n C.Equipo con mayor numero de partidos ganados\n D.Total goles anotados por todos los equipos\n  E.Promedio de goles por torneo \n F.Volver al menu anterior"]
    os.system('cls')
     
    for i in opciones:
        print(i)


    try:
        op=input('--').upper()
        print(op)
        if (op not in listMenu):
            crearMenuReportes()

    except:
        print('Error en la opcion')
        os.system('pause')
        crearMenuReportes()
        
    else:
        return op