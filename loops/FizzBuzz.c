// Douglas London, FizzBuzz c
#include <stdio.h>

int main(void){
    
int number = 0;
while (number <= 50){
    if (number == 0){
        printf("0\n");
        number += 1;
    }else if(number%3==0 && number%5==0){
        printf("FizzBuzz\n");
        number += 1;
    }else if(number%5==0){
        printf("buzz\n");
        number += 1;
    }else if (number%3==0){
        printf("fizz\n");
        number += 1;
    }else{
        printf("%d\n", number);
        number += 1;
    }
}








    return 0;
}