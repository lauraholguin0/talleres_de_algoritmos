Algoritmo Salario
	Escribir "Dime tu salario base"
	Leer sb
	Escribir "Dime el valor tu primera venta"
	Leer pv
	Escribir "Dime el valor tu segunda venta"
	Leer sv
	Escribir "Dime el valor tu tercera venta"
	Leer tv
	vt<-pv+sv+tv
	porcentage<- vt/100
	total<-porcentage+sb
	Escribir "Tu 10% en ventas: " porcentage
	Escribir "Tu salario total es: " total
FinAlgoritmo
