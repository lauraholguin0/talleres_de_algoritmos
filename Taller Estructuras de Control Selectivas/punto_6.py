A=int(input(""))
B=int(input(""))
C=int(input(""))
D=int(input(""))
if (D > 5):
    C += 1
if (C > 5):
    B += 1
if (B > 5):
    A += 1
A = str(A)
B = str(B)
C = str(C)
D = str(D)
num = A + B + C + D
if len(num) > 4:
    B = str(int(B) * 0)
    C = str(int(C) * 0)
    D = str(int(D) * 0)
    num = A + B + C + D

elif len(num) > 3:
    C = str(int(C) * 0)
    D = str(int(D) * 0)
    num = A + B + C + D
print(num)