n=int(input(""))
n2=0
lim=0
while True:
    if(n2<n):
        n2=n2+1
        datos=int(input(""))
        if(lim<=datos):
            lim=datos
        else:    
            continue
    else:
        print (lim)
        break