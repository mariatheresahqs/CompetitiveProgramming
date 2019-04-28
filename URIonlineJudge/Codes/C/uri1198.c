#include <stdio.h>

int main() {
    long long int valor1, valor2, diferenca;
    while(scanf("%lld %lld", &valor1, &valor2)!=EOF){
        if(valor1>valor2){
            diferenca = valor1 - valor2;
        } else{
            diferenca = valor2 - valor1;
        }
        printf("%lld\n", diferenca);
    }

    return 0;
}