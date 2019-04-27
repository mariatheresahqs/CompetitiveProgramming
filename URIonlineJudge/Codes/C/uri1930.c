#include <stdio.h>

int main() {
    int nCasos=4, entrada1, entrada2, entrada3, entrada4,total=0, i;
    scanf("%d %d %d %d", &entrada1, &entrada2, &entrada3, &entrada4);
    total = entrada1 + entrada2 + entrada3 + entrada4;
    total-=3;
    printf("%d\n", total);
    return 0;
}