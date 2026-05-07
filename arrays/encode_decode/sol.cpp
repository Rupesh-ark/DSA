#include <bits/stdc++.h>
using namespace std;
string encode(const vector<string>& strings_to_encode);
vector<string> decode(string string_to_decode);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    vector<string> strGroup, decoded;
    string temp;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        strGroup.push_back(temp);
    }
    temp = encode(strGroup);
    decoded = decode(temp);
    return 0;
}

string encode(const vector<string>& strings_to_encode){
    string encoded_string = "";
    for (auto& str : strings_to_encode){
        int len = str.length();
        encoded_string = encoded_string + to_string(len) + "#" + str;
    }
    return encoded_string;
}

vector<string> decode(string string_to_decode){

    cout << string_to_decode << endl;

    return {""};
}
