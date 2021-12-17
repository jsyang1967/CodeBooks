#include <iostream>
using namespace std;
  
int main() {
    int a, b, c, d;
    while (cin >> a >> b >> c >> d){
        if (b != c){
            cout << "Error\n";
            continue;
        }
        long long A[a][b], B[b][d];
        for (int i = 0; i < a; i++){
            for (int j = 0; j < b; j++){
                cin >> A[i][j];
            }
        }
        for (int i = 0; i < c; i++){
            for (int j = 0; j < d; j++){
                cin >> B[i][j];
            }
        }
        long long C[a][d];
        for (int i = 0; i < a; i++){
            for (int j = 0; j < d; j++){
                C[i][j] = 0;
                for (int k = 0; k < c; k++){
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        for (int i = 0; i < a; i++){
            for (int j = 0; j < d; j++){
                cout << C[i][j] << " ";
            }
            cout << "\n";
        }
    }
    return 0;
}