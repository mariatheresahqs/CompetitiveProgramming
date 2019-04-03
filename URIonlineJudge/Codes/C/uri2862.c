#include <stdio.h>

int main() {
    int nCasos, energia;
    scanf("%d", &nCasos);
    for (int i=0; i<nCasos;i++){
        scanf("%d", &energia);
        if(energia>8000){
            printf("Mais de 8000!\n");
        } else{
            printf("Inseto!\n");
        }
    }
    return 0;
}