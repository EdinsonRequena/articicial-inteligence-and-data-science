#include <stdio.h>

#define LON 128
#define KDA_CONST 3

typedef struct
{
	char user_name[LON];
	int user_level;
	int exp;
} your_user;

typedef struct
{
    your_user eddy;
    char champ_name[LON];
    int kda [KDA_CONST];
} game;


int main() {
    game user;

	printf("What's your name: ?");
	scanf("%s", &user.eddy.user_name);

    printf("What's the champion name: ?");
	scanf("%s", &user.champ_name);

	printf("What's your level: ?");
	scanf("%d", &user.eddy.user_level);

	printf("What's your exp: ?");
	scanf("%d", &user.eddy.exp);

	printf("How much kills do you hve: ?");
	scanf("%d", &user.kda[0]);

	printf("How mouch deaths do you hace: ?");
	scanf("%d", &user.kda[1]);

	printf("How much assists do you have: ?");
	scanf("%d", &user.kda[2]);

    float ratio = (float)(user.kda[0] + user.kda[1]) / user.kda[2];

    printf("name%s\n", user.eddy.user_name);
    printf("champion%s\n", user.champ_name);
    printf("level%d\n", user.eddy.user_level);
    printf("exp%d\n", user.eddy.exp);
    printf("kills%d\n", user.kda[0]);
    printf("deaths%d\n", user.kda[1]);
    printf("assists%d\n", user.kda[2]);
    printf("kda%f\n", ratio);

    return 0;
}