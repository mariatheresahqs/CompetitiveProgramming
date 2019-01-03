#include<stdio.h>
int main()
{
    int tamanho, i,j,x;
    while(1){
        scanf("%d",&tamanho);
        if(tamanho==0){
            break;
        }
        for(i=1;i<=tamanho;i++){
            for(j=1;j<=tamanho;j++){
                x = i;
                if(j < x){
                    x = j;
                }
                if(tamanho-i+1 < x){
                    x = tamanho-i+1;
                }
                if(tamanho-j+1 < x){
                    x = tamanho-j+1;
                }
                printf("%3d",x);
                if(j < tamanho){
                    printf(" ");
                }
                else printf("\n");
            }
        }
        printf("\n");
    }
    return 0;
}