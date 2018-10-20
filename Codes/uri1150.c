#include <stdio.h>

int main() {
    int x,z, soma, somador=0, contador=0;
    //pede o valor x
    scanf("%d", &x);
    //pede o valor z
    scanf("%d", &z);
    while (z<=x){
        scanf("%d",&z);
    }
    soma = x;
    contador ++;
    somador = x;
    while(somador<z){
        soma = soma + 1;
        somador += soma;
        //printf("soma: %d\n", soma);
        //printf("somador: %d\n", somador);
        contador++;
    }
    printf("%d", contador);
    return 0;
}