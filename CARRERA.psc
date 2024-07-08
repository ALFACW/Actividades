Proceso CARRERA
	Definir valla como cadena;
	Escribir "Estas corriendo una carrera de 100 metros y tendras diferentes obstaculos";
	Escribir "Has encontrado una valla, Si: saltar la valla y No: seguir con la carrera (Responder con Si o No)";
	Leer valla;
	Si valla == "Si" Entonces
		Escribir "Has Saltado la valla";
		
	Sino Escribir "Puedes continuar la carrera";
	FinSi
	
	Definir tunel como cadena;
	Escribir "Sigues corriendo y te encuentras con un tunel de frente";
	Escribir "Has encontrado un tunel, Si: Atravesar el Tunel , No: Seguir con la carrera (Responder con Si o No)";
	Leer tunel;
	Si tunel == "Si" Entonces
		Escribir "Has Atravesado el Tunel";
	Sino Escribir "Puedes continuar corriendo";
	FinSi
	
	Definir laguna como cadena;
	Escribir "Has llegado casi a al fin de la carrera, pero te has encontrado con el obstaculo final";
	Escribir "Has encontrado una laguna, Si: Nadar hasta la meta , No: Seguir con la carrera (Responder con Si o No)";
	Leer laguna;
	Si laguna== "Si" Entonces
		Escribir "Debes nada 500 metros";
		Escribir "Has comenzado a nadar";
		Escribir "Te has agotado y debes devolver al inicio";
		Escribir "Has perdido la carrera";
	SiNo Escribir "Felicitaciones, has terminado la carrera con Exito";
		
	FinSi
	
FinProceso
