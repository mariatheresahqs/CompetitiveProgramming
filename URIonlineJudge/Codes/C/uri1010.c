#include <stdio.h>

int main(){

    int codigo1, codigo2;
    int qnt1, qnt2;
    float valor1, valor2, valor3;

    scanf("%d %d %f", &codigo1, &qnt1, &valor1);
    scanf("%d %d %f", &codigo2, &qnt2, &valor2);

    valor3= (float)(qnt1*valor1)+(qnt2*valor2);

    printf("VALOR A PAGAR: R$ %.2f\n", valor3);

}
