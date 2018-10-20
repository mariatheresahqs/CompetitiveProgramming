#include <stdio.h>

int main() {
    float s, i, soma=0;
    for(i=1; i<=100;i++){
        s = (float)1/i;
        soma += s;
        //printf("%.2f ", s);
    }
    printf("%.2f\n", soma);
    return 0;
}