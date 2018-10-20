#include <stdio.h>

int main() {
    int entradas, valor, i,j, c, soma=0;
    scanf("%d", &entradas);
    for(j=0;j<entradas;j++) {
        scanf("%d", &valor);
        c = valor / 2;
        soma = 0;
        for (i = 1; i <= c; i++) {
            if (valor % i == 0) {
                soma += i;
            }
        }
        if (soma == valor) {
            printf("%d eh perfeito\n", valor);
        }
        else {
            printf("%d nao eh perfeito\n", valor);
        }
    }
    return 0;
}