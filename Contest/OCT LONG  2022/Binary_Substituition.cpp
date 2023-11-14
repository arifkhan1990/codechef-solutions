#include <bits/stdc++.h>
using namespace std;
#define lln long long int

lln cp(int idx, string& s, vector<int>& res, map<string, string>& code, string curr, set<string>& cS)
{
    if (idx < 0){
        auto it = cS.find(curr);
        if (it == cS.end()){
            cS.insert(curr);
            return 1;
        }
        return 0;
    }

    if(res[idx] != -1) return res[idx];
    lln one = cp(idx - 1, s,res, code, code[s.substr(idx,1)+curr], cS);
    lln two = 0;
    if(idx-1 >= 0 and code.find(s.substr(idx-1, 2)) != code.end()){
        two = cp(idx-2, s,res,code, code[s.substr(idx-1, 2)]+curr, cS);
    }
    return res[idx] = (one+two) % 998244353;
}

int main()
{
    int t;
    cin >> t;
    while(t--) {
        string s;
        cin >> s;
        lln n = s.length();
        vector<int> res(n, -1);
        map<string, string> code{{"a","01"},{"b","10"},{"ab","010"},{"ba","101"}};
        set<string> cS;
        cout << cp(n-1, s, res, code, "", cS)<< endl;
    }
    return 0;
}