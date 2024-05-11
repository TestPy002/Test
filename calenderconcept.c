#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<time.h>
#include<math.h>
#include<unistd.h>
#include<string.h>
#include<ctype.h>
int day,d,m;
char name[12][6]={"Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"};
void month();
int give(int n);
void printmon(int m,int d,int day)
{
    if(m==12) exit(0);
    int q;
    printf("\n%s\n",name[m]);
    int k=day; int l=1;
    int i,j;
    q=give(m+1);
    q++;
    while(l<q)
    {
        for(j=1;j<8&&l<q;j++)
        {
            if(j<k)
            {
                printf("\t");
            }
            else
            {
            printf("%d\t",l);
            l++;
            }
        }
            k=0;
        printf("\n");
    }
    printmon(m+1,1,j);
}
void current()
{
    time_t t=time(NULL);
    struct tm *now = localtime(&t);
    day=now->tm_wday;
    d=now->tm_mday;
    m=now->tm_mon;
    month();
}
int give(int n)
{
    switch(n)
    {
        case 1:
        return 31;
        case 2:
        return 28;
        case 3:
        return 31;
        case 4:
        return 30;
        case 5:
        return 31;
        case 6:
        return 30;
        case 7:
        return 31;
        case 8:
        return 31;
        case 9:
        return 30;
        case 10:
        return 31;
        case 11:
        return 30;
        case 12:
        return 31;
    }
}
void month()
{
    char a[5][7]; int i=day,j,l;
        for(l=m+1;l>0;l--)
        {
        for(j=d;j>0;j--,i--)
        {
            if(i==0) i=7;
        }
        if((j==0)&&(l>1))
        {
            d=give(l-1);
        }
        }
        j++; i++;
        if(i==7) i=0;
        printf("%d month %d date %d day\n",l,j,i);
        time_t t=time(NULL);
    struct tm *now = localtime(&t);
    now->tm_wday=i;
    now->tm_mon=l;
    now->tm_mday=j;
    printf("%s",asctime(now));
    if(i==0) i=7;
    printmon(l,j,i);
}
void main()
{
    current();
}
//3rd day,20th day,12th month