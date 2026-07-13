#include <iostream>
#include <string>
#include <string_view>

bool is_anagram(const std::string& left, const std::string& right);

namespace {

int failures = 0;

void expect(bool condition, std::string_view name) {
    if (!condition) {
        std::cerr << "FAIL: " << name << '\n';
        ++failures;
    }
}

}  // namespace

int main() {
    expect(is_anagram("", ""), "empty strings");
    expect(is_anagram("x", "x"), "identical single character");
    expect(is_anagram("listen", "silent"), "reordered characters");
    expect(is_anagram("anagram", "nagaram"), "repeated characters");
    expect(!is_anagram("aab", "abb"), "different character counts");
    expect(!is_anagram("rat", "car"), "different characters");
    expect(!is_anagram("ab", "a"), "different lengths");
    expect(!is_anagram("a", "A"), "comparison is case-sensitive");

    if (failures == 0) {
        std::cout << "All Valid Anagram tests passed.\n";
    }
    return failures == 0 ? 0 : 1;
}
