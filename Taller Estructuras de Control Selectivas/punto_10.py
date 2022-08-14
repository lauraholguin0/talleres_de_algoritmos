categoria=int(input(""))
sueldobruto=int(input(""))
if(categoria==1 and sueldobruto==5000000):
    print(f"Para categoria {categoria}su nuevo sueldo bruto es de {sueldobruto+(sueldobruto*0.10)}")
elif(categoria==2 and sueldobruto==4300000):
    print(f"Para categoria {categoria}su nuevo sueldo bruto es de {sueldobruto+(sueldobruto*0.15)}")
elif(categoria==3 and sueldobruto==3600000):
    print(f"Para categoria {categoria}su nuevo sueldo bruto es de {sueldobruto+(sueldobruto*0.20)}")
elif(categoria==4 and sueldobruto==2000000):
    print(f"Para categoria {categoria}su nuevo sueldo bruto es de {sueldobruto+(sueldobruto*0.40)}")
elif(categoria==5 and sueldobruto==900000):
    print(f"Para categoria {categoria}su nuevo sueldo bruto es de {sueldobruto+(sueldobruto*0.60)}")
else:
    print(f"categoria o salario no conrresponden")