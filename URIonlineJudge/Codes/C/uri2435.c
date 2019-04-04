#include <stdio.h>

int main()
{
    int charrete1, charrete2;
    long double tempo1, tempo2,  distancia1, velocidade1, distancia2, velocidade2;

    scanf("%d %Lf %Lf", &charrete1, &distancia1, &velocidade1);
    scanf("%d %Lf %Lf", &charrete2, &distancia2, &velocidade2);

    tempo1 = distancia1/velocidade1;
    tempo2 = distancia2/velocidade2;

    if(tempo1<tempo2){
        printf("%d\n", charrete1);
    } else {
        printf("%d\n", charrete2);
    }

    return 0;
}
