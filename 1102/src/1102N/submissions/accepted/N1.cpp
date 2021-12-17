#include <iostream>
using namespace std;  
string word1, word2;
int min(int a,int b,int c)
{
    return c>(a>b?b:a)?(a>b?b:a):c;
}  
int main() {
    cin >> word1 >> word2;
    int table[word1.size()+1][word2.size()+1];
    for(int i=0;i<=word1.size();i++) table[i][0]=i;
    for(int i=0;i<=word2.size();i++) table[0][i]=i;
    for (int i = 1; i <= word1.size(); i++)
    {
        for (int j = 1; j <= word2.size(); j++)
        {
            table[i][j] = min(table[i - 1][j] + 1, table[i][j - 1] + 1, table[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]));
        }
    }
    cout <<  table[word1.size()][word2.size()];
 
}