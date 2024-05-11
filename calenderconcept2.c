#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<time.h>
#include<math.h>
#include<unistd.h>
#include<string.h>
#include<ctype.h>

void timeprint();
int days(int n);
/*void start();
void printmon();
void calender();
void notes();
void screen();*/

int days(int n)
{
    switch(n)
    {
        case 1:
        return 31;
        case 2:
        return 29;
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
void screen()
{
    printf("THIS IS A CALENDER PLANNER");
    printf("\nInstructions\n");
    printf("1.Use arrow keys to navigate between months\n");
    printf("2.Type day number to set a note\n");
    printf("3.Tap enter for refresh\n");
    printf("4.Tap esc key to exit\n");
    printf("Press any key to see calender\n");
}
void timeprint()
{
    time_t t=time(NULL);
    printf("%s",ctime(&t));
}
void start()
{
    int day,m,d;
    time_t t=time(NULL);
    struct tm *now = localtime(&t);
    day=now->tm_wday;
    d=now->tm_mday;
    m=now->tm_mon;
    int i=day,j,l;
        /*for(l=m+1;l>0;l--)
        {
        for(j=d;j>0;j--,i--)
        {
            if(i==0) i=7;
        }
        if((j==0)&&(l>1))
        {
            d=days(l-1);
        }
        }*/ int o=0; int u=days(m+1); int z;
        for(l=m+1;(l<13)&&(o<2);)
        {
            for(j=d;j<u+1;j++,i++)
        {
            if(i==7) i=0;
            printf("%d day %d date %d l\n",i,j,l);
        }
        if((j==u+1)&&(l<13))
        {
            if(l==12) z=1;
            else z=l+1;
            u=days(z);
            printf("\nl-%d u-%d\n",z,u);
        }
        if(l==12) {l=1; o=o+1; d=1;}
        else {l=l+1;}
            printf("%d day %d date %d year %d l\n",i,j,o,l);
            if(l==3) break;
        }
        printf("\nl-%d\n",l);
        j--; i--;
        if(l==1) l=11;
        else l=l-2;
        if(i==7) i=0;
        printf("%d month %d date %d day\n",l,j,i);
        time_t tp=time(NULL);
    struct tm *now1 = localtime(&tp);
    now1->tm_wday=i;
    now1->tm_mon=l;
    now1->tm_mday=j;
    now1->tm_year=now1->tm_year+1;
    printf("%s",asctime(now1));
    if(i==0) i=7;
    //printmon(l,j,i);
}

void main()
{
    //screen();
    start();
}