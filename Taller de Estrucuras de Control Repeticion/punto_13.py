# 13.	La Facultad de Ingeniería ha efectuado una prueba de admisión a un grupo de N estudiantes y, suponiendo que de cada prueba solicitamos el nombre del aspirante y el puntaje final, se le pide que usted elabore un programa que obtenga los siguientes resultados:

# •	Nombre del estudiante con el puntaje más alto
# •	Nombre del estudiante con el puntaje más bajo
# •	Puntaje máximo obtenido
# •	Puntaje mínimo obtenido
# •	Promedio de todos los puntajes obtenidos
# •	Porcentaje de estudiantes con puntajes inferiores al promedio
# •	Porcentaje de estudiantes con puntajes superiores al promedio
n=int(input(""))
contador=0
Na=""
Nb=""
Pa=0
Pb=0
puntaje=""
while (contador<n):
    contador=contador+1
    nombre=str(input(""))
    puntaje=int(input(""))
    if(Pa<=puntaje):
        Pa=puntaje
        Na=nombre
    if(puntaje<Pa or puntaje<Pb):
        Pb=puntaje
print(Pb,Pa)
#profe no pude la verdad no me dio la logica si lo explica en clase se lo agradeceria.
