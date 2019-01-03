#include <stdio.h>

int main() {
    int entradas, numero, i, j, primo=0;
    scanf("%d", &entradas);
    for(i=0; i<entradas; i++){
        scanf("%d", &numero);
        for(j=1; j<=numero; j++){
            if(numero%j==0){
                primo +=1;
            }
        }
        if(primo>2){
            printf("%d nao eh primo\n", numero);
        }
        else{
            printf("%d eh primo\n", numero);
        }
        primo=0;
    }
    return 0;
}