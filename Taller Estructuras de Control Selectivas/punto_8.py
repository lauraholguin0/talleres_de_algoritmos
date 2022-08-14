import math
p=int(input(""))
q=int(input(""))
pq=int((p^3)+(q^4)-(2*(p^2)))
if pq>680 :
    print(f"{p} y {q} satisfacen la expresion")
else:
    print(f"{p} y {q} no satisfacen la expresion")
