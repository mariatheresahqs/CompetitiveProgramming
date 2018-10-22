#include <stdio.h>

int main() {
    int casos,raio1, raio2, menorRaio=0,i;
    scanf("%d", &casos);
    for(i=0;i<casos;i++){
        scanf("%d %d",&raio1, &raio2);
        menorRaio = raio1 + raio2;
        printf("%d\n", menorRaio);
        menorRaio = 0;
    }
    return 0;
}
