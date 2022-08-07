l_An=int(input("ingrese la lectura anterior:(kw) "))
l_Ac=int(input("ingrese la lectura actual:(kw)"))
coxkw=int(input("ingrese el costo por kilovatio: "))
total=(l_Ac-l_An)*coxkw
print(f"el monto total a pagar en un mes de luz eléctrica es de: {total}")