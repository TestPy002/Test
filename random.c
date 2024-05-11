#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<time.h>
void randomfloat(int l, int u, int n)
{
    int i;
    for(i=0; i<n ; i++)
    {
        
        float num= ((float)rand()/RAND_MAX)*(u-l) + l;
        printf("%.2f ",num);
    }
}
void randomint(int l, int u, int n)
{
    int i;
    for(i=0; i<n ; i++)
    {
        
        float num= (rand()%(u-l+1)) + l;
        printf("%.2f ",num);
    }
}
void main()
{
    int n; int u,l;
    srand(time(0));
    printf("Enter number of random numbers-");
    scanf("%d",&n);
    //printf("Enter the min number-");
    //scanf("%d",&l);
    printf("Enter the max number-");
    scanf("%d",&u);
    //randomfloat(l,u,n);
    randomize();
    for(int i=0; i<n ; i++)
    {
        printf("%d ", random(u));
    }
}