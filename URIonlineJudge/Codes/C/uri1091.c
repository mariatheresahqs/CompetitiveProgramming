#include <stdio.h>

int main(){

    int casos, divisorX, divisorY, x, y, i;

    while(1){
             scanf("%d", &casos);
             if(casos == 0) break;

             scanf("%d %d", &divisorX, &divisorY);

             for(i = 0; i < casos; i++){
                   scanf("%d %d", &x, &y);
                   if(x == divisorX || y == divisorY) printf("divisa\n");
                   else if(x > divisorX && y > divisorY) printf("NE\n");
                   else if(x > divisorX && y < divisorY) printf("SE\n");
                   else if(x < divisorX && y > divisorY) printf("NO\n");
                   else if(x < divisorX && y < divisorY) printf("SO\n");
             }
    }
    return 0;
}