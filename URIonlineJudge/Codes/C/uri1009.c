#include <stdio.h>
#include <math.h>

int main(){

    char name;
    double salary, totalmoney, total;

    scanf("%s %lf %lf",&name, &salary, &totalmoney);

    total=salary+totalmoney*0.15;

    printf("TOTAL = R$ %.2f\n", total);

    return 0;

}
