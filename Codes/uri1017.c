#include <stdio.h>
#include <math.h>

int main(){

    int h, v, d;
    double f;

    scanf("%d %d", &h, &v);

    d = h*v;
    f = d/12.0;

    printf("%.3f\n", f);

    return 0;
}
