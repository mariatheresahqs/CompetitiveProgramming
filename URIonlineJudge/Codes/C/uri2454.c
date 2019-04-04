#include <stdio.h>

int main()
{
    int porta1, porta2;
    scanf("%d %d", &porta1, &porta2);
    if(porta1==0){
        printf("C\n");
    }
    if(porta1==1 && porta2==0){
        printf("B\n");
    }
    if(porta1==1 && porta2==1){
        printf("A\n");
    }

    return 0;
}
