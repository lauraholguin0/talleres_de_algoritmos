sexo=input("(mujer o hombre):")
edad=int(input("(edad en meses):"))
hemoglobina=float(input("(g):"))

if (0<=edad<=1) and (13<=hemoglobina<=26):
    print("no tiene anemia")
elif (0<=edad<=1) and (hemoglobina<13 or hemoglobina>26):
    print("tiene anemia")

elif(1<edad<=6) and (10<=hemoglobina<=18):
    print("no tiene anemia")
elif (1<edad<=6) and (hemoglobina<10 or hemoglobina>18):
    print("tiene anemia")

elif(6<edad<=12) and (11<=hemoglobina<=15):
    print("no tiene anemia")
elif (6<edad<=12) and (hemoglobina<11 or hemoglobina>15):
    print("tiene anemia")

elif(12<edad<=60) and (11.5<=hemoglobina<=15):
    print("no tiene anemia")
elif (12<edad<=60) and (hemoglobina<11.5 or hemoglobina>15):
    print("tiene anemia")

elif(60<edad<=120) and (12.6<=hemoglobina<=15.5):
    print("no tiene anemia")
elif (60<edad<=120) and (hemoglobina<12.6 or hemoglobina>15.5):
    print("tiene anemia")

elif(120<edad<=180) and (13<=hemoglobina<=15.5):
    print("no tiene anemia")
elif (120<edad<=180) and (hemoglobina<13 or hemoglobina>15.5):
    print("tiene anemia")

elif(sexo=="hombre")and (edad>180) and (14<=hemoglobina<=18):
    print("no tiene anemia")
elif (sexo=="hombre")and (edad>180) and (hemoglobina<14 or hemoglobina>18):
    print("tiene anemia")
else:
    print("datos incorrectos")