#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<string> strGroup(n);
    for (int i = 0; i < n; i++) {
        cin >> strGroup[i];
    }

    unordered_map<string, vector<string>> groups;

    for (string& str : strGroup) {
        array<int, 26> count = {0};

        for (char c : str) {
            count[c - 'a']++;
        }

        string key;
        for (int i = 0; i < 26; i++) {
            key += to_string(count[i]) + "#";
        }

        groups[key].push_back(str);
    }

    for (auto& [key, anagrams] : groups) {
        for (size_t i = 0; i < anagrams.size(); i++) {
            if (i > 0) cout << " ";
            cout << anagrams[i];
        }
        cout << endl;
    }

    return 0;
}
