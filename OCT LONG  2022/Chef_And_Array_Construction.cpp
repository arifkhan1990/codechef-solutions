#include <bits/stdc++.h>
using namespace std;
#define lln long long int
#define mod 998244353

lln subSetAndSum(lln n, vector<lln> arr, lln Len, lln L){
    lln sm = arr[n % Len];
    n = (int)n/Len;
    for(lln i = 1; i < L; i++){
        sm = (sm & arr[n % Len]);
        n = (int)n/Len;
    }
    return sm%mod;
}

lln permutation(vector<lln> arr, lln Len, lln L){
    lln ar = 0;
    for(lln i = 0; i < pow(Len, L); i++) {
        ar += subSetAndSum(i, arr, Len, L);
    }
    return ar%mod;
}

int main()
{
    lln t;
    cin >> t;
    while(t--) {
        lln n , m;
        cin >> n >> m;
        vector<lln> v;
        for(lln i=1; i<=m ; i++){
            v.push_back(i);
        }
        cout << permutation(v, m,n) << endl;
    }
    return 0;
}