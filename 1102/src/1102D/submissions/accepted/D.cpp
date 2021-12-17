#include<bits/stdc++.h>
using namespace std;
 
typedef long long LL ;
int n ; LL ai ,sum=0 ,min_odd=1LL<<30 ;
 
int main(){
    scanf("%d",&n ) ;
    for (int i=0 ;i<n;i++ ){
        scanf("%I64d",&ai ) ;
        sum+=ai ;
        if (ai%2==1)min_odd=min(min_odd,ai) ;
    }
    if (sum%2==1)sum-=min_odd ;
    cout << sum <<endl ;
}