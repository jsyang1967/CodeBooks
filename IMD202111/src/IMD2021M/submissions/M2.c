#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<queue>

using namespace std;

const int INF = 0x3f3f3f3f;

int n,m;
int a[110][110];//鄰接矩陣
int vis[110];//標記是否在隊列中，“1”是，“0”否
int dist[110];//dist[i]表示從起點到vi的最短路徑的長度
int path[110];//path[i]表示從起點到vi的最短路徑上頂點vi的前一個頂點序號

void Bellman_Ford()
{
    memset(vis,0,sizeof(vis));
    memset(path,-1,sizeof(path));
    memset(dist,INF,sizeof(dist));
    queue<int>que;
    que.push(1);
    dist[1] = 0;
    vis[1] = 1;
    while(que.size())
    {
        int x = que.front();
        que.pop();
        vis[x] = 0; //清除“在隊列中”標誌
        for(int i = 1;i <= n;i++)
        {
            if(dist[i] > dist[x] + a[x][i])
            {
                dist[i] = dist[x] + a[x][i];
                path[i] = x;
                if(!vis[i]) //如果已經在隊列中，就不要重複加了
                {
                    vis[i] = 1;
                    que.push(i);
                }
            }
        }
    }
}

int main()
{
   while(~scanf("%d",&n))
   {
       if(n == 0)
            break;
       scanf("%d",&m);
       memset(a,INF,sizeof(a));//初始化鄰接矩陣
       for(int i = 0;i < n;i++)
            a[i][i] = 0;
       int u,v,w;
       for(int i = 0;i < m;i++)
       {
           scanf("%d %d %d",&u,&v,&w);
           a[u][v] = w;
           a[v][u] = w;
       }
       Bellman_Ford();//求最短路徑
       int ans = dist[n];
       int s = 1,t = n;
       /*將第一次求得的最短路徑所經過的邊進行修改
       例如：經過了邊(u,v)，則先將a[v][u] = -[u][v],然後將a[u][v] 修改爲INF，然後第二次尋找最短路*/
       while(s != t)
       {
           a[t][path[t]] = -a[path[t]][t];
           a[path[t]][t] = INF;
           t = path[t];
       }
       Bellman_Ford();
       int res = dist[n];
       if(ans == INF || res == INF)
       {
           printf("Back to jail\n");
            continue;
       }
       ans += res;
       printf("%d\n",ans);
   }
   return 0;
}