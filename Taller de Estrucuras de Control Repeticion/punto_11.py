mujeres=0
hombres=0
si=0
no=0
edad=0
numper=int(input(""))
numper2=0
a=0
r=0
c=0
t=0
w=0
o=0
while(numper2<numper):
    respuesta_uno =str(input("¿consume licor(si o no)?: "))
    numper2=numper2+1
    if(respuesta_uno=="si"):
        si=si+1
        respuesta_dos=str(input("¿Eres mujer o hombre?: "))
        if(respuesta_dos=="mujer"):
            mujeres=mujeres+1
            respuesta_tres=int(input("¿Que edad tienes?: "))
            edad=edad+respuesta_tres
            respuesta_cuatro=int(input("¿Licor prefereido (1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro)?: "))
            if (respuesta_cuatro==1):
                a=a+1
            elif(respuesta_cuatro==2):
                r=r+1
            elif(respuesta_cuatro==3):
                c=c+1
            elif(respuesta_cuatro==4):
                t=t+1
            elif(respuesta_cuatro==5):
                w=w+1
            elif(respuesta_cuatro==6):
                o=o+1
        else:
            hombres=hombres+1
            respuesta_tres=int(input("¿Que edad tienes?: "))
            respuesta_cuatro=int(input("¿Licor prefereido (1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro)?: "))
            if (respuesta_cuatro==1):
                a=a+1
            elif(respuesta_cuatro==2):
                r=r+1
            elif(respuesta_cuatro==3):
                c=c+1
            elif(respuesta_cuatro==4):
                t=t+1
            elif(respuesta_cuatro==5):
                w=w+1 
            elif(respuesta_cuatro==6):
                o=o+1
    else:
        no=no+1
        continue