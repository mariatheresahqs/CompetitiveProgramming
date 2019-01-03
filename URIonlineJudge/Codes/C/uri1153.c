#include <stdio.h>

int main() {
    int n, fatorial=1, i;
    scanf("%d", &n);
    for (i=0; i<=(n-1); i++){
         fatorial *= (n-i);
    }
    printf("%d\n", fatorial);
    return 0;
}