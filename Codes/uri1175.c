#include <stdio.h>

int main() {
    int vetor[20], valor, temporario, i;
    for(i=0;i<20;i++){
        scanf("%d", &valor);
        vetor[i] = valor;
    }
    for(i=0;i<10;i++){
        temporario = vetor[i];
        vetor[i] = vetor [20-1  - i];
        vetor[20-1 -i]= temporario;
    }
    for(i=0; i<20; i++){
        printf("N[%d] = %d\n", i, vetor[i]);
    }
    return 0;
}