// Libarary functions of string
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<conio.h>
int first(char a[], int p)
{
    int i,l=0;
    for(i=0;i<p, isblank(a[i])==0 ;i++,l++); //isblank gives 0 if character not blank space
    return l;
}
int back(char a[], int q)
{
    int i,l=0;
    for(i=q+1;a[i]!='\0';i++,l++);
    return l;
}
void main()
{
    system("cls");
    printf("STRING BASIC FUNCTIONS EXAMPLE-\n");
    char a[20],b[20];
    printf("Enter name of groom-");
    scanf("%[^\n]%*c",a); // takes spaces as input also
    printf("Groom-%s",a);
    printf("\nEnter name of bride-");
    scanf("%[^\n]%*c",b);
    printf("Bride-%s\n",b);
    int x,y;
    x=strlen(a); // strlen counts spaces too in string along with all characters
    y=strlen(b);
    printf("1st-%d\t2nd-%d",x,y);
    // we have to count characters before blank space, we will use ctype functions
    int h,k;
    h=first(a, x);
    k=first(b, y);
    printf("\nLenght of first word in groom name-%d",h);
    printf("\nLenght of first word in bride name-%d",k);
    int z,w;
    z=back(a,h);
    w=back(b,k);
    printf("\nLenght of last word in groom name-%d",z);
    printf("\nLenght of last word in bride name-%d",w);
    char c[h],d[y-k];
    strcpy(c,&a[h]); //copies 2nd string to 1st string and also can copy string from any point by giving address where to copy(a[x])
    strncpy(d,b,k);  // copies n characters of 2nd string to 1st string
    strcat(d,c);  // joins 2nd string to end of 1st string and strncat joins first n characters of 2nd string , can use address too like above
    printf("\nWife name-%s\n",d);
    printf("--------------------\n");
    printf("string compare function demo-\n");
    char str[10]; char str2[10];
    printf("Enter word-");
    scanf("%s",str);
    printf("1st string = %s\n",str);
    strcpy(str2,str);
    strrev(str2); //reverses the string
    printf("2nd string(1st string reverse order) = %s\n",str2);
    int san=strcmp(str,str2); // compares 2 strings and gives 0 if both equal
    if(san==0)
    {
        printf("1st String is pallindrome"); // says not pallindrome if letters differ upper and lower so use tolower
    }
    else {printf("Not pallindrome");}
    getch();
    system("cls");
    printf("STRING EXTRA FUNCTIONS");
    char para[]={"Creepy pasta is best horror stuff"} , *ret , *las;
    printf("para is %s\n",para);
    ret=strchr(para, 'p'); //gives a pointer pointing to first occured character(p) that is searched
    las=strrchr(para , 't'); // gives a pointer pointing to last occured character(t) that is searched
    printf("Para from first p-%s\n",ret);
    printf("Para from last t-%s\n",las);
    ret=strstr(para, "horror"); //gives a pointer pointing to first letter of pasta in para (exact 'pasta' should be present in para)
    printf("Para from pasta-%s\n",ret);
    ret=strpbrk(para, "pAzpek"); /*gives a pointer pointing to first available letter in Azpek, here e is first in para so pointer points to it*/
    printf("Para containing any character from A,z,p,e,k-%s\n",ret);
    int q=strspn(para, "Cpasta"); //checks letters of para with cpasta, gives no of same characters but breaks when one character is different
    printf("No of characters Para containing Cpasta-%d\n",q); // gives 1 because it breaks since e not equal to p
    q=strcspn(para, "pasta"); //checks if letters of para not equal to 'p'asta, breaks once it gets same
    printf("No of characters until pasta comes-%d\n",q); // p of Creepy gets equal to p of pasta so only 'cree' is before so answer is 4
    printf("String functions end here\n---------------------------\n");
}

