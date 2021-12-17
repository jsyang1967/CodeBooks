#include <iostream>
#include <bitset>
using namespace std;
/* clang++-7 -pthread -std=c++17 -o main1 CSES1745.cpp */
int n, a;
bitset <100005> bs;
  
int main() {
    cin >> n;
    bs.reset();
    bs.set(0, 1);
    for (int i = 0; i < n; i++){
        cin >> a;
        bs |= bs << a;
    }
    cout << bs.count()-1 << "\n";
    for (int i = 1; i < 100005; i++){
        if (bs[i]) cout << i << " ";
    }
} 