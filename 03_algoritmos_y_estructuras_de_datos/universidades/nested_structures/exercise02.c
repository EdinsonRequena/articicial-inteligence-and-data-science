/*

Vamos a modificar el programa anterior para trabajar con tablas de estructuras, de forma que 
calculemos el KDA total de los cinco jugadores que han participado en la partida.
Para obtener dicho dato es necesario sumar por un lado los asesinatos de los cinco 
jugadores, por otro las muertes y finalmente las asistencias. 
Asimismo, calcularemos el ratio de ese KDA total. 

------------------------------resuelto por pasos--------------------------------

1)Definir tres constantes a la cual le pasaremos por valor la longitud de los vectores que crearemos mas adelante
	*)Esos vectores seran:
		kda
		longitud de las cadenas
		los 5 jugadores

2)Crear dos estructuras anidadas con las variables necesarias para almacenar los datos requeridos.
	a) los datos requeridos son:
		*)Nombre
		*)Nombre del campeon
		*)Nivel
		*)Experencia
		*)Asesinatos
		*)Muertes
		*)Asistencias

	b) ejemplo de codigo:
		typedef struct {
			char campeon[MAX_STR];
   			int kda[INFO];
		} juego;

		typedef struct {
    			char nombre[MAX_STR];
    			int nivel;
    			int experiencia;
    			juego partida;
		} invocador;

3)Crear las tablas estructuradas para poder almacenar los datos de los jugadores.
	*)ejemplo en codigo:

    		invocador usuario[5];
    		int kda_total[3];
    		double ratio;

4)Solicitar los datos que almacenaremos en las variables de la estructura creada previamente, sacar el ratio de de KDA y mostrar el ratio por pantalla.
	
	a) solicitar datos:
		*)Ejemplo en codigo:

    			printf("JUGADOR 1\n");
    			printf("¿Cuál es tu nombre de invocador? ");
    			scanf("%s", usuario[0].nombre);
    			printf("¿Con qué campeón has jugado tu última partida? ");
    			scanf("%s", usuario[0].partida.campeon);
    			printf("¿Cuántos asesinatos has hecho? ");
    			scanf("%d", &usuario[0].partida.kda[0]);
    			printf("¿Cuántas veces has muerto? ");
    			scanf("%d", &usuario[0].partida.kda[1]);
    			printf("¿Y cuántas asistencias has hecho? ");
    			scanf("%d", &usuario[0].partida.kda[2]);
    			ratio = (double) (usuario[0].partida.kda[0] + usuario[0].partida.kda[2]) / usuario[0].partida.kda[1];
    			printf("%s, tu KDA ratio con %s ha sido %.2lf.\n", usuario[0].nombre, ratio, usuario[0].partida.campeon);

	b)Sacar ratio y motrarlo por pantalla
		*)Ejemplo en codigo:

    			ratio = (double) (usuario[0].partida.kda[0] + usuario[0].partida.kda[2]) / usuario[0].partida.kda[1];
    			printf("%s, tu KDA ratio con %s ha sido %.2lf.\n", usuario[0].nombre, ratio, usuario[0].partida.campeon);

			// repetir con el resto de jugadores

5)Sumar el KDA de todos los jugadores, sacar el ratio de ese KDA y mostrarlo por pantalla.
	a)Sumar KDA y sacar el ratio
		*)ejemplo de codigo:

    		kda_total[0] = usuario[0].partida.kda[0] + usuario[1].partida.kda[0] + usuario[2].partida.kda[0] + usuario[3].partida.kda[0] + usuario[4].partida.kda[0];
    		kda_total[1] = usuario[0].partida.kda[1] + usuario[1].partida.kda[1] + usuario[2].partida.kda[1] + usuario[3].partida.kda[1] + usuario[4].partida.kda[1];
    		kda_total[2] = usuario[0].partida.kda[2] + usuario[1].partida.kda[2] + usuario[2].partida.kda[2] + usuario[3].partida.kda[2] + usuario[4].partida.kda[2];
    		ratio = (double) (kda_total[0] + kda_total[2]) / kda_total[1];

	b) mostrar por pantalla el nombre de los jugadores, el kda total y ratio de ese kda total
		*)ejemplo en codigo:

    			printf("\nUsuarios %s, %s, %s, %s y %s, el KDA de vuestra partida ha sido %d/%d/%d y su ratio %.2lf.\n", usuario[0].nombre, usuario[1].nombre, 				usuario[2].nombre, usuario[3].nombre, usuario[4].nombre, kda_total[0], kda_total[1], kda_total[2], ratio);  

			



*/

#include <stdio.h>

#define MAX_STR 128
#define INFO 3
#define USERS 5

typedef struct {
	char campeon[MAX_STR];
    int kda[INFO];
} juego;

typedef struct {
    char nombre[MAX_STR];
    int nivel;
    int experiencia;
    juego partida;
} invocador;

