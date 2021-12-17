#include <iostream>
using namespace std;
#define N 101
#define max3(a, b, c) max(max(a, b), c)
int dp[N][N][N] = {0};
int main(void)
{
 string s1, s2, s3;
 cin >> s1 >> s2 >> s3;
 s1 = "0" + s1;
 s2 = "0" + s2;
 s3 = "0" + s3;
 int n1 = s1.length();
 int n2 = s2.length();
 int n3 = s3.length();
 for (int i = 1; i < n1; i++)
    for (int j = 1; j < n2; j++)
        for (int k = 1; k < n3; k++)
            if ((s1[i] == s2[j]) && (s2[j] == s3[k]))
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1;
            else
                dp[i][j][k] = max3(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1]);
 cout << dp[n1-1][n2-1][n3-1] << endl;
}