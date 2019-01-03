#include <stdio.h>

int main() {
    int x, i, par=0, soma=0, k=0, p=1;
    do{
        scanf("%d",&x);
        if( x==0){
            break;
        }
        else {
            for (i = 0; i < 5; i++) {
                if (x % 2 == 0) {
                    par = x + k;
                    soma += par;
                    k += 2;
                } else {
                    par = x + p;
                    soma += par;
                    p += 2;
                }
            }
        }
        printf("%d\n", soma);
        par = 0;
        soma = 0;
        k=0;
        p=1;
    }while (x!=0);
    return 0;
}