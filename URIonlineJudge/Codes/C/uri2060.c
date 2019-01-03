#include <stdio.h>

int main() {
    int quantidade, i, valor, multiplo2=0, multiplo3=0, multiplo4=0, multiplo5=0;
    scanf("%d", &quantidade);
    for(i=0; i<quantidade;i++){
        scanf("%d", &valor);
        if(valor%2==0){
            multiplo2++;
        }
        if(valor%3==0){
            multiplo3++;
        }
        if(valor%4==0){
            multiplo4++;
        }
        if(valor%5==0){
            multiplo5++;
        }
    }
    printf("%d Multiplo(s) de 2\n", multiplo2);
    printf("%d Multiplo(s) de 3\n", multiplo3);
    printf("%d Multiplo(s) de 4\n", multiplo4);
    printf("%d Multiplo(s) de 5\n", multiplo5);
    return 0;
}