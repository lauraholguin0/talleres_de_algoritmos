lecturaAn=int(input(""))
lecturaAc=int(input(""))
lectura=(lecturaAn-lecturaAc)

if(0<lectura<=100):
    print(f"El monto a pagar es ${lectura*4600}")
elif(101<lectura<=300):
    print(f"El monto a pagar es ${lectura*8000}")
elif(301<lectura<=500):
    print(f"El monto a pagar es ${lectura*10000}")
elif(lectura>=501):
    print(f"El monto a pagar es ${lectura*12000}")
else:
    print("error ")
#tome esos valores ya que el ejercicio en el taller no es entendible  :3