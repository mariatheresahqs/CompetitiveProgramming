#include <stdio.h>

int main() {
    int tamanho, linha,  i, j;
    tamanho=12;
    float matriz[tamanho][tamanho], media, soma=0;
    char operacao;
    //Recebe a linha
    scanf("%d", &linha);
    //Recebe a operacao
    scanf(" %c", &operacao);
    for(i=0; i<tamanho; i++){
        for(j=0; j<tamanho;j++){
            matriz[i][j]=0;
        }
    }
    for(i=0; i<tamanho; i++){
        for(j=0; j<tamanho;j++){
            scanf("%f", &matriz[i][j]);
        }
    }
    for(i=0; i<tamanho; i++){
        for(j=0; j<tamanho;j++){
            if(i==linha){
                soma += matriz[i][j];
            }
        }
    }
    media = soma/tamanho;
    if(operacao=='S') {
        printf("%.1f\n", soma);
    }
    else if (operacao=='M') {
        printf("%.1f\n", media);
    }
    return 0;
}
