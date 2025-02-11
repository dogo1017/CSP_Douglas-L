// Douglas London, string notes c
#include <stdio.h>
#include <string.h>

char subject[50];
char scentence[] = "The quick brown fox jumps over the lazy dog.";

int main(void){
    //printf("What class are you in?\n");
    //scanf("%s", subject);
    //fgets(subject, sizeof(subject), stdin);
   // printf("You are in %s, that is a cool class.", subject);
   //name[0] = 'T';
   //name[1] = 'o';
   //name[2] - 'r';
   //name[3] = 'i';
   printf("%lu\n",sizeof(scentence));
   printf("%d\n", strlen(scentence));

char one[] = "hello ";
char two[] = "world!";
char three[] = "welcome to my program. ";
printf("%s\n", one);
strcat(one, two);
printf("%s\n", one);
strcat(three, one); //can only do 2 at a time
printf("%s\n", three);
    return 0;
}