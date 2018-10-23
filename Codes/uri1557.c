#include <stdio.h>
#include <math.h>

int main() {
    int tamanho, i, j;
    while (1) {
        scanf("%d", &tamanho);
        if(tamanho==0){
            break;
        }
        long long int matriz[tamanho][tamanho];
        int espacamento, contador = 0;
        for (i = 0; i < tamanho; ++i) {
            for (j = 0; j < tamanho; ++j) {
                matriz[i][j] = (int)pow(2, (i + j));
            }
        }
        espacamento = (int)matriz[tamanho - 1][tamanho - 1];
        while (espacamento>0) {
            espacamento /= 10;
            contador++;
        }
        //printf("%d\n", contador);
        for (i = 0; i < tamanho; ++i) {
            for (j = 0; j < tamanho; ++j) {
                if(j==(tamanho-1)) {
                    printf("%*lld", contador, matriz[i][j]);
                } else{
                    printf("%*lld ",contador, matriz[i][j]);
                }
            }
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}
