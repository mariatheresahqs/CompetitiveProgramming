#include <stdio.h>

int main() {
    int valor[4],i,j, temporario, flag=0;
    for(i=0;i<4;i++) {
        scanf("%d", &valor[i]);
    }
    for(i=0;i<4;i++){
        for(j=1;j<3-i;j++) {
            if (valor[j] > valor[j+1]) {
                temporario = valor[j];
                valor[j] = valor[j+1];
                valor[j+1] = temporario;
            }
        }
    }
    for(i=0;i<=1;i++){
        if (valor[i+2] - valor[i+1] < valor[i] && valor[i+1] + valor[i+2] > valor[i]) {
            flag=1;
        }
    }


    if (flag==1) {
        printf("S\n");
    } else {
        printf("N\n");
    }

    return 0;
}