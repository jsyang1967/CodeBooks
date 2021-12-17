#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#define SC struct coord
// fake bottom-up DP，同樣的子問題可能會算許多遍。
SC
{
    int x,y;
}xy[11];
int N;
int dp[1<<11][11];    // lookup table for memoization
int adj[11][11];  // adjacency matrix。兩點間的距離。
int ans;        // TSP的答案
 
void TSP(int s, int i, int s_size)
{
    
    if (s_size == N)
    {
        // 最後再加上一條回到原點的邊，形成環狀路線。
        if (dp[s][i] + adj[i][0] < ans)
            ans = dp[s][i] + adj[i][0];
        
        return;
    }
 
    for (int j=1; j<=N; ++j) // 只走第0點以外的點
        if (!(s & (1 << j)))
        {
            // ss = s + {j};
            int ss = s | (1 << j);
            if (!dp[ss][j] || dp[s][i] + adj[i][j] < dp[ss][j])
            {
                dp[ss][j] = dp[s][i] + adj[i][j];
                TSP(ss, j, s_size + 1);
            }
        }
}

int main(void)
{
    
    
    int i,j,k;
    int T;
    int x,y;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d %d",&x,&y);
        scanf("%d %d",&xy[0].x,&xy[0].y);
        scanf("%d",&N);
        for(i=1;i<=N;i++)
            scanf("%d %d",&xy[i].x,&xy[i].y);
        for(i=0;i<N;i++)
            for(j=i+1;j<=N;j++)
            {    
                adj[i][j] = abs(xy[i].x-xy[j].x)+abs(xy[i].y-xy[j].y);
                adj[j][i] = adj[i][j];
            }
        memset(dp, 0, sizeof(dp));
        ans = 1e9;
        TSP(0, 0, 0);   // 令商人從第0點出發。
        printf("The shortest path has length %d\n",ans);
    }
    
    
    return 0;
}