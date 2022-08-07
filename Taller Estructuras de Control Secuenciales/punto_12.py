mate=float(input("ingrese la nota de matematicas:"))
mate_uno=float(input("ingrese la nota n1:"))
mate_dos=float(input("ingrese la nota n2:"))
mate_tres=float(input("ingrese la nota n3:"))

fisica=float(input("ingrese la nota de fisica:"))
fisica_uno=float(input("ingrese la nota n1:"))
fisica_dos=float(input("ingrese la nota n2:"))

quimica=float(input("ingrese la nota de quimica:"))
quimica_uno=float(input("ingrese la nota n1:"))
quimica_dos=float(input("ingrese la nota n2:"))
quimica_tres=float(input("ingrese la nota n3:"))

promat_uno=(((mate_uno+mate_dos+mate_tres)/3)*0.1)
prommat_dos=(mate*0.9)
prommattotal=(promat_uno+prommat_dos)

promfi_uno=(((fisica_uno+fisica_dos)/2)*0.2)
promfi_dos=(fisica*0.8)
promfitotal=(promfi_uno+promfi_dos)

promqui_uno=(((quimica_uno+quimica_dos+quimica_tres)/3)*0.15)
promqui_dos=(quimica*0.85)
promquitotal=(promqui_dos+promqui_uno)

print("este es el promedio de matematicas: ",prommattotal)
print("este es el promedio de fisica: ",promfitotal)
print("este es el promedio de quimica: ",promquitotal)