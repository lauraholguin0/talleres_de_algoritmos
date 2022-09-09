usuarios = { 
"iperurena": { 
"nombre": "Iñaki", 
"apellido": "Perurena", 
"password": "123123" 
}, 
"fmuguruza": { 
"nombre": "Fermín", 
"apellido": "Muguruza", 
"password": "654321" 
}, 
"aolaizola": { 
"nombre": "Aimar", 
"apellido": "Olaizola", 
"password": "123456" 
} 
}
a=True
c=0
while a:
    if c<3:
        user=input("ingrese el nombre de usuario:")
        password=input("ingrese contraseña:")
        c+=1
        for i in usuarios:
            if i==user:
                    usuarios[user]["password"]==password
                    print((usuarios[user]["nombre"]),(usuarios[user]["apellido"]))
                    a=False
                    break
            else:
                continue
    else:
        print("maximo de 3 intentos")
        break

