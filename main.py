import modulos.menu as mp
import modulos.registroequipos as re
import modulos.reportes as rt

#import modulos.reportes as r
if __name__ == '__main__':
    listaEquipos={}
    fechas={}
    local={}
    visitante={}
    principal=True
    while principal:
        re.titulo()
        op=mp.crearMenu()

        if (op==1):
            agreEquipo=True
            while agreEquipo:   
                re.requipos(listaEquipos)
                agreEquipo=bool(input('Ingrese S(si) si desea agregar otro equipo o enter(No)'))
            re.os.system('cls')
        elif (op==2):
            re.titulo()
            re.registFechas(listaEquipos, fechas)
        elif (op==3):
            re.titulo()
            marcador=True
            while marcador:
                re.titulo()
                opr=rt.crearMenuReportes()
                if (opr=='A'):
                     re.mayorGoles(listaEquipos)
                elif (opr=='B'):
                    re.mayorPuntos(listaEquipos)
                    
                elif (opr=='C'):
                     re.mayorPartidosGanados(listaEquipos)

                elif (opr=='D'):
                    re.totalGoles(listaEquipos)
                    
                elif (opr=='E'):
                    re.promedioGoles(listaEquipos)
               
                elif (opr=='F'):
                    marcador=False

        elif (op==4):
            re.mostrarTabla(listaEquipos)
            re.os.system('pause')
                    
        
        elif (op==5):
            principal=False
   

        