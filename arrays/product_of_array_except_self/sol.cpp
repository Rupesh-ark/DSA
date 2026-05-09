#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n, prefix = 1, postfix = 1;
  cin >> n;
  vector<int> numArray(n);
  vector<int> resArray(n);
  for (int i = 0; i < n; i++) {
    cin >> numArray[i];
  }
  for (int i = 0; i < n; i++) {
    resArray[i] = prefix;
    prefix *= numArray[i];
  }
  for (int i = n - 1; i >= 0; i--) {
    resArray[i] *= postfix;
    postfix *= numArray[i];
  }
  for (auto i : resArray) {
    cout << "i: " << i << endl;
  }
  return 0;
}
