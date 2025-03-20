// Douglas London, Conditionals Notes C
#include <stdio.h>
#include <string.h> // needed to compare strings

char name[] = "Treyson";
int num;

int main(void){
//How do you write an if statement in C?
if(strcmp(name, "Douglas") == 0){ // strcmp is for comparing strings
    printf("Hello Douglas, Welcome to class.");


//How do you write else statements in C?
}else{
    printf("Hello %s Welcome to class.\n", name);


printf("How many siblings do you have?\n");
scanf("%d", &num);
//How do you write elif/ else if statements in C?
if(num == 0){
    printf("you are an only child\n");
}else if(num <= 2){
    printf("you have a couple siblings\n");
}else if(num <= 5){
    printf("You have a few siblings\n");
}else{
    printf("You have a lot of siblings\n");
}

//How do you write the 3 logical operators in C?

// && = and
// || = or
// ! = not


if(num == 7 || num == 13){
    printf("That is an unlucky number\n");
}else if(num <10 && num > 5){
    printf("%d is a large single digit number\n", num);

}else if(!(num < 10)){
    if(num == 12){
        printf("thats a dozen!\n");
    }else{
    printf("%d is a big number\n");
    }
}else{
    printf("you typed in %d\n", num);
}


    return 0;
}