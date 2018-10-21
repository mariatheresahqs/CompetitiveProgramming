#include <stdio.h>

int main() {
    int tamanho,i, j;
    //printf("Declare o tamanho da matriz:\n);
    scanf("%d", &tamanho);
    int matriz[i][j];
    for(i=0; i<tamanho;i++){
        for (j = 0; j < tamanho; j++) {
            if(i==j){
                matriz[i][j]=1;
            }
            if((i+j)==tamanho-1){
                matriz[i][j]=2;
            } else{
                matriz[i][j]=3;
            }
        }
    }
    for(i=0;i<tamanho;i++){
        for (int j = 0; j < tamanho;j++) {
            if(j<tamanho-1) {
                printf("%d ", matriz[i][j]);
            } else if(j==tamanho-1){
                printf("%d\n", matriz[i][j]);
            }
        }
    }
    return 0;
}