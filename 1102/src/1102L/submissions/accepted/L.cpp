#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
const int maxn = 1005;
int prime[maxn]; // 0:prime
vector <int> v;
 
int main() {
    int N, C, K, p;
    // 建立質數表
    prime[0] = 1;
    p = 2;
    v.push_back(1);
    while (p <= maxn){
        if (!prime[p]) {
            v.push_back(p);
            for (int i=2*p; i<maxn; i+=p)
                prime[i] = 1;
        }
        p++;
    }
    while (cin >> N >> C){
        auto it = lower_bound(v.begin(), v.end(), N);
        K = (int)(it - v.begin());
        if (*it == N) {
            K++;
        }
        cout << N << ' ' << C << ":";
        for (int i=max(0, K/2 - C + (K % 2)); i<min(K, K/2+C); i++){
            cout << ' ' << v[i];
        }
        cout << '\n';
    }
    return 0;
}