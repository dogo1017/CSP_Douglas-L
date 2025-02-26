// Douglas London, old enough C
#include <stdio.h>

int age;


int main(void){

    printf("Welcome to my old enough program that tells you whether you are old enough to vote, drive, get a learners permit, and go to school.\n");

    printf("What is your age:\n");
    scanf("%d", &age);
    
    if(age >= 18){
        printf("You can vote\n");
    }else if(age >= 16){
        printf("you can drive\n");
    }else if(age >= 15){
        printf("You can get a learners permit\n");
    }else if(age >= 4){
        printf("You can go to school");
    }else{
        printf("How the frick is a todler working this program!!! You should not be able to even read! Go back to watching cocomelon little nerd.");
    }


    
    return 0;

}