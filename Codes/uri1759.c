#include <stdio.h>

int main() {
    int repeticao, i;
    scanf("%d", &repeticao);
    for(i=0; i<repeticao;i++){
        if(i==(repeticao-1)){
            printf("Ho!\n");
        }
        else {
            printf("Ho ");
        }
    }
    return 0;
}
