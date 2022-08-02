Algoritmo sin_titulo
	escribir "nombre :"
	leer n
	escribir "primer apellido: "
	leer p1
	escribir "segundo apellido: "
	leer p2
	N<-Mayusculas(n)
	P1<-Mayusculas(p1)
	P2<-Mayusculas(p2)
	N1<-SubCadena(N,0,1)
	P_1<-subcadena(P1,0,1)
	P_2<-subcadena(P2,0,1)
	iniciales<-Concatenar(N1,P_1)
	NC<-Concatenar(iniciales,P_2)
	Escribir NC
FinAlgoritmo
