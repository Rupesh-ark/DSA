#include <iostream>
#include <string_view>
#include <vector>

bool contains_duplicate(const std::vector<int>& values);

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
    expect(!contains_duplicate({}), "empty input has no duplicate");
    expect(!contains_duplicate({7}), "single value has no duplicate");
    expect(!contains_duplicate({2, 5, 8}), "distinct values");
    expect(contains_duplicate({4, 9, 4}), "duplicate values");
    expect(contains_duplicate({-3, 1, -3}), "negative duplicate");
    expect(contains_duplicate({1, 2, 3, 4, 2}), "non-adjacent duplicate");

    if (failures == 0) {
        std::cout << "All Contains Duplicate tests passed.\n";
    }
    return failures == 0 ? 0 : 1;
}
