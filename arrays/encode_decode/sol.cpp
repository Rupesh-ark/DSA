#include <bits/stdc++.h>
using namespace std;
string encode(const vector<string> &strings_to_encode);
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
  cout << "Encoded String: " << temp << endl;
  decoded = decode(temp);
  for (string word : decoded) {
    cout << word << " ";
  }
  return 0;
}

string encode(const vector<string> &strings_to_encode) {
  string encoded_string = "";
  for (auto &str : strings_to_encode) {
    int len = str.length();
    encoded_string = encoded_string + to_string(len) + "#" + str;
  }
  return encoded_string;
}

vector<string> decode(string string_to_decode) {
  // cout << string_to_decode << endl;
  vector<string> decoded_vector;
  size_t i = 0, j = 0;
  int length_of_word;
  while (i < string_to_decode.length()) {
    j = i;
    while (string_to_decode[j] != '#')
      j++;
    length_of_word = stoi(string_to_decode.substr(i, j - i));
    cout << "Length of word: " << length_of_word << endl;
    decoded_vector.push_back(string_to_decode.substr(j + 1, length_of_word));
    i = j + 1 + length_of_word;
  }
  return decoded_vector;
}
