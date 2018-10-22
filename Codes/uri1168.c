#include <stdio.h>
#include <string.h>

int main() {
    int casos, i=0,j, contadorLeds=0;
    char numero[100], tamanhoNumero;
    scanf("%d", &casos);
    while(i<casos){
        scanf("%s", &numero);
        tamanhoNumero = strlen(numero);
        for (j=0;j<tamanhoNumero;j++) {
            if (numero[j] == '1') {
                contadorLeds += 2;
            } if (numero[j] == '2'){
                contadorLeds += 5;
            }else if(numero[j] == '3'){
                contadorLeds += 5;
            } else if (numero[j] == '4') {
                contadorLeds += 4;
            }  else if(numero[j] == '5'){
                contadorLeds += 5;
            } else if (numero[j] == '6') {
                contadorLeds += 6;
            } else if (numero[j] == '7') {
                contadorLeds += 3;
            } else if (numero[j] == '8') {
                contadorLeds += 7;
            } else if (numero[j] == '9') {
            contadorLeds += 6;
            } else if (numero[j] == '0') {
                contadorLeds += 6;
            }
        }
        printf("%d leds\n", contadorLeds);
        i++;
        contadorLeds=0;
    }
    return 0;
}
