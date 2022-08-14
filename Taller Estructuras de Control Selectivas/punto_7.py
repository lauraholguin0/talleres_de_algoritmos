distanciarecorrida=int(input(""))
if(distanciarecorrida<300 and distanciarecorrida>1):
    print(f" por {distanciarecorrida}km paga 50000 COP")
elif(distanciarecorrida<1000 and distanciarecorrida>=300):
    print(f"por {distanciarecorrida}km paga {(70000+((distanciarecorrida-300)*30000))}COP")
elif(distanciarecorrida>=1000):
    print(f"por {distanciarecorrida}km paga {(150000+(((distanciarecorrida-1000)*9000)))} COP")
else :
    print(f"recorrer distancia minima de 1 km")