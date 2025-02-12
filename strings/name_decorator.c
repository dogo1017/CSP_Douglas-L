// Douglas London, TEMPLATE
#include <stdio.h>
#include <string.h>


char name[100] = "hi";

int main(void){
    
printf("Hello, this is my name decorator program. What is your first name? \n");
scanf("%s", name);

char str1[] = "~~~";  
char str2[] = "~~~";  

strcat(str1, name);

strcat(str1, str2);

printf(str1);
























    return 0;
}