#include <stdio.h>

int main(){
    int n, count, x, y;
    double divi;
    
    scanf("%d", &n);
    for (count=0; count<n; count++){
        scanf("%d %d", &x, &y);
        
        if (y==0)
            printf("divisao impossivel\n");
        else {
            divi=x/(y*1.00);
            printf("%.1lf\n", divi);

        }
    }
    return 0;
}
