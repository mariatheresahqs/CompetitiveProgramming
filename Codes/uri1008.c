#include <stdio.h>
#include <math.h>

int main(){
    int empn, hw;
    float aph, sal;

    scanf("%d%d%f", &empn, &hw, &aph);

    sal=hw*aph;

    printf("NUMBER = %d\n", empn);
    printf("SALARY = U$ %0.2f\n", sal);

    return 0;
}
