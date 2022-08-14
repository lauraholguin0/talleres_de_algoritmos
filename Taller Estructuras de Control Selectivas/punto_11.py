Temp=int(input("ingrese temperatura en grados Fahrenheit:"))
if(Temp>85):
    print(f"El deporte que puede practicar es: Natacion")
elif(70<Temp<=85):
    print(f"El deporte que puede practicar es: Tenis")
elif(32<Temp<=70):
    print(f"El deporte que puede practicar es: Golf")
elif(10<Temp<=32):
    print(f"El deporte que puede practicar es: Esquí")
elif(Temp<= 10):
    print(f"El deporte que puede practicar es: Marcha")

