#include <iostream>
using namespace std;
int main()
{
    int n,a,index,reverse,rem;     
    //g++ c.cpp -o main
    //./main < 1.in
    while(cin>>n)
    {
        a=0; 
        index = 0;
        reverse=0;
        while(n!=0)    
        {    
            rem=n%10;      
            reverse=reverse*10+rem;    
            n/=10;    
        } 
        n=reverse;  
        a+=n%10;
        n/=10;  
        while(n>0)  
        {  
        
            if(index % 2 == 0)
            {
                a+=n%10;
            }
           
            else 
            {
                a-=n%10;
            }
            index += 1;
            n/=10;  
        }  
        cout<<a<<endl;    
    }  
   
    return 0;
}