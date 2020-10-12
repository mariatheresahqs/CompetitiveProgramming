#include <stdio.h>
int main(){
    float  salario,valor,novo;
    scanf("%f",&salario);
    if(salario>=0 && salario<=400){
        valor=(salario*15)/100.0;
        novo=valor+salario;
        printf("Novo salario: %.2f\n",novo);
        printf("Reajuste ganho: %.2f\n",valor);
        printf("Em percentual: 15 %\n");
    }
    if(salario>=400.01 && salario<=800.00){
        valor=(salario*12)/100.0;
        novo=valor+salario;
         printf("Novo salario: %.2f\n",novo);
        printf("Reajuste ganho: %.2f\n",valor);
        printf("Em percentual: 12 %\n");
    }
    if(salario>=800.01 && salario<=1200.00){
        valor=(salario*10)/100.0;
        novo=valor+salario;
         printf("Novo salario: %.2f\n",novo);
        printf("Reajuste ganho: %.2f\n",valor);
        printf("Em percentual: 10 %\n");
    }
    if(salario>=1200.01 && salario<=2000.00){
        valor=(salario*7)/100.0;
        novo=valor+salario;
         printf("Novo salario: %.2f\n",novo);
        printf("Reajuste ganho: %.2f\n",valor);
        printf("Em percentual: 7 %\n");
    }
    if(salario>2000.00){
        valor=(salario*4)/100.0;
        novo=valor+salario;
         printf("Novo salario: %.2f\n",novo);
        printf("Reajuste ganho: %.2f\n",valor);
        printf("Em percentual: 4 %\n");
    }
    
    return 0;
}
