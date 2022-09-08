estudiantes={
}
suspendidos=[]
aprobados=[]
notas=[]
alumnos=int(input("ingrese numero de alumnos:"))
c=0
f=1
if alumnos<=10:
    for i in range(0,alumnos):
        c+=1
        nombre=input(f"Ingrese nombre del estudiante {c}: ")
        nota=int(input(f"Ingrese nota del estudiante {c} (0 a 100): "))
        estudiantes.update({c:{}})
        (estudiantes[c]).update({"nombre":nombre})
        (estudiantes[c]).update({"nota":nota})
    for f in range(1,(alumnos+1)):
        if((estudiantes[f]["nota"])<60):
            suspendidos.append(estudiantes[f]["nombre"])
        elif(estudiantes[f]["nota"])>=60:
            aprobados.append(estudiantes[f]["nombre"])
        notas.append(estudiantes[f]["nota"])
    print(f"Personas supendidas: {suspendidos}.")
    print(f"Personas aprobados: {aprobados}.")
    print(f"Media de las notas: {(sum(notas))/alumnos}.")
else:
    print("maximo 10 estudiantes")
