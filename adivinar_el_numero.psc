Proceso adivinar_el_numero
	Definir numeroadivinar, numerousuario, intentos, intentosusuario Como Entero;
	Definir acertado Como Logico;
	acertado <- falso;
	numeroadivinar <- azar(100);
	Escribir numeroadivinar;
	Escribir 'Ingresar intentos que quieras tener';
	Leer intentos;
	Mientras intentos>0 Y No acertado Hacer
		Escribir 'Ingresa su numero';
		Leer numerousuario;
		Si numerousuario==numeroadivinar Entonces
			Escribir 'Felicitaciones has adivinado el numero'; 
			acertado <- Verdadero;
		SiNo
			Escribir 'Intentelo nuevamente, te quedan ', intentos-1, " intentos";
		FinSi
		intentos <- intentos-1;
	FinMientras
	Si  NO acertado Entonces
		Escribir 'Lo siento no has adivinado';
	FinSi
FinProceso
