// Douglas London, Time C
#include <stdio.h>
#include <time.h>




int main(void){
    //time scince Jan 1 1970
    time_t seconds;
    seconds = time(NULL);
    //printf("seconds since Jan 1, 1970 = %d\n", seconds);

    //Current time
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    //printf("current time and date is %s\n", asctime(timeinfo));

    //current hour
    time_t now = time(NULL);

    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    printf("%d\n", hour);




    return 0;
}