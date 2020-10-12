#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
char n(char x){
switch (x) {
		case 'G': case 'Q': case 'a': case 'k': case 'u':
		return 0;
		case 'I': case 'S': case 'b': case 'l': case 'v':
		return 1;
		case 'E': case 'O': case 'Y': case 'c': case 'm': case 'w':
		return 2;
		case 'F': case 'P': case 'Z': case 'd': case 'n': case 'x':
		return 3;
		case 'J': case 'T': case 'e': case 'o': case 'y':
		return 4;
		case 'D': case 'N': case 'X': case 'f': case 'p': case 'z':
		return 5;
		case 'A': case 'K': case 'U': case 'g': case 'q':
		return 6;
		case 'C': case 'M': case 'W': case 'h': case 'r':
		return 7;
		case 'B': case 'L': case 'V': case 'i': case 's':
		return 8;
		case 'H': case 'R': case 'j': case 't':
		return 9;
	}
}
int main (){
	char D, frase[100];
	unsigned short qnt;
    int i;
	scanf("%hu", &qnt);
	while (qnt--){
		scanf(" %[^\n]",frase);
		i = 0;
		D = 0;
		while (frase[i]){
			if (isalpha(frase[i]))
				if (D < 12){
					printf("%hhd", n(frase[i]));
			    	D++;
				}
			i++;
		}
		printf("\n");
	}
}
