#include <stdio.h>
#include <stdlib.h>

int main()
{
    int m, n, d, sum=0;
    while(1)
    {
        scanf("%d %d", &m, &n);

        if (m<=0 || n<=0){
            break;
        }

        else{
            if (m<n){
                for(d=m; d<=n; d++){
                    printf("%d ", d);
                    sum+=d;
                }
                printf("Sum=%d\n", sum);
                sum=0;
            }
            else if (m>n) {
                for (d=n; d<=m; d++){
                    printf("%d ", d);
                    sum+=d;
                }
                printf("Sum=%d\n", sum);
                sum=0;
            }
            else if (m=n){
                printf("%d ", m);
                printf("Sum=%d", m);
            }
            sum=0;
        }
    }
        return 0;
}
