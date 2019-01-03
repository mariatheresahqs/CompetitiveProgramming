#include <stdio.h>

int main(){
    int x, count=0;
    double num, soma, media;
    while (1){
        if (count==2)
            break;
        scanf("%lf", &num);
        if (num>=0 && num<=10){
                soma+=num;
                count++;
            }
        else
            printf("nota invalida\n");
    }
    media=soma/2;
    printf("media = %.2lf\n", media);
    return 0;
}
