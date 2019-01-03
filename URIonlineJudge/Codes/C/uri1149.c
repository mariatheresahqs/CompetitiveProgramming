#include <stdio.h>

int main() {
    int valorA, valorN,i, soma=0;
    scanf("%d %d", &valorA, &valorN);
    while (valorN <= 0) {
        scanf("%d", &valorN);
    }
    for (i = 0; i <= (valorN-1); i++) {
        soma += valorA;
        valorA++;
    }
    printf("%d\n", soma);
    return 0;
}