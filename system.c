#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void main()
{
    char file[]={"test.csv"};
    char exe[]={"cmd/c"}; //cmd/c prefix for system command, it is similar to command prompt
    strcat(exe,file);
    //system(exe); // after cmd/c write file/app exe path by copying from pc
    //system("START www.google.com"); //using start prefix we can open any website by its url
    //system("cmd/c calender"); //write c file or any code file to run it
    //if used .c with file name then it opens file, else it runs exe file and code output comes
    //system("cmd/c navigation");
    //system("cmd/c C:\\Users\\hp\\Edge\\Application\\msedge.exe");
    //system("cmd/c C:\\Users\\hp\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe");
    //system("cmd/c \"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe\"");
    //system("START ms-windows-store:");
    //system("start microsoft.windows.camera:");
    system("cmd/c C:\\Users\\hp\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe");
    //system("cmd/c calc");
    //system("start calc");
}