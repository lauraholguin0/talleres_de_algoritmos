montototal=int(input(""))
if(montototal>=5000000):
    print(f"inversion $ {(montototal*0.055)}")
    print(f"prestamo banco $ {(montototal*0.30)}")
    print(f"credito $ {(montototal*0.65)}")
    print(f"interes ${((montototal*0.65)*0.2)}")
elif(montototal<500000):
    print(f"inversion $ {(montototal*0.70)}\ncredito ${(montototal*0.30)}\ninteres $ {(montototal*0.30)*0.20}")   