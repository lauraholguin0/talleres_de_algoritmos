inversion=int(input(""))
interesAnual=float(input(""))
interes=(inversion*interesAnual)/100
if(interes>=100000):
    print(interes+inversion)    
else:
    print(f"no invertir ganancia de ${interes}.")