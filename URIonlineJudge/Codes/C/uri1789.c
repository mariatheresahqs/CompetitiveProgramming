#include <stdio.h>

int main() {
    int casos, i;
    while(scanf("%d", &casos)!=EOF) {
        int lesmas[casos], maiorVelocidade=0, nivel;
        for(i=0; i<casos;i++){
            scanf("%d", &lesmas[i]);
            if(lesmas[i]>maiorVelocidade){
                maiorVelocidade = lesmas[i];
            }
        }
        if(maiorVelocidade<10){
            nivel = 1;
        } else if(maiorVelocidade>=10 && maiorVelocidade<20){
            nivel =2;
        } else{
            nivel =3;
        }
        printf("%d\n", nivel);
    }
    return 0;
}
