// Douglas London, expressions practice C
#include <stdio.h>
#include <math.h>

int first_equation = 7-24/8*4+6;
int second_equation = 18/3-7+2*5;
int third_equation = 6*4/12+72/8-9;
int fourth_equation = (17-6/2)+4*3;
int fifth_equation = -2*(1*4-2/2)+(6+2-3);
int sixth_equation = -1*((3-4*7)/5)-2*24/6;
int seventh_equation = (3*pow(5,2)/15)-(5-pow(2,2));
int eighth_equation = (pow(1, 4)*pow(2,2)+pow(3,3))-pow(2,5)/4;
int nineth_equation = pow((22/2-2*5), 2)+pow((4-6/6),2);

int main(void){
    printf("%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n", first_equation, second_equation, third_equation, fourth_equation, fifth_equation, sixth_equation, seventh_equation, eighth_equation, nineth_equation);
    return 0;
}