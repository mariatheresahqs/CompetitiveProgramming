#include <stdio.h>

void main()
{
    int entradas, linhas, colunas, i, sonares;
    scanf("%d", &entradas);
    for(i=0;i<entradas;i++){
        scanf("%d %d", &linhas, &colunas);
        linhas -= 2;
        colunas -= 2;
        while(linhas%3!=0){
            linhas+=1;
        }
        while(colunas%3!=0){
            colunas+=1;
        }
        sonares = (linhas/3) * (colunas/3);
        printf("%d\n", sonares);
    }
}