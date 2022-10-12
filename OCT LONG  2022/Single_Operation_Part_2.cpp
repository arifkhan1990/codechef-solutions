#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        string s;
        cin >> s;

        int v = 0, c = 0;
        int mx = INT_MAX;

        for(int i = n-1; i >= 0; i--){
            if (s[i] == '1'){
                v += pow(2,c);
            }
            c++;
        }
        int  y = 0;
        for(int i = 1; i <= n; i++) {
            int p = (v/pow(2,i));
            p = v ^ p;
            if (p < mx) {
                mx = p;
                y = i;
            }
        }
        cout << y << endl;
    }
    return 0;

}