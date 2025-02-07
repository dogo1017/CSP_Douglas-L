// Douglas London, Financial Calculator
#include <stdio.h>

int main(void){
    

float income = 0;
// ask user what their rent is (wariable and input)
float rent =0;
// ask user what their utilities is (wariable and input)
float utilities =0;
// ask user what their groceries is (wariable and input)
float groceries = 0;
// ask user what their transportation is (wariable and input)
float transportation = 0;



// printf statement that welcomes user and tells what the program does
printf("Hello, this is my financial calculator that calculates savings, spendings, and other financial expenses.\n");
// ask user what their income is (wariable and input)
printf("what is your monthly income?\n");
scanf("%f", &income);
// ask user what their rent is (wariable and input)
printf("what is your mothly cost of rent?\n");
scanf("%f", &rent);
// ask user what their utilities is (wariable and input)
printf("what is your monthly cost of utilities?\n");
scanf("%f", &utilities);
// ask user what their groceries is (wariable and input)
printf("what is your monthly cost of groceries?\n");
scanf("%f", &groceries);
// ask user what their transportation is (wariable and input)
printf("what is your monthly spend on transportation?\n");
scanf("%f", &transportation);
// calculate savinggs as 10% of income (income*.1) (variable)
float savings = income*.1;
// calculate spending as income-savings-rent-untilities-groveries-transportation (variable)
float spendings = income-savings-rent-utilities-groceries-transportation;
// calculate percent income of rent  (rent/income*100) (variable)
float rent_percent = rent/income*100;
// calculate percent income of utilities  (utilities/income*100) (variable)
float utilities_percent = utilities/income*100;
// calculate percent income of groceries (groceries/income*100) (variable)
float groceries_percent = groceries/income*100;
// calculate percent income of transportation (transportation/income*100) (variable)
float transportation_percent = transportation/income*100;
// calculate percent income of spending (spending/income*100) (variable)
float spending_percent = spendings/income*100;
//  your rent is $XX.XX which is XX% of your income. (printf)
printf("your rent is $%.2f, which is %.2f%% of your income.\n", rent, rent_percent);
//  your utilities is $XX.XX which is XX% of your income. (printf)
printf("your utilities is $%.2f, which is %.2f%% of your income.\n", utilities, utilities_percent);
//  your groceries is $XX.XX which is XX% of your income. (printf)
printf("your groceries is $%.2f, which is %.2f%% of your income.\n", groceries, groceries_percent);
//  your transportation is $XX.XX which is XX% of your income. (printf)
printf("your transportation is $%.2f, which is %.2f%% of your income.\n", transportation, transportation_percent);
//  your savings is $XX.XX which is XX% of your income. (printf)
printf("your savings is $%.2f, which is 10%% of your income.\n", savings);
// //  your spending is $XX.XX which is XX% of your income. (printf)
printf("your spendings is $%.2f, which is %.2f%% of your income.\n", spendings, spending_percent);











    return 0;
}