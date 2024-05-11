#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<time.h>
#include<math.h>
#include<unistd.h>
#include<string.h>
#include<ctype.h>
struct report
{
    char name[10];
    int marks[5] , roll ;
};
typedef struct report report;
void choose(report *r, char sub[5][10], int f , int n);
void data(report* r, char sub[5][10],int f,int n);
void create(report *r, char sub[5][10],int f, int n);
void display(report *r, char sub[5][10] ,int f, int n);
void add(report *r, char sub[5][10], int f, int n);
void choose(report *r, char sub[5][10], int f , int n)
{
    system("cls");
    int ch;
    printf("Choose-\n1.Add more\n2.Display\n3.Top Three\n4.Exit\n");
    scanf("%d",&ch);
    switch(ch)
    {
        case 1:
        add(r,sub,f,n); break;
        case 2:
        display(r,sub,f,n); break;
        case 3:
        printf("Under way"); break;
        case 4:
        exit(0); break;
        default :
        printf("Wrong Choice\n");
        choose(r,sub,f,n);
    }
}
void data(report *r, char sub[5][10],int f,int n)
{
    int sum; int i;
    for(int h=f;h<n;h++)
    {   
        sum=0;
        printf("Enter name-");
        scanf("%s",&(r+h)->name);
        printf("Enter marks-\n");
        for(i=0;i<3;i++)
        {
            printf("%s-",sub[i+1]);
            scanf("%d",&(r+h)->marks[i]);
            sum=(r+h)->marks[i] + sum;
        }
        (r+h)->marks[3]= sum/3;
    }
    choose(r,sub,f,n);
}
void create(report *r, char sub[5][10],int f, int n)
{
    r=(report*)malloc(n*sizeof(report));
    data(r,sub,f,n);
}
void add(report *r, char sub[5][10], int f, int n)
{
    f=n;
    printf("Enter number of students-");
    scanf("%d",&n);
    n=n+f;
    r= (report*)realloc(r,n*sizeof(report));
    data(r,sub,f,n );
}
void display(report *r, char sub[5][10] ,int f, int n)
{
    system("cls");
    printf("Marks List\n");
    
    for(int l=0;l<5;l++)
    {
    printf("%s\t",sub[l]);
    }
    printf("\n");
    for(int k=0;k<n;k++)
    {
        printf("%s",(r+k)->name);
        {
            for(int o=0;o<4; o++)
            {
                printf("\t%d",(r+k)->marks[o]);
            }
        }
        printf("\n");
    }
    getch();
    system("cls");
    choose(r,sub,f,n);
}
void main()
{  
    int n,f=0; char sub[5][10]={"Name","Physics","Maths","C-lang","Percentage"};
    report *r;
    printf("Enter number of students-");
    scanf("%d",&n);
    create(r,sub,f,n);
}