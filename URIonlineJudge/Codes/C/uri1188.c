#include <stdio.h>

int main() {
    int tamanho, i, j;
    tamanho = 12;
    double matriz[tamanho][tamanho], media, soma=0, count=0;
    char letra;
    //printf("Declare o tipo de operação que deseja realizar com a matriz, sendo S para soma e M para média:\n");
    scanf("%c", &letra);
    //printf("Declare %d valores para a matriz:\n", tamanho*tamanho);
    for(i=0; i<tamanho;i++){
        for(j=0; j<tamanho;j++){
            scanf("%lf", &matriz[i][j]);
            if((i>j) && ((i+j)>tamanho-1)) {
                soma += matriz[i][j];
                count++;
            }
        }
    }
    if(letra=='S'){
        printf("%.1lf\n", soma);
    }
    else if(letra=='M'){
        media = soma/count;
        printf("%.1lf\n", media);
    }
    return 0;
}