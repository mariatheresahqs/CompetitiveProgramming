#include <stdio.h>

int main() {
    int nLink, resultado, i;
    scanf("%d", &nLink);
    resultado = nLink;
    for(i=0; i<2;i++){
        resultado *=2;
    }
    printf("%d\n", resultado);
    return 0;
}