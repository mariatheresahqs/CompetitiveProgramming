#include <stdio.h>
#include <string.h>

int main() {
    int numeroCasos;
    char sheldon[10], raj[10];
    scanf("%d", &numeroCasos);
    for(int i=1; i<=numeroCasos;i++){
        scanf("%s%s", sheldon, raj);
        if(!strcmp(sheldon, raj)){
            printf("Caso #%d: De novo!\n", i);
        } else if(!strcmp(sheldon, "tesoura")){
            if (!strcmp(raj, "papel") || !strcmp(raj, "lagarto")) {
                printf("Caso #%d: Bazinga!\n", i);
            } else if(!strcmp(raj, "Spock") || !strcmp(raj, "pedra")){
                printf("Caso #%d: Raj trapaceou!\n", i);
            }
        } else if(!strcmp(sheldon, "papel")){
            if (!strcmp(raj, "pedra") || !strcmp(raj, "Spock")) {
                printf("Caso #%d: Bazinga!\n", i);
            } else if(!strcmp(raj, "tesoura") || !strcmp(raj, "lagarto")){
                printf("Caso #%d: Raj trapaceou!\n", i);
            }
        } else if(!strcmp(sheldon, "pedra")){
            if (!strcmp(raj, "lagarto") || !strcmp(raj, "tesoura")) {
                printf("Caso #%d: Bazinga!\n", i);
            } else if(!strcmp(raj, "Spock") || !strcmp(raj, "papel")){
                printf("Caso #%d: Raj trapaceou!\n", i);
            }
        } else if(!strcmp(sheldon, "lagarto")){
            if (!strcmp(raj, "Spock") || !strcmp(raj, "papel")) {
                printf("Caso #%d: Bazinga!\n", i);
            } else if(!strcmp(raj, "pedra") || !strcmp(raj, "tesoura")){
                printf("Caso #%d: Raj trapaceou!\n", i);
            }
        } else if(!strcmp(sheldon, "Spock")){
            if (!strcmp(raj, "tesoura") || !strcmp(raj, "pedra")) {
                printf("Caso #%d: Bazinga!\n", i);
            } else if(!strcmp(raj, "lagarto") || !strcmp(raj, "papel")){
                printf("Caso #%d: Raj trapaceou!\n", i);
            }
        }
    }

    return 0;
}