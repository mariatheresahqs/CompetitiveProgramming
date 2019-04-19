#include <stdio.h>

int main() {
    int entrada, valor1, valor2, valor3,mmc=1;
    int i=2, flag=0, diferenca;
    do {
        scanf("%d", &entrada);
        scanf("%d %d %d", &valor1, &valor2, &valor3);
        while (flag == 0) {
            if (valor1 % i == 0 || valor2 % i == 0 || valor3 % i == 0) {
                mmc *= i;
                if (valor1 % i == 0) {
                    valor1 = valor1 / i;
                }
                if (valor2 % i == 0) {
                    valor2 = valor2 / i;
                }
                if (valor3 % i == 0) {
                    valor3 = valor3 / i;
                }
            } else {
                i++;
            }
            if (valor1 == 1 && valor2 == 1 && valor3 == 1) {
                flag = 1;
            }
            diferenca = mmc - entrada;

        }
        printf("%d\n", diferenca);
        mmc = 1;
        i = 2;
        flag = 0;
    } while(entrada!=EOF);

    return 0;
}