/*Matrix addition,subtraction,multiplication,transpose*/
#include<stdio.h>
#include<stdlib.h>
void matrixtake(int d[][20], int r, int c)
{
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            scanf("%d", &d[i][j]);
        }
    }
}
void matrixdisplay(int d[20][20], int r, int c)
{
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            printf("%d ",d[i][j]);
        } printf("\n");
    }
}
void add(int a[][20], int b[][20],int r, int c)
{   
    matrixdisplay(a,r,c);
    printf("+\n");
    matrixdisplay(b,r,c);
    int e[20][20];
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            e[i][j]=a[i][j]+b[i][j];
        }
    }
    printf("=\n");
    matrixdisplay(e,r,c);
    printf("-------\n");
}
    void subtract(int a[][20], int b[][20],int r, int c)
{   
    matrixdisplay(a,r,c);
    printf("-\n");
    matrixdisplay(b,r,c);
    int e[20][20];
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            e[i][j]=a[i][j]-b[i][j];
        }
    }
    printf("=\n");
    matrixdisplay(e,r,c);
    printf("---------\n");
}
    void multiply(int a[][20], int b[][20],int r, int c)
{   
    matrixdisplay(a,r,c);
    printf("*\n");
    matrixdisplay(b,r,c);
    int e[20][20];
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {   
            e[i][j]=0;
            for(int k=0;k<r;k++)
            {
                e[i][j]= e[i][j] + a[i][k]*b[k][j];
            }
        }
    }
    printf("=\n");
    matrixdisplay(e,r,c);
    printf("-------\n");
}
void transpose(int a[][20],int r, int c)
{   
    matrixdisplay(a,r,c);
    printf("Transpose of matrix is\n");
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            a[i][j]=a[j][i];
        }
    }
    matrixdisplay(a,r,c);
    printf("--------\n");
}
void main()
{
    system("cls");
    int a[20][20] , b[20][20] , r,c;
    printf("Enter rows and columns-");
    scanf("%d%d",&r,&c);
    printf("Enter your 1st matrix-");
    matrixtake(a,r,c);
    printf("Enter your 2nd matrix-");
    matrixtake(b,r,c);
    printf("-------\n");
    add(a,b,r,c);
    subtract(a,b,r,c);
    multiply(a,b,r,c);
    transpose(a,r,c);
    transpose(b,r,c);
   }