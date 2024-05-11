#include <stdio.h>
#include <stdlib.h>
   void character(int *a)
{
    printf("Character value is %c\n",*a);
}
   void hexadecimal(int *a)
{
    printf("Hexadecimal value is %x\n",*a);
}   
   void octal(int *a)
{
    printf("Octal value is %o\n",*a);
}  
   void pointer(int *a)
{
    printf("Pointer/address is %p\n", &a);
}   
   void number(int* a)
{
    printf("Number value is %d\n",*a);
}  
   void main()
{
    int a,c; char ch,b;
  do 
    {  system("cls");
       printf("Choose-\n1.ChARACTER\n2.NUMBER\n");
       scanf("%d",&c);
       if (c==1)
     {
       printf("Enter-");
       scanf("%s",&b);
       a=b;
       character(&a);
       number(&a);
       hexadecimal(&a);
       octal(&a);
       pointer(&a);
     } 
       else if (c==2)
     {
       printf("Enter=");
       scanf("%d",&a);
       number(&a);
       character(&a);
       hexadecimal(&a);
       octal(&a);
       pointer(&a);
     }  
       else { printf("Wrong Choice-Choose 1 or 2\n"); }
       printf("Do you want to continue(Y/N)-");
       scanf("%s",&ch);
    } while (ch=='Y'||ch=='y') ; 
}