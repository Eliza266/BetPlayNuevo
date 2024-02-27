import os
def crearMenu():
    listMenu=[1,2,3,4,5]

    try:
        print(" 1.Registrar equipo\n 2.Registrar fecha de juego\n 3.Reportes\n 4.Marcadores por equipo \n5.salir")
        op=int(input('--'))
        if (op not in listMenu):
            os.system('cls')
            crearMenu()

    except:
        os.system('pause')
        crearMenu()
        
    else:
        return op