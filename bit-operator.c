#include <stdio.h> 
#include<stdlib.h>
void binary(int n)
{  int i,a[20];
    for (i = 0; n > 0; i++) {
        a[i] = n % 2;
        n = n / 2;
    }

    printf("\nBinary Format:");

    // Loop to print the binary format of given number
    for (i = i - 1; i >= 0; i--) 
    {
        printf("%d", a[i]);
    }
    printf("\n");
}
void andbit(int a, int b)
{   int d;
    printf("%d\n%d",a,b);
    binary(a); printf("\n");
    binary(b);
    printf("\t&");
    d=a&b; printf("\n");
    binary(d);
    printf("%d & %d = %d",a,b,d);

}
void orbit(int a, int b)
{
    int d;
    printf("\n%d\n%d",a,b);
    binary(a);
    binary(b);
    printf("\t|");
    d=a|b; printf("\n");
    binary(d);
    printf("%d | %d = %d",a,b,d);

}
void xorbit(int a, int b)
{
    int d;
    printf("\n%d\n%d",a,b);
    binary(a);
    binary(b);
    printf("\t^");
    d=a^b; printf("\n");
    binary(d);
    printf("%d ^ %d = %d",a,b,d);

}
void leftshift(int c)
{   
    int n,e;
    printf("\nEnter how much you want to shift-");
    scanf("%d",&n);
    printf("%d",c);
    binary(c);
    e= c<<n;
    printf("\n");
    binary(e);
    printf("Left shift by %d times, %d = %d",n,c,e);
}
void rightshift(int c)
{   
    int n,e;
    printf("\nEnter how much you want to shift-");
    scanf("%d",&n);
    printf("%d",c);
    binary(c);
    e= c>>n;
    printf("\n");
    binary(e);
    printf("Right shift by %d times, %d = %d",n,c,e);
}
void complement(int c)
{   
    int e;
    printf("\n%d",c);
    binary(c);
    e= ~c;
    printf("\n");
    binary(e);
    printf("complement, %d = %d",c,e);
}


int main() 
{ 
    system("cls");
    int a,b,c;
    printf("Enter two numbers for bit operations-");
    scanf("%d%d",&a,&b);
    andbit(a,b);
    orbit(a,b);
    xorbit(a,b);
    printf("\nEnter number for left,right shift and complement-");
    scanf("%d",&c);
    leftshift(c);
    rightshift(c);
    complement(c);
    return 0; 
} 