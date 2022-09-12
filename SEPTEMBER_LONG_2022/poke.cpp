//partially solve this solution 
#include<bits/stdc++.h>
using namespace std;

vector<int> sortV(vector<pair<int,int>> N) {
    vector<pair<int,int>> a=N;
    sort(a.begin(), a.end());
    vector<int> p;
    for(int i = 0; i< N.size(); i++){
        p[i] = a[i].second;
    }
    return p;
}

vector<int> intersection(vector<int> v1, vector<int> v2){
    vector<int> v3;

    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    set_intersection(v1.begin(),v1.end(),
                          v2.begin(),v2.end(),
                          back_inserter(v3));
    return v3;
}

int findPos(vector<int>a, int l, int h, int v) {
    while(l < h) {
        int m = (l+h)/2;
        if(a[m] <  v) {
            l = m + 1;
        }else if(a[m] > v) {
            h = m-1;
        }else{
            return m;
        }
    }
    return -1;
}

int main() {
    int T, n, x;
    cin >> T;
    while(T--) {
        cin >> n;
        vector<pair<int, int> > g,w;
        vector<int>ans(n, 0);
        vector<int>gS, wS, sWs;

        for(int i = 0,x;i<n ;i++) {
            cin >> x;
            g.push_back( make_pair(x,i) );
        }
        for(int i = 0,x;i<n ;i++) {
            cin >> x;
            w.push_back( make_pair(x,i) );
        }

        gS = sortV(g);
        wS = sortV(w);
        sWs = sortV(w);
        sort(sWs.begin(), sWs.end());
        for(int i = 0; i< n; i++) {
            ans[gS[i]] += i;
            // int wl = find(wS.begin(), wS.end(), gS[i]) - wS.begin();
            int wl = findPos(wS, 0, wS.size()-1, gS[i]);
            vector<int>::const_iterator first = wS.begin();
            vector<int>::const_iterator last = wS.begin() + wl;
            vector<int>w1;
            w1.assign(first, last);

            vector<int>::const_iterator f = gS.begin()+i;
            vector<int>::const_iterator l = gS.end();
            vector<int>g1;
            g1.assign(f, l);
            
            auto v3 = intersection(w1, g1);
             ans[gS[i]] += w1.size() - v3.size();
        }

        int maximum = *max_element(ans.begin(), ans.end());
        int qualify = count(ans.begin(), ans.end(), maximum);

        cout << qualify << endl;
    }
   return 0;
}
