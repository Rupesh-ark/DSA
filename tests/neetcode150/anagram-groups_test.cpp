#include <algorithm>
#include <iostream>
#include <string>
#include <string_view>
#include <utility>
#include <vector>

std::vector<std::vector<std::string>> group_anagrams(
    const std::vector<std::string>& values
);

namespace {

int failures = 0;

std::vector<std::vector<std::string>> canonicalize(
    std::vector<std::vector<std::string>> groups
) {
    for (auto& group : groups) {
        std::sort(group.begin(), group.end());
    }
    std::sort(groups.begin(), groups.end());
    return groups;
}

void expect_groups(
    const std::vector<std::string>& input,
    std::vector<std::vector<std::string>> expected,
    std::string_view name
) {
    if (canonicalize(group_anagrams(input)) != canonicalize(std::move(expected))) {
        std::cerr << "FAIL: " << name << '\n';
        ++failures;
    }
}

}  // namespace

int main() {
    expect_groups(
        {"eat", "tea", "tan", "ate", "nat", "bat"},
        {{"eat", "tea", "ate"}, {"tan", "nat"}, {"bat"}},
        "multiple groups"
    );
    expect_groups({"abc", "cab", "foo"}, {{"abc", "cab"}, {"foo"}}, "two groups");
    expect_groups({"a"}, {{"a"}}, "single string");
    expect_groups({"", ""}, {{"", ""}}, "duplicate empty strings");
    expect_groups({}, {}, "empty input");

    if (failures == 0) {
        std::cout << "All Group Anagrams tests passed.\n";
    }
    return failures == 0 ? 0 : 1;
}
