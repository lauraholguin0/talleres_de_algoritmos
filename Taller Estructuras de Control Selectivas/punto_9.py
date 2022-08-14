cliente=input("Nombre del cliente:")
monto=int(input(""))
if(monto<=50000):
    print(f"no hay descuento")
if(50000<monto<=100000):
    print(f"{cliente}: \nEl monto total es:{monto}\nEl monto a pagar es:{monto*0.05}\nRecibio un descuento del 5%")
if(100000<monto<=700000):
    print(f"{cliente}: \nEl monto total es:{monto}\nEl monto a pagar es:{monto*0.11}\nRecibio un descuento del 11%")
if(700000<monto<=1500000):
    print(f"{cliente}: \nEl monto total es:{monto}\nEl monto a pagar es:{monto*0.18}\nRecibio un descuento del 18%")
if(monto>1500000):
    print(f"{cliente}: \nEl monto total es:{monto}\n El monto a pagar es:{monto*0.25}\nRecibio un descuento del 25%")
