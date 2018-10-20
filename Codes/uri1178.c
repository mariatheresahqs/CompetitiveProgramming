#include <stdio.h>

int main() {
    double valor, vetor[100];
    int i;
    scanf("%lf", &valor);
    for(i=0;i<100;i++){
        vetor[i] = valor;
        valor = valor/2;
    }
    for(i=0;i<100;i++){
        printf("N[%d] = %.4lf\n", i, vetor[i]);
    }
    return 0;
}