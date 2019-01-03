#include <stdio.h>

int main() {
    int vetor[1000], valor, count=0, i, j;
    scanf("%d", &valor);
    for (i=0; i<(1000);i++){
        if(count==valor){
            count=0;
            vetor[i] = count;
            count++;
        }
        else{
            vetor[i] = count;
            count++;
        }
    }
    for(i=0;i<1000;i++){
        printf("N[%d] = %d\n", i, vetor[i]);
    }
    return 0;
}