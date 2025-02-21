// Douglas London, Finantial calculator update C
#include <stdio.h>

float inputs(char type[20], int input[50]){
    printf("What is your monthly %s cost:\n", type);
    scanf("%f", &input);
    return;
}

float income;
float utilities;
float groceries;
float transportation;


int main(void){
    
printf("Hello, this is my finantial calculator that calculates savings, spendins, and other finantial expenses.\n");
printf("What is your monthly income:\n");
scanf("%f", income);

float rent = inputs("rent", 0);








    return 0;
}