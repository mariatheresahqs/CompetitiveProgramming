#include <stdio.h>

int main(){
    
    float x, preco;
    int y;
    
    scanf("%f %d", &x, &y);
    
    if (x==1)
        x=4;
    else if (x==2)
        x=4.5;
    else if (x==3)
        x=5;
    else if (x==4)
        x=2;
    else if (x==5)
        x=1.5;
    
    preco = x*y;
    
    printf("Total: R$ %.2f\n", preco);
    
}
