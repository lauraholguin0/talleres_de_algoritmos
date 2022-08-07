total_cuota=int(input("cuanto es el pago total en cuotas:"))
contado=int(input("cuanto es al contado: "))
p=(((total_cuota-contado)/12)*100)/contado
print(f"el porcentaje de recargo por cueto es del : {p}%") 