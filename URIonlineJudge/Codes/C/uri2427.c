#include <stdio.h>
#include <math.h>

int main()
{
    int tamanho, pedacos;
    scanf("%d", &tamanho);
    tamanho/=2;
    pedacos = 4;
    while(tamanho>=2){
        pedacos *=4;
        tamanho= tamanho/2;
        
    }
    
    printf("%d\n", pedacos);

    return 0;
}
