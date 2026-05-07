#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n,target, diff;
    cin>>n;
    vector<int> nums(n);
    unordered_map<int, int> hash;
    for (int i = 0; i < n; i++) cin >> nums[i];
    cin>>target;

    for(int i = 0; i < n; i++){
        diff = target - nums[i];
        if(hash.count(diff)){
            cout << "i: " << i << ", j: " << hash[diff]<< endl;
            break;
        }
        hash[nums[i]] = i;
    }
  

    return 0;
}
