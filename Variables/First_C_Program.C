#include <stdio.h>

char name;

int main(void){

    printf("What is your name: ");
    scanf("%s", &name);
    printf("Hi %s", &name);
    return 0;
}