contador=0
while(contador==0):
    contraseña=int(input(""))
    if(contraseña!=2002):
        print ("Sehna Invalida")
        continue
    elif(contraseña==2002):
        print("Acesso Permitido")
        contador=contador+1