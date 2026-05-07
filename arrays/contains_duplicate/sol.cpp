#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  cin >> n;
  vector<int> nums(n);
  for (int i = 0; i < n; i++)
    cin >> nums[i];

  unordered_set<int> seen;
  for (int x : nums) {
    if (seen.count(x)) {
      cout << "true" << endl;
      return 0;
   }
    seen.insert(x);
  }
  cout << "false" << endl;
  return 0;
}
