#include <stdio.h>

int main() {

    int entrada;
    while(scanf("%d", &entrada)!=EOF){
        entrada--;
        printf("%d\n", entrada);
    }
    return 0;
}