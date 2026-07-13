#include <iostream>
#include <string_view>
#include <vector>

std::vector<int> two_sum(const std::vector<int>& values, int target);

namespace {

int failures = 0;

void expect_pair(
    const std::vector<int>& values,
    int target,
    const std::vector<int>& result,
    std::string_view name
) {
    bool valid = result.size() == 2;
    if (valid) {
        const int left = result[0];
        const int right = result[1];
        valid = left >= 0 && right >= 0 && left != right
            && static_cast<std::size_t>(left) < values.size()
            && static_cast<std::size_t>(right) < values.size();
        if (valid) {
            valid = values[left] + values[right] == target;
        }
    }

    if (!valid) {
        std::cerr << "FAIL: " << name << '\n';
        ++failures;
    }
}

}  // namespace

int main() {
    expect_pair({3, 8, 4}, 12, two_sum({3, 8, 4}, 12), "pair near the end");
    expect_pair({5, 1, 7}, 6, two_sum({5, 1, 7}, 6), "pair near the start");
    expect_pair({-2, 9, 3}, 7, two_sum({-2, 9, 3}, 7), "negative value");
    expect_pair({4, 4}, 8, two_sum({4, 4}, 8), "equal values at distinct indices");
    expect_pair({0, 6, 2}, 6, two_sum({0, 6, 2}, 6), "zero value");

    if (failures == 0) {
        std::cout << "All Two Sum tests passed.\n";
    }
    return failures == 0 ? 0 : 1;
}
