// Douglas London, 
#include <stdio.h>

char name[20];

int main(void){

    printf("What is your name: \n");
    scanf("%s", &name);
    printf("Hi %s", &name);
    return 0;
}