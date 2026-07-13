#include <iostream>
#include <string>
#include <string_view>
#include <vector>

std::string encode(const std::vector<std::string>& values);
std::vector<std::string> decode(const std::string& encoded);

namespace {

int failures = 0;

void expect_round_trip(const std::vector<std::string>& values, std::string_view name) {
    if (decode(encode(values)) != values) {
        std::cerr << "FAIL: " << name << '\n';
        ++failures;
    }
}

}  // namespace

int main() {
    expect_round_trip({}, "empty list");
    expect_round_trip({""}, "one empty string");
    expect_round_trip({"red", "blue"}, "ordinary strings");
    expect_round_trip({"a:b", "", "x y"}, "separator-like and empty strings");
    expect_round_trip({"same", "same"}, "duplicate strings");
    expect_round_trip({"#12", "0#", "line\nbreak"}, "digits and control characters");

    if (failures == 0) {
        std::cout << "All Encode and Decode Strings tests passed.\n";
    }
    return failures == 0 ? 0 : 1;
}
