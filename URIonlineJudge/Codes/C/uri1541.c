#include <stdio.h>
#include <math.h>
int main()
{
    double medidaA,medidaB,percentualMax,areaConstrucao,areaTerreno, lado;
    while(1) {
        scanf("%lf", &medidaA);
        if(medidaA==0) {
            break;
        }
       else
        {
            scanf("%lf %lf", &medidaB,&percentualMax);
            areaConstrucao=medidaA*medidaB;
            areaTerreno=(areaConstrucao/percentualMax)*100;
            lado= pow(areaTerreno, .5);
            printf("%d\n",(int)lado);
        }
    }
    return 0;
}