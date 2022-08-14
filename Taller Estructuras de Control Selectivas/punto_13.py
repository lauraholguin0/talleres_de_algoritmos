from posixpath import split
from datetime import date
today=date.today()
dia_h=today.day
mes_h=today.month
año_h=today.year

nacimiento=input("ingrese su fecha de nacimiento: (Año/Mes/Dia) ")
(año,mes,dia)=nacimiento.split("/")
año_n=int(año)
mes_n=int(mes)
dia_n=int(dia)
edad=0

if(mes_n==mes_h):
    if(dia_h>=dia_n):
        edad=año_h-año_n
    else:
        edad=(año_h-año_n)-1
elif(mes_h>mes_n):
    edad=año_h-año_n
else:
    edad=(año_h-año_n)-1

signo=""
if((22<=dia_n<30 and mes_n==11) or (1<dia_n<=21 and mes_n==12)):
    signo="Sagitario"
elif((22<=dia_n<30 and mes_n==12) or (1<dia_n<=20 and mes_n==1)):
    signo="Capricornio"
elif((21<=dia_n<30 and mes_n==1) or (1<dia_n<=19 and mes_n==2)):
    signo="Acuario"
elif((20<=dia_n<30 and mes_n==2) or (1<dia_n<=19 and mes_n==3)):
    signo="Piscis"
elif((21<=dia_n<30 and mes_n==3) or (1<dia_n<=20 and mes_n==4)):
    signo="Aries"
elif((21<=dia_n<30 and mes_n==4) or (1<dia_n<=21 and mes_n==5)):
    signo="Tauro"
elif((22<=dia_n<30 and mes_n==5) or (1<dia_n<=21 and mes_n==6)):
    signo="Geminis"
elif((22<=dia_n<30 and mes_n==6) or (1<dia_n<=22 and mes_n==7)):
    signo="Cancer"
elif((23<=dia_n<30 and mes_n==7) or (1<dia_n<=23 and mes_n==8)):
    signo="Leo"
elif((24<=dia_n<30 and mes_n==8) or (1<dia_n<=22 and mes_n==9)):
    signo="Virgo"
elif((23<=dia_n<30 and mes_n==9) or (1<dia_n<=22 and mes_n==10)):
    signo="libra"
elif((23<=dia_n<30 and mes_n==10) or (1<dia_n<=21 and mes_n==11)):
    signo="Escorpion"        
else:
    print(f"no valido")
    
print(edad)
print(signo)
