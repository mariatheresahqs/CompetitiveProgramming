#include <stdio.h>

int main() {
    int reclamacoes,i;
    while(scanf("%d", &reclamacoes)!=EOF){
        if(reclamacoes>0){
            printf("vai ter duas!\n");
        } else{
            printf("vai ter copa!\n");
        }
    }
    return 0;
}
