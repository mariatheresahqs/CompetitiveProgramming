#include <stdio.h>

int main() {
    int tamanho, i, j, valor1, valor1Final;
    while(scanf("%d", &tamanho)!=EOF) {
        int matriz[tamanho][tamanho];
        for (i = 0; i < tamanho; i++) {
            for (j = 0; j < tamanho; j++) {
                matriz[i][j] = 0;
            }
        }
        for (i = 0; i < tamanho; i++) {
            for (j = 0; j < tamanho; j++) {
                if (i == 0 || j == 0 || i == (tamanho - 1) || j == (tamanho - 1)) {
                    matriz[i][j] = 0;
                }
                if (i == j) {
                    matriz[i][j] = 2;
                }
                if ((i + j) == (tamanho - 1)) {
                    matriz[i][j] = 3;
                }
            }
        }
        valor1 = tamanho / 3;
        valor1Final = tamanho - valor1;
        for (i = valor1; i < (valor1Final); i++) {
            for (j = valor1; j < (valor1Final); j++) {
                matriz[i][j] = 1;
            }
        }
        if (matriz[tamanho / 2][tamanho / 2]) {
            matriz[tamanho / 2][tamanho / 2] = 4;
        }
        for (i = 0; i < tamanho; i++) {
            for (j = 0; j < tamanho; j++) {
                printf("%d", matriz[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}
