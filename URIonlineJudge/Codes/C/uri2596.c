#include <stdio.h>

int main() {
    int casos, qntEsferas,i,j,k, contadorDivisores=0, contadorEsferas=0;
    scanf("%d", &casos);
    for(i=0;i<casos;i++){
        scanf("%d", &qntEsferas);
        for(j=1; j<=qntEsferas;j++){
            for(k=1;k<=j;k++){
                if(j%k==0){
                    contadorDivisores+=1;
                }
            }
            if(contadorDivisores%2==0){
                contadorEsferas+=1;
            }
            contadorDivisores=0;
        }
        printf("%d\n", contadorEsferas);
        contadorEsferas = 0;
    }

    return 0;
}