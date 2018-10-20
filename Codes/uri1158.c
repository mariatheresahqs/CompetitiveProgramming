#include <stdio.h>

int main() {
    int n, x, y,i=0, j=0, soma=0, k=0, impar = 0;
    scanf("%d", &n);
    for(i=0;i<n;i++){
        scanf("%d %d", &x, &y);
        if (x%2==0){
            while(j<y) {
                impar = x +1 +k;
                soma += impar;
                k+=2;
                j++;
            }
        }
        else if(x%2!=0){
            while(j<y) {
                impar = x + k;
                soma += impar;
                k+=2;
                j++;
            }
        }
        printf("%d\n", soma);
        soma=0;
        impar = 0;
        k=0;
        j=0;
    }
    return 0;
}