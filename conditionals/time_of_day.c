// Douglas London, Time of day C
#include <stdio.h>
#include <time.h>





int main(void){
    

    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;

    if(hour < 12){
    printf("Good morning!");
    }else if(hour < 17){
    printf("Good afternoon!");
}else{
    printf("Good evening!");
}






    return 0;
}