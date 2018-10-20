#include <stdio.h>

int main() {
    double i, s=0, b=1;
    for (i=1; i<=39;i+=2){
        s += i/b;
        b*= 2;
        printf("%.2lf\n", s);
    }
    printf("%.2lf\n", s);
    return 0;
}