#include <stdio.h>

int main() {
    int Ncasos, produto, quantidade, i;
    float total=0, valorProduto=0;
    scanf("%d", &Ncasos);
    for(i=0;i<Ncasos;i++) {
        scanf("%d %d", &produto, &quantidade);
        switch (produto) {
            case 1001 :
                valorProduto += 1.50;
                break;

            case 1002 :
                valorProduto += 2.50;
                break;

            case 1003 :
                valorProduto += 3.50;
                break;

            case 1004 :
                valorProduto += 4.50;
                break;

            case 1005 :
                valorProduto += 5.50;
                break;

            default:
                valorProduto += 0;
        }
        valorProduto*=quantidade;
        total +=valorProduto;
        valorProduto=0;
    }
    printf("%.2f\n", total);

    return 0;
}