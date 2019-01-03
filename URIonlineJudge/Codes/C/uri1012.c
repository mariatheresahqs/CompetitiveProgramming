#include <stdio.h>
#include <math.h>

int main(){

    double a, b, c, rect1, circle, trap, square, rect2;

    scanf("%lf %lf %lf", &a, &b, &c);

    rect1= (a*c)/2;
    circle= c*c*3.14159;
    trap= ((a+b)*c)*1/2;
    square= b*b;
    rect2= a*b;

    printf("TRIANGULO: %.3f\n", rect1);
    printf("CIRCULO: %.3f\n", circle);
    printf("TRAPEZIO: %.3f\n", trap);
    printf("QUADRADO: %.3f\n", square);
    printf("RETANGULO: %.3f\n", rect2);

    return 0;
}
