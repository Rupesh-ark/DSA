#include <algorithm>
#include <iostream>
#include <string_view>
#include <vector>

std::vector<int> top_k_frequent(const std::vector<int>& values, int k);

namespace {

int failures = 0;

void expect_values(
    const std::vector<int>& input,
    int k,
    std::vector<int> expected,
    std::string_view name
) {
    std::vector<int> actual = top_k_frequent(input, k);
    std::sort(actual.begin(), actual.end());
    std::sort(expected.begin(), expected.end());
    if (actual != expected) {
        std::cerr << "FAIL: " << name << '\n';
        ++failures;
    }
}

}  // namespace

int main() {
    expect_values({1, 1, 1, 2, 2, 3}, 2, {1, 2}, "two most frequent");
    expect_values({4, 4, 5, 5, 5, 6, 6, 6, 6}, 1, {6}, "single result");
    expect_values({-1, -1, 2, 3, 3}, 2, {-1, 3}, "negative value");
    expect_values({9}, 1, {9}, "single value");
    expect_values({1, 2, 2, 3, 3, 3}, 3, {1, 2, 3}, "all distinct values requested");

    if (failures == 0) {
        std::cout << "All Top K Frequent Elements tests passed.\n";
    }
    return failures == 0 ? 0 : 1;
}
