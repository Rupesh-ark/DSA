#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s, t;
    unordered_map<char, int> sig;
    cin>>s;
    cin>>t;
    if (s.length() != t.length()){
        cout<< "false" << endl;
        return 0;
    }

    for (char c : s) sig[c]++;
       
    for( auto ch : sig){
        cout << ch.first << ": " << ch.second << endl;
    }
    for (char c : t) sig[c]--;

    for(auto& [c,count] : sig){
        if(count != 0){
            cout<<"false" << endl;
            return 0;
        }
    }
    cout<<"true" << endl;
    return 0;

}
