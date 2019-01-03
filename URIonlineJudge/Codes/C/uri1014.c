#include <stdio.h>
#include <math.h>

int main(){

    int x;
    double y, avg;

    scanf("%d %lf", &x, &y );

    avg = x/y;

    printf("%.3f km/l\n", avg);

    return 0;
}
