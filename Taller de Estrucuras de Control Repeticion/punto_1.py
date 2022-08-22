n=int(input(""))
k=int(input(""))
numero = n
while(k<n):
    if(n>=k):
        numero = n-1
        n=numero
        print(numero)