int main() {    
    invocador usuario[USERS];
    int kda_total[INFO];
    double ratio;

    printf("JUGADOR 1\n");
    printf("¿Cuál es tu nombre de invocador? ");
    scanf("%s", usuario[0].nombre);
    printf("¿Con qué campeón has jugado tu última partida? ");
    scanf("%s", usuario[0].partida.campeon);
    printf("¿Cuántos asesinatos has hecho? ");
    scanf("%d", &usuario[0].partida.kda[0]);
    printf("¿Cuántas veces has muerto? ");
    scanf("%d", &usuario[0].partida.kda[1]);
    printf("¿Y cuántas asistencias has hecho? ");
    scanf("%d", &usuario[0].partida.kda[2]);
    /* Fórmula ratio KDA: (K+A)/D. 
    Como verás vamos a reutilizar la variable ratio a lo largo del código, 
    pues una vez que la mostramos deja de interesarnos dicho valor. */
    ratio = (double) (usuario[0].partida.kda[0] + usuario[0].partida.kda[2]) / usuario[0].partida.kda[1];
    printf("%s, tu KDA ratio con %s ha sido %.2lf.\n", usuario[0].nombre, ratio, usuario[0].partida.campeon);  

    printf("\nJUGADOR 2\n");
    printf("¿Cuál es tu nombre de invocador? ");
    scanf("%s", usuario[1].nombre);
    printf("¿Con qué campeón has jugado tu última partida? ");
    scanf("%s", usuario[1].partida.campeon);
    printf("¿Cuántos asesinatos has hecho? ");
    scanf("%d", &usuario[1].partida.kda[0]);
    printf("¿Cuántas veces has muerto? ");
    scanf("%d", &usuario[1].partida.kda[1]);
    printf("¿Y cuántas asistencias has hecho? ");
    scanf("%d", &usuario[1].partida.kda[2]);
    ratio = (double) (usuario[1].partida.kda[0] + usuario[1].partida.kda[2]) / usuario[1].partida.kda[1];
    printf("%s, tu KDA ratio con %s ha sido %.2lf.\n", usuario[1].nombre, ratio, usuario[1].partida.campeon);  
    
    printf("\nJUGADOR 3\n");
    printf("¿Cuál es tu nombre de invocador? ");
    scanf("%s", usuario[2].nombre);
    printf("¿Con qué campeón has jugado tu última partida? ");
    scanf("%s", usuario[2].partida.campeon);
    printf("¿Cuántos asesinatos has hecho? ");
    scanf("%d", &usuario[2].partida.kda[0]);
    printf("¿Cuántas veces has muerto? ");
    scanf("%d", &usuario[2].partida.kda[1]);
    printf("¿Y cuántas asistencias has hecho? ");
    scanf("%d", &usuario[2].partida.kda[2]);
    ratio = (double) (usuario[2].partida.kda[0] + usuario[2].partida.kda[2]) / usuario[2].partida.kda[1];
    printf("%s, tu KDA ratio con %s ha sido %.2lf.\n", usuario[2].nombre, ratio, usuario[2].partida.campeon);  
    
    printf("\nJUGADOR 4\n");
    printf("¿Cuál es tu nombre de invocador? ");
    scanf("%s", usuario[3].nombre);
    printf("¿Con qué campeón has jugado tu última partida? ");
    scanf("%s", usuario[3].partida.campeon);
    printf("¿Cuántos asesinatos has hecho? ");
    scanf("%d", &usuario[3].partida.kda[0]);
    printf("¿Cuántas veces has muerto? ");
    scanf("%d", &usuario[3].partida.kda[1]);
    printf("¿Y cuántas asistencias has hecho? ");
    scanf("%d", &usuario[3].partida.kda[2]);    
    ratio = (double) (usuario[3].partida.kda[0] + usuario[3].partida.kda[2]) / usuario[3].partida.kda[1];
    printf("%s, tu KDA ratio con %s ha sido %.2lf.\n", usuario[3].nombre, ratio, usuario[3].partida.campeon);  

    printf("\nJUGADOR 5\n");
    printf("¿Cuál es tu nombre de invocador? ");
    scanf("%s", usuario[4].nombre);
    printf("¿Con qué campeón has jugado tu última partida? ");
    scanf("%s", usuario[4].partida.campeon);
    printf("¿Cuántos asesinatos has hecho? ");
    scanf("%d", &usuario[4].partida.kda[0]);
    printf("¿Cuántas veces has muerto? ");
    scanf("%d", &usuario[4].partida.kda[1]);
    printf("¿Y cuántas asistencias has hecho? ");
    scanf("%d", &usuario[4].partida.kda[2]);    
    ratio = (double) (usuario[4].partida.kda[0] + usuario[4].partida.kda[2]) / usuario[4].partida.kda[1];
    printf("%s, tu KDA ratio con %s ha sido %.2lf.\n", usuario[4].nombre, ratio, usuario[4].partida.campeon);  

    kda_total[0] = usuario[0].partida.kda[0] + usuario[1].partida.kda[0] + usuario[2].partida.kda[0] + usuario[3].partida.kda[0] + usuario[4].partida.kda[0];
    kda_total[1] = usuario[0].partida.kda[1] + usuario[1].partida.kda[1] + usuario[2].partida.kda[1] + usuario[3].partida.kda[1] + usuario[4].partida.kda[1];
    kda_total[2] = usuario[0].partida.kda[2] + usuario[1].partida.kda[2] + usuario[2].partida.kda[2] + usuario[3].partida.kda[2] + usuario[4].partida.kda[2];
    ratio = (double) (kda_total[0] + kda_total[2]) / kda_total[1];

    printf("\nUsuarios %s, %s, %s, %s y %s, el KDA de vuestra partida ha sido %d/%d/%d y su ratio %.2lf.\n", usuario[0].nombre, usuario[1].nombre, usuario[2].nombre, usuario[3].nombre, usuario[4].nombre, kda_total[0], kda_total[1], kda_total[2], ratio);  

    return 0;
}