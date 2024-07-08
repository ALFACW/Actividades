Proceso ordenando_numeros
	Definir num1,num2,num3 Como Entero;
	Definir aux Como Entero;
	escribir "Escriba 3 numero num1,num2,num3, los cuales se ordenaran de menor a mayor";
	Leer  num1,num2,num3;
	Repetir 
		si num1>num2 Entonces
			aux = num1;
			num1 = num2;
			num2 = aux;
		FinSi
		si num2>num3 Entonces
			aux = num2;
			num2 = num3;
			num3 = aux;
	
		FinSi
	Hasta Que num1<num2 y num2<num3;
	Escribir num1;
	Escribir num2;
	Escribir num3;
	
	
	
FinProceso
