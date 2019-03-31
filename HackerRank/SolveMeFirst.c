#include <stdio.h>

int solveMeFirst(int a, int b) {
    return a+b;//retorno da soma dos valores dos parametros passados para a funcao
 
}

int main() {
    int num1,num2;
    scanf("%d %d",&num1,&num2);
    int sum; 
    sum = solveMeFirst(num1,num2);//passagem de parametros para funcao
    printf("%d",sum);
    return 0;
}
