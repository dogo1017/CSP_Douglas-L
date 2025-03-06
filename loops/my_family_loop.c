// Douglas London, my family loop C
#include <stdio.h>



int main(void){

char members[][20] = {"Brielle", "Sarianne", "Rosalie", "Bennett"};


int xlenght = sizeof(members)/sizeof(members[0]);

int x;
for(x=0;x<xlenght;x++){
    printf("Hello %s\n", members[x]);
}






    return 0;
}