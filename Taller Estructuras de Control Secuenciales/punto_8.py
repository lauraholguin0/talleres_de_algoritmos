import math
#entradas
a=float(input("ingrese a: "))
b=float(input("ingrese b: "))
c=float(input("ingrese c: "))
#cajanegra
s=((a+b+c)/2)
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area es :",area)
