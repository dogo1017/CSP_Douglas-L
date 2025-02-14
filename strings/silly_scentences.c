// Douglas London, Silly scentences C
#include <stdio.h>
// empty string variables for user words (minimum 3)

char adj1[50];                    
char noun2[50];
char verb_pt3[50]; 
char adv4[50];
char adj5[50];
char noun6[50];
char noun7[50];
char adj8[50];
char verb9[50];
char adv10[50]; 
char verb_pt11[50]; 
char adj12[50];

int main(void){
    
//welcome user


printf("welcome to my silly scentences program. When the program asks for a specific category of word you will think of one and respond with one, and only one, of those words to fill out a scentence.\n");

//ask for words (print with scanf) (in C we need to tell the user they can only type one word)

//print the story with inserted variables ("welcome %s to my progtram", name)

printf("adjective:\n");
scanf("%s", adj1);
printf("noun:\n");
scanf("%s", noun2);
printf("verb in past tense:\n");
scanf("%s", verb_pt3);
printf("adverb:\n");
scanf("%s", adv4);
printf("adjective:\n");
scanf("%s", adj5);
printf("noun:\n");
scanf("%s", noun6);
printf("noun:\n");
scanf("%s", noun7);
printf("adjective:\n");
scanf("%s", adj8);
printf("verb:\n");
scanf("%s", verb9);
printf("adverb:\n");
scanf("%s", adv10);
printf("verb in past tense:\n");
scanf("%s", verb_pt11);
printf("adjective:\n");
scanf("%s", adj12);


printf("Today I went to the zoo. I saw a(n) %s %s jumping up and down in its tree. He %s %s through the large tunnel that led to its %s %s. I got some peanuts and passed them through the cage to a gigantic gray %s towering above my head. Feeding that animal made me hungry. I went to get a %s scoop of ice cream. It filled my stomach. Afterwards I had to %s %s to catch our bus. When I got home I %s my mom for a %s day at the zoo.", adj1, noun2, verb_pt3, adv4, adj5, noun6, noun7, adj8, verb9, adv10, verb_pt11, adj12);



    return 0;
}

