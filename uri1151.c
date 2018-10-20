#include <stdio.h>

int main() {
    int n,i, fibonacci, primeiro = 0, segundo=1, contador=1;
    scanf("%d", &n);
    for (i=0; i<n; i++){

        if(i<=1){
            printf("%d ", i);
        }
        else {
            fibonacci = primeiro + segundo;
            primeiro = segundo;
            segundo = fibonacci;
            if(contador<n) {
                printf("%d ", fibonacci);
            } else {
                printf("%d\n", fibonacci);
            }
        }
        contador++;
    }
    return 0;
}