Proceso sin_titulo
	Definir contador,limite,suma,resta,num1,num2,resultado,op Como Entero;
	op<-1;
	Mientras  op<>3 Hacer
		Escribir "Menu:";
        Escribir "1- Sumar";
        Escribir "2- Restar";
        Escribir "0- Salir";
        Escribir "Seleccione una opción: ";
		leer op;
		Si 	op<>3  Entonces
			Limpiar Pantalla;
		FinSi
	Si op=1  Entonces
		Escribir "Has seleccionado la opcion sumar";
		Escribir "Ingresa Numero 1";
		leer num1;
		Escribir "Ingresa Numero 2";
		leer num2;
		resultado<-num1+num2;
		escribir " El resultado de la suma es ", resultado;
	FinSi
	si op=2 Entonces
		Escribir "Has seleccionado la opcion restar";
		Escribir "Ingresa Numero 1";
		Leer num1;
		Escribir "Ingresa Numero 2";
		Leer num2;
		resultado<-num1-num2;
		escribir " El resultado de la resta es ", resultado;
	FinSi
	si op =0 Entonces
		Escribir " Has salido del programa";
		Leer num1;
		
	FinSi
FinMientras
	 
FinProceso
