#include<stdio.h>
int main(){
    int secret[4];
    int guess[4];
    int check[4];
    int n;
    int p,q;
    int i,j,k;
    while(scanf("%d %d %d %d",&secret[0],&secret[1],&secret[2],&secret[3])!=EOF)
    {


        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            q=0;
            p=0;
            for(i=0;i<4;i++)
            {
                scanf("%d",&guess[i]);
                if(guess[i]==secret[i])
                {
                    p++;
                    check[i]=1;
                }
                else
                    check[i]=0;
            }

            for(i=0;i<4;i++)
            {
                if(check[i]!=1)
                    for(k=0;k<4;k++)
                        if(check[k]==0 && secret[i]==guess[k])
                            {
                                q++;
                                check[k]=2;
                                break;
                            }
            }printf("%dA%dB\n",p,q);
        }
    }
    return 0;
}