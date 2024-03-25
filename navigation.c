#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
void display(int n)
{
    switch(n)
    {
    case 1:
    system("cls");
    printf("1\n\n"); break;
    case 2:
    system("cls");
    printf("2\n"); break;
    case 3:
    system("cls");
    printf("3\n"); break;
    case 4:
    system("cls");
    printf("4\n"); break;
    case 5:
    system("cls");
    printf("5\n"); break;
    }
}

int main()
{
    int chr1, chr2; int i=0; int c;
    for(int j=0;j<6;j++)
    {
    printf("Press any arrow key...\n");
    //c=getch();
    //if(c!=0xE0) {printf("hel");}
    //else
    //{
    chr1 = getch();
    if (chr1 == 0xE0) //to check scroll key interrupt
    {
    chr2 = getch();  //to read arrow key
    switch(chr2)
    {
    case 75: printf("LEFT ARROW KEY PRESSED\n");
        if(i==0||i==1)
        {
            break;
        }
        i--; display(i);
        break;
    case 77: printf("RIGHT ARROW KEY PRESSED\n");
    if(i==5)
    {
        break;
    }
            i++; display(i);
        break;
    default: printf("OTHER KEY PRESSED: %d %d\n", chr1, chr2);
        break;
    };
    } 
    else {printf("Hel");}  
    }
    //}
    return 0;
}