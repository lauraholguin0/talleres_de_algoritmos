estudiantes=int(input("ingrese numero de estudiantes: "))
mujeres=int(input("ingrese numero de mujeres: "))
hombres=int(input("ingrese numero de hombres: "))
pormujeres=(100*mujeres)/estudiantes
porhombre=(100*hombres)/estudiantes
print(f"el porcentaje de mujeres es: {pormujeres}% \nel porcentaje de hombre: {porhombre}%")