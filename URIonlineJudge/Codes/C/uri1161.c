#include <stdio.h>

long long int fatorial(long long int valor){
    long long int valorFatorial;
    if(valor<=1){
        return 1;
    } else{
        valorFatorial = valor * fatorial(valor - 1);
        return (valorFatorial);
    }

}

int main() {
    long long int valor1, valor2, soma;

    while(scanf("%lld %lld", &valor1, &valor2)!=EOF){
        valor1 = fatorial(valor1);
        valor2 = fatorial(valor2);
        soma = valor1 + valor2;
        printf("%lld\n", soma);
    }

    return 0;
}