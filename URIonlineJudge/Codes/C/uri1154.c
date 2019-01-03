#include <stdio.h>

int main() {
    int idade, idades, quantidade=0;
    float media=0;
    idades = 0;
    idade=0;
    while(idade>=0) {
        idades += idade;
        quantidade++;
        scanf("%d", &idade);
    }
    media = (float)idades/(quantidade-1);
    printf("%.2f\n", media);
    return 0;
}
