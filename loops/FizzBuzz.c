// Douglas London, FizzBuzz c
#include <stdio.h>

int main(void){
    
int number = 0;
while (number <= 50){
    if (number == 0){
        print(0);
        number += 1;
    }else if(number%3==0 && number%5==0){
        print("FizzBuzz");
        number += 1;
    }else if(number%5==0){
        print("buzz");
        number += 1;
    }else if (number%3==0){
        print("fizz");
        number += 1;
    }else{
        print(number);
        number += 1;
    }
}








    return 0;
}