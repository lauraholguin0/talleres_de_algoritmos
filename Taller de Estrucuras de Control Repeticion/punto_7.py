datos=input("")
(x,m)=datos.split(" ")
m=int(m)
x=int(x)
nuevaexp=0
while (nuevaexp==0):
    if(0<x<=3 and 10<=m<=((2**32)-1)):
        nuevaexp=x*m
        print(nuevaexp)
    else:
        nuevaexp=nuevaexp+1
        print(" ")
