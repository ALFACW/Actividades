Proceso marios_bross
	definir bloques,monedas,romper,acumulador,derribar Como Entero;
	definir baches,saltos,contador Como Entero;
	definir escaleras,altura,escalar Como Entero;
	bloques <- 3;
	derribar <- 3;
	monedas <- azar(50)+1;
	acumulador=0;
	Repetir
		Escribir "Mario ha encontrado unos bloques el cual debe derribar para obtener las monedas";
		bloques=bloques-1;
		escribir "";
	
		Escribir "Quieres derribar el bloque 1:Si y 2:No";
		leer romper;
		Si romper=1 Entonces
			Escribir "Felicidades has obtenido ", monedas, " monedas, puedes seguir con la aventura";
			acumulador=acumulador+monedas;
			escribir "";
		SiNo
			escribir "";
			Escribir "Has obtenido 0 monedas, puedes continuar la aventura";
			Escribir  "";
		FinSi
	Repetir
		Escribir "Mario ha encontrado otro bloque el cual debe derribar para obtener las monedas";
		
		Escribir "Quieres derribar el bloque 1:Si y 2:No";
		leer romper;
		monedas <- azar(50)+1;
		bloques=bloques-1;
		Si romper=1 Entonces
			Escribir "has obtenido ", monedas, " monedas, puedes seguir con la aventura";
			acumulador=acumulador+monedas;
			Escribir "";
		SiNo
			Escribir "Has obtenido 0 monedas, puedes continuar la aventura";
			escribir "";
		FinSi
	Hasta Que bloques=0
hasta que bloques=0 
escribir "";
Escribir  "";
    Escribir "Has conseguido terminar la mision y has conseguido ", acumulador, " monedas en total";
	escribir "";
	escribir "";
	
	Escribir "Luego de recolectar las monedas, mario se ha encontrado con varios baches el cual debe saltar, si no caera al precipicio, ¡¡¡AYUDALO A LLEGAR DONDE LA PRINCESA!!!";
	baches <- 5;
	contador = 0;
	Repetir
		escribir "Mario ha encontrado ",baches," baches en el camino, ayudalo a saltarlos (1:Saltar , 2:No Saltar)";
		baches=baches-1;
		contador = (contador+baches)+1;
		Leer saltos;
		si saltos=1 Entonces
			
			Escribir "Felicidades has saltado el bache, puedes continuar tu aventura para salvara la princesa";
		SiNo
			
			Escribir "Has caido por el precipicio, intentalo nuevamente.";
		FinSi
		Repetir
			escribir "te quedan ",baches," baches para llegar donde la princesa, ayudalo a saltarlos (1:Saltar , 2:No Saltar)";
			baches=baches-1;
			Leer saltos;
			si saltos=1 Entonces
				
				Escribir "Felicidades has saltado el bache, puedes continuar tu aventura para salvara la princesa";
			SiNo
				
				Escribir "Has caido por el precipicio, intentalo nuevamente.";
			FinSi
		Hasta Que baches=0
	Hasta Que baches=0
	Escribir "has saltado ",contador, " baches, cada ves estas mas cerca de terminar tu mision";
	Escribir "";
	Escribir "";
	
	Escribir "OHHHHH NOO, Mario se ha encontrado con la mision final";
	Escribir "Son escaleras que van aumentando su tamaño una tras otras, ayuda a mario a finalizar la mision y rescatar a la princesa, comencemos";
	escribir "";
	
	escaleras<-3;
	altura=azar (20);
	contador=0;
	
	Escribir " Mario tiene que subir ", escaleras, " escaleras, tienes que ayudarlo";
	Escribir "";
	Repetir 
		Escribir  "La primera escalera tiene una altura de ",altura, " metros, (1:Escalar y 2; No escalar)";
		leer escalar;
		escaleras = escaleras-1;
		altura = azar(20);
		contador =contador+altura;
		Si escalar=1 Entonces
			escribir "Has escalado la primera escalera";
			escribir "";
		SiNo
			escribir "Has fallado";
		FinSi
		
		Repetir 
			Escribir  "La segunda escalera tiene una altura de ",altura, " metros, (1:Escalar y 2; No escalar)";
			leer escalar;
			escaleras = escaleras-1;
			altura = azar(20);
			
			contador =contador+altura;
			Si escalar=1 Entonces
				escribir "Has escalado la segunda escalera";
				escribir "";
			SiNo
				escribir "Has fallado";
			FinSi
			
			Repetir 
				Escribir  "La tercera escalera tiene una altura de ",altura, " metros, (1:Escalar y 2; No escalar)";
				leer escalar;
				escaleras = escaleras-1;
				altura = azar(20);
				contador =contador+altura;
				Si escalar=1 Entonces
					escribir "Has escalado la tercera escalera";
					escribir "";
				SiNo
					escribir "Has fallado";
				FinSi
				
			hasta que escaleras =0
		Hasta Que escaleras=0
	Hasta Que escaleras=0
	Escribir "";
	Escribir "Felicidades has terminado la mision, has rescatado a la princesa";
	Escribir "Has escalado un total de ",contador, " metros";
FinProceso
	
	

