#include<stdio.h>

int main(){

    int I;
    int i, j;

    while(scanf("%d", &I) && I){

        int P = 0;
        int bit[31] = {0};

        for(i = 0; I > 0; i++){
            if(I & 1){
                P++;
            }
            bit[i] = I & 1;
            I >>= 1;
        }

        printf("The parity of ");
        for(j = i - 1; j >= 0; j--){
            printf("%d", bit[j]);
        }
        printf(" is %d (mod 2).\n", P);
    }

    return 0;
}