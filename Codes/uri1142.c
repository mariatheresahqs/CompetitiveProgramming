#include <stdio.h>

int main(){
    
    int valor, contlinha=0, contnum=1;
    scanf("%d", &valor);
    
    while(contlinha<valor){
        if (contnum%4==0){
            printf("PUM\n");
            contlinha++;
        }
        else{
            printf("%d ",contnum);
        }
        contnum++;
    }
    
    return 0;
}
