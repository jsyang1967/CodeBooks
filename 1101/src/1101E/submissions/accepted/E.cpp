#include <iostream>
using namespace std;
int main()
{
    int y;
    int n, a;

    while (cin >> n)
    {
        a = 0;
        while (n > 0)
        {
            a += n % 10;
            n /= 10;
        }
        cout << a << endl;
    }

    return 0;
}