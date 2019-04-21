#include <stdio.h>

int main() {
    double volume, diametro, altura, area, raiz;
    while(scanf("%lf %lf", &volume, &diametro)!=EOF) {
        raiz = diametro/2;
        area = raiz*raiz*3.14;
        altura = volume/area;
        printf("ALTURA = %.2lf\n", altura);
        printf("AREA = %.2lf\n", area);
    }
    return 0;
}