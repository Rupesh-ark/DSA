#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int k,n;
    cin >> k;
    cin >> n;
    vector<int> nums(n);
    vector<int> sol(k);
    cout << "Size: " << n << endl;
    cout << "K: " << k << endl;
    unordered_map<int, int> count_hash;
    unordered_map<int, vector<int>> frequency;
    for(int i = 0; i < n ; i++) cin >> nums[i];
    for(int i = 0; i < n ; i++) cout << nums[i] << " ";
    cout<<endl;
    for(int i = 0; i < n ; i++) {
        count_hash[nums[i]]++;
    }
    for(auto& [c,count] : count_hash){
       frequency[count].push_back(c);
    }

   for(auto& [c,values] : frequency){
        for(auto& val: values){
            sol.push_back(val);
            if(int(sol.size()) == k)
                break;
        }
   }

   for(auto& val : sol){
    cout << val << " ";
   }

    return 0;
}
