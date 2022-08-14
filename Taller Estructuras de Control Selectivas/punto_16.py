A=int(input(""))
B=int(input(""))
C=int(input(""))

D=(B**2)-4*(A*C)
print(f"valor de D: {D}")
if D==0:
    x1=-B/(2*A)
    print(f"x1=x2= {x1}")
elif D>0:
    x1=(-B+((B**2-4*A*C)/(2*A))**1/2)
    x2=(-B-((B**2-4*A*C)/(2*A))**1/2)
    print(f" x1= {x1}\nx2= {x2}")
elif D<0:
    print("no tiene solucion en los Reales")