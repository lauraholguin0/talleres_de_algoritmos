mujeresm=0
mujeres=0
hombres=0
si=0
no=0
edad=0
edadmuj=0
edadhom=0
numper=int(input(""))
numper2=0
a=0
r=0
y=0
ycontador=0
c=0
t=0
w=0
z=0
o=0
x=0
homnoa=0
while(numper2<numper):
    numper2=numper2+1
    sexo=str(input("¿Eres hombre o mujer?: "))
    if(sexo=="mujer"):
        mujeres=mujeres+1
        edadmuj=int(input("¿Que edad tiene?:"))
        respuesta_cuatro=int(input("¿Licor prefereido (1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro)?: "))
        if (respuesta_cuatro==1):
            a=a+1
        elif(respuesta_cuatro==2):
            r=r+1
        elif(respuesta_cuatro==3):
            c=c+1
            y=respuesta_tres+y
            ycontador=ycontador+1
        elif(respuesta_cuatro==4):
            t=t+1
        elif(respuesta_cuatro==5):
            w=w+1
            z=z+1
        elif(respuesta_cuatro==6):
            o=o+1
    else:
        if(sexo=="hombre"):
            hombres=hombres+1
            respuesta_tres=int(input("¿Que edad tiene?:"))
            x=respuesta_tres
            if(20<=x<=25):
                respuesta_cuatro=int(input("¿Licor prefereido (1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro)?: "))
                if (respuesta_cuatro==1):
                    a=a+1
                elif(respuesta_cuatro==2):
                    r=r+1
                    homnoa=homnoa+1
                elif(respuesta_cuatro==3):
                    c=c+1
                    homnoa=homnoa+1
                    y=respuesta_tres+y
                    ycontador=ycontador+1
                elif(respuesta_cuatro==4):
                    t=t+1
                    homnoa=homnoa+1
                elif(respuesta_cuatro==5):
                    w=w+1 
                    homnoa=homnoa+1
                    z=z+1
                elif(respuesta_cuatro==6):
                    o=o+1
                    homnoa=homnoa+1
            elif(respuesta_tres==respuesta_tres):
                respuesta_cuatro=int(input("¿Licor prefereido (1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro)?: "))
                if (respuesta_cuatro==1):
                    a=a+1
                elif(respuesta_cuatro==2):
                    r=r+1
                elif(respuesta_cuatro==3):
                    c=c+1
                    y=respuesta_tres+y
                    ycontador=ycontador+1
                elif(respuesta_cuatro==4):
                    t=t+1
                elif(respuesta_cuatro==5):
                    w=w+1
                    z=z+1
                elif(respuesta_cuatro==6):
                    o=o+1
    if(0<edadmuj<=17):
        mujeresm=mujeresm+1
    continuar=str(input("¿quiere continuar?:"))
    if(continuar=="si"):
        continue
    else:
        break
print(f"Total de personas encuestadas que consumen licor{si}")
print(f"mujeres menores de edad{mujeresm}")
print(f"hombres que no toman aguardiente y tienen entre 20 y 25 años: {homnoa}")
print(f"Promedio de edad de las personas que consumen cerveza.{y/ycontador}")
print(f"Porcentaje de personas que consumen whisky en relación con el total encuestado.{(numper*z)/100}")
#profe fue lo que entendi de que funciona funciona.