#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>
#include<ctype.h>
void main()
{
    char a[30], b[30];
    int i,l=0,digit=0,pun=0,upp=0,low=0;
    printf("Enter your email address-");
    scanf("%s",a);
    printf("Your email-%s",a);
    for(i=0;a[i]!='\0';i++,l++);
    printf("\nLenght-%d",l);
    for(i=0;i<l;i++)
    {
        if(isalpha(a[i])!=0)
        {
            if(islower(a[i])==0)
            {
                upp++;
            }
            else
            {
                low++;
            }
        }
        if(isdigit(a[i])!=0)
        {
            digit++;
        }
        if(ispunct(a[i])!=0)
        {
            pun++;
        }
        a[i]=tolower(a[i]);
        b[i]=toupper(a[i]);
    }
    printf("\nUpper characters-%d\nLower characters-%d\nDigits=%d\nSpecial characters-%d",upp,low,digit,pun);
    printf("Email address in lower case-%s",a);
    printf("\nEmail address in upper case-%s",b);
}