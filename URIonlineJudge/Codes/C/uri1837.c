#include <stdio.h>

int main() {
    int divisor, dividendo, resto, quociente;
    scanf("%d %d", &dividendo, &divisor);

        resto = dividendo % divisor;
        quociente = dividendo / divisor;
        if(resto<0) {
            if (quociente < 0) {
                quociente--;
            }
            if (quociente > 0) {
                quociente++;
            }
            resto = dividendo - (divisor*quociente);
        }

    printf("%d %d\n", quociente, resto);
    return 0;
}