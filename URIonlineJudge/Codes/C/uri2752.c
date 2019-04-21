#include <stdio.h>

int main() {
    char vetor[50] = "AMO FAZER EXERCICIO NO URI";

    printf("<%s>\n", vetor);
    printf("<%30s>\n", vetor);
    printf("<%.20s>\n", vetor);
    printf("<%-20s>\n", vetor);
    printf("<%-30s>\n", vetor);
    printf("<%.30s>\n", vetor);
    printf("<%30.20s>\n", vetor);
    printf("<%-30.20s>\n", vetor);
    return 0;
}