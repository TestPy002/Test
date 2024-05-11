#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<time.h>
#include<math.h>
#include<unistd.h>
#include<string.h>
#include<ctype.h>

void main()
{
    time_t p;
    p=time(NULL);
    struct tm *t;
    t=localtime(&p);
    char buf[200];
    strftime(buf, sizeof(buf), "%Y %m %d %H %M %S", gmtime(&p));
    printf("%s\n", buf);
}