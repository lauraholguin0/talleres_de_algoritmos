salariobruto=int(input(""))
if(salariobruto>900000):
    print(int(salariobruto*1.15))
elif(salariobruto<=900000):
    print(int(salariobruto*1.12))