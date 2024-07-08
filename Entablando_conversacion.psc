Algoritmo Entablando_conversacion
	Escribir "Hola, Como estas?";
	Leer estado;
	Escribir "Estoy Bien";
	Escribir "Como te llamas?";
	Leer nombre;
	Escribir "yo me llamo luis, cuantos años tienes?";
	Leer edad;
	Escribir "yo tengo 18 años, estas estudiando en el duocuc?";
	Leer estudio;
	Si estudio== "Si" Entonces
		Escribir "yo tambien estudio en el duocuc";
	SiNo
		Escribir "en que universidad estudias";
	Fin Si
	escribir "Que estas estudiando?";
	Leer carrera;
	Si carrera== "Ingenieria Informatica" Entonces
		Escribir "yo tambien estudio ingenieria informatica";
	SiNo
		Escribir "yo estudio ingenieria informatica";
	Fin Si
	escribir "En que horario";
	Leer Horario;
	Escribir "Que coincidencia, Yo estudio Vespertino";
	Escribir "Bueno me tengo que ir que tengo clases ahora";
	Leer Despedida;
	Escribir "Chao, Cuidate";
	
FinAlgoritmo
