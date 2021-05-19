/*

Vamos a modificar el programa anterior para trabajar con tablas de estructuras, de forma que 
calculemos el KDA total de los cinco jugadores que han participado en la partida.
Para obtener dicho dato es necesario sumar por un lado los asesinatos de los cinco jugadores,
por otro las muertes y finalmente las asistencias. Asimismo, 
calcularemos el ratio de ese KDA  total.  

------------------------------resuelto por pasos--------------------------------

1)Definir dos constantes a la cual le pasaremos por valor la longitud de los vectores que crearemos mas adelante (opcional)

2)Crear una estructura con las variables necesarias para almacenar los datos requeridos.
	a) los datos requeridos son:
		*)Nombre
		*)Nombre del campeon
		*)Asesinatos
		*)Muertes
		*)Asistencias

	b) ejemplo de codigo:
		typedef struct {
			char name[10];
			char champion[10];
			int kills;
			int deaths;
			int assists;
		} players;

3)Crear una tabla estructurada para poder almacenar los datos de los jugadores.
	*)ejemplo en codigo:
		players game[5];
4)Solicitar los datos que almacenaremos en las variables de la estructura creada previamente, sacar el ratio de de KDA y mostrar el ratio por pantalla.
	
	a) solicitar datos:
		*)Ejemplo en codigo:

    			printf("Name: ");
    			scanf("%s", &game[0].name);

    			printf("Champion: ");
    			scanf("%s", &game[0].champion);

			printf("kills: ");
    			scanf("%d", &game[0].kills);

    			printf("deaths: ");
    			scanf("%d", &game[0].deaths);

    			printf("assists: ");
    			scanf("%d", &game[0].assists);
			// y asi hasta completar todos los jugadores

	b)Sacar ratio y motrarlo por pantalla
		*)Ejemplo en codigo:

    			float player1_ratio = (float)(game[0].kills + game[0].assists)/game[0].deaths;
			printf("Ratio player1 %f\n", player1_ratio);o);
			// repetir con el resto de jugadores

5)Sumar el KDA de todos los jugadores, sacar el ratio de ese KDA y mostrarlo por pantalla.
	a)Sumar KDA y sacar el ratio
		*)ejemplo de codigo:
			int total_kills = game[0].kills + game[1].kills + game[2].kills + game[3].kills + game[4].kills
			int total_deaths = game[0].deaths + game[1].deaths + game[2].deaths + game[3].deaths + game[4].deaths
			int total_assists = game[0].assists + game[1].assists + game[2].assists + game[3].assists + game[4].assists
			total_ratio = (float)(total_kills + total_deaths) / total_assists

	b) mostrar por pantalla el nombre de los jugadores, el kda total y ratio de ese kda total
		*)ejemplo en codigo:

			printf("Players %s%s%s%s%s have kda: %d/%d/%d and ratio: %f", game[0].name, game[1].name, game[2].name, game[3].name, game[4].name, total_kills, 				total_deaths, total_assists, total_ratio)
			
*/

#include <stdio.h>

#define LON 128
#define TABLE 5

typedef struct {
	char name[LON];
	char champion[LON];
	int kills;
	int deaths;
	int assists;
} players;

int main() {
	players game[TABLE];

    printf("Name: ");
    scanf("%s", &game[0].name);
    printf("Champion: ");
    scanf("%s", &game[0].champion);
	printf("kills: ");
    scanf("%d", &game[0].kills);
    printf("deaths: ");
    scanf("%d", &game[0].deaths);
    printf("assists: ");
    scanf("%d", &game[0].assists);
    float player1_ratio = (float)(game[0].kills + game[0].assists)/game[0].deaths;
	printf("Ratio player1 %f\n", player1_ratio);

    printf("Name: ");
    scanf("%s", &game[1].name);
    printf("Champion: ");
    scanf("%s", &game[1].champion);
	printf("kills: ");
    scanf("%d", &game[1].kills);
    printf("deaths: ");
    scanf("%d", &game[1].deaths);
    printf("assists: ");
    scanf("%d", &game[1].assists);
    float player2_ratio = (float)(game[1].kills + game[1].assists)/game[1].deaths;
	printf("Ratio player2%f\n", player2_ratio);

    printf("Name: ");
    scanf("%s", &game[2].name);
    printf("Champion: ");
    scanf("%s", &game[2].champion);
	printf("kills: ");
    scanf("%d", &game[2].kills);
    printf("deaths: ");
    scanf("%d", &game[2].deaths);
    printf("assists: ");
    scanf("%d", &game[2].assists);
    float player3_ratio = (float)(game[2].kills + game[2].assists)/game[2].deaths;
	printf("Ratio player3%f\n", player1_ratio);

    printf("Name: ");
    scanf("%s", &game[3].name);
    printf("Champion: ");
    scanf("%s", &game[3].champion);
	printf("kills: ");
    scanf("%d", &game[3].kills);
    printf("deaths: ");
    scanf("%d", &game[3].deaths);
    printf("assists: ");
    scanf("%d", &game[3].assists);
    float player4_ratio = (float)(game[3].kills + game[3].assists)/game[3].deaths;
	printf("Ratio player4%f\n", player1_ratio);

    printf("Name: ");
    scanf("%s", &game[4].name);
    printf("Champion: ");
    scanf("%s", &game[4].champion);
	printf("kills: ");
    scanf("%d", &game[4].kills);
    printf("deaths: ");
    scanf("%d", &game[4].deaths);
    printf("assists: ");
    scanf("%d", &game[4].assists);
    float player5_ratio = (float)(game[4].kills + game[4].assists)/game[4].deaths;
	printf("Ratio player5%f\n", player1_ratio);

    int total_kills = game[0].kills + game[1].kills + game[2].kills + game[3].kills + game[4].kills;
	int total_deaths = game[0].deaths + game[1].deaths + game[2].deaths + game[3].deaths + game[4].deaths;
	int total_assists = game[0].assists + game[1].assists + game[2].assists + game[3].assists + game[4].assists;
	float total_ratio = (float)(total_kills + total_deaths) / total_assists;

    printf("Players %s%s%s%s%s have kda: %d/%d/%d and ratio: %f", game[0].name, game[1].name, game[2].name, game[3].name, game[4].name, total_kills,total_deaths, total_assists, total_ratio);

    return 0;
}
