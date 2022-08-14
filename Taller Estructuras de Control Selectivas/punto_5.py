departamento_uno=int(input(""))
departamento_dos=int(input(""))
departamento_tres=int(input(""))
importeGlobal=(departamento_uno+departamento_dos+departamento_tres)
interes=(importeGlobal)*0.33
salario=int(input(""))
extra=salario*0.20
if(departamento_uno>=interes and departamento_dos>=interes and departamento_tres>=interes):
    print(f"ingreso total ${(salario+extra)*3} y ingreso individual de cada vendedor ${(salario+extra)}")
elif(departamento_uno>=interes and departamento_dos>=interes):
    print (f"los departamentos 1 y 2 vendieron más del 33% recibe ${(salario+extra)} cada uno")
elif(departamento_uno>=interes and departamento_tres>=interes):
    print (f"los departamentos 1 y 3 vendieron más del 33% recibe ${(salario+extra)} cada uno")
elif(departamento_dos>=interes and departamento_tres>=interes):
    print (f"los departamentos 2 y 3 vendieron más del 33% recibe ${(salario+extra)} cada uno")
elif(departamento_uno>=interes):
    print (f"el departamento 1 vendio más del 33% recibe ${(salario+extra)}")
elif(departamento_dos>=interes):
    print (f"el departamento 2 vendio más del 33% recibe ${(salario+extra)}")
elif(departamento_tres>=interes):
    print (f"el departamento 3 vendio más del 33% recibe ${(salario+extra)}")