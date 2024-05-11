//Bit operator interesting operators
#include<stdio.h>
#include<stdlib.h>
int oppositeSigns(int x, int y) 
{ 
	return ((x ^ y) < 0); 
} 

void main ()
{
    system("cls");
    int a;
    printf("Enter number to check odd/even using bitwise AND:-");
    scanf("%d",&a);
    (a&1)? printf("odd") : printf("even"); // eg. a=5, 5= 1001, then 5&1= 1001 & 0001 = 1, 1 is true, then print odd
    printf("\n");
    // C code to swap using XOR
    int p,q;
	printf("Enter 2 numbers-");
    scanf("%d%d",&p,&q);
	// Code to swap 'x' (1010) and 'y' (0101)
	p = p ^ q; // x now becomes 15 (1111)
	q = p ^ q; // y becomes 10 (1010)
	p = p ^ q; // x becomes 5 (0101)

	printf("After Swapping: p = %d, q = %d", p, q);
    printf("\n");
    // C Program to Detect 
// if two integers have opposite signs. 
	int x,y;
    printf("Enter 2 numbers-");
    scanf("%d%d",&x,&y);
	oppositeSigns(x,y) ?
	printf ("Signs are opposite"):
	printf ("Signs are not opposite"); 
} 