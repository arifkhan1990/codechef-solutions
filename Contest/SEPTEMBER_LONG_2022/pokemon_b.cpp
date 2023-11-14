#include<bits/stdc++.h>
using namespace std;

vector<int> sortR(vector<int> GW, int n) {
    vector<int> s=GW;
    sort(s.begin(), s.end());
    for(int i = 0; i <n; i++){
        GW[i] = lower_bound(s.begin(), s.end(), GW[i]) - s.begin();
    }
    return GW;
}


int main() {
    int T, n, x;
    cin >> T;
    while(T--) {
        int ans = 0, pos = 0;
        cin >> n;
        vector<int> g,w;
        vector<int>q(n), r(n), s(n), p;

        for(int i = 0,x;i<n ;i++) {
            cin >> x;
            g.push_back(x);
        }
        for(int i = 0,x;i<n ;i++) {
            cin >> x;
            w.push_back(x);
        }
        g = sortR(g, n);
        w = sortR(w, n);

        for(int i = 0; i < n; i++) {
            q[g[i]] = w[i];
            s[i] = g[i] + w[i];
            r[w[i]] = i;
        }

        for(int i = 0; i<n; i++){
            p.insert(upper_bound(p.begin(),p.end(), q[i]), q[i]);
            s[r[q[i]]] -= lower_bound(p.begin(),p.end(),q[i]) - p.begin();
        }
        for(int x:s){
            pos = max(pos,x);
        }
        for(int x:s){
            ans += (x==pos);
        }
        cout << ans << endl;
    }
    return 0;
}
