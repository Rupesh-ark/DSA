#include <cassert>
#include <iostream>
#include <vector>

void reverse_array(std::vector<int>& values) {
    for (std::size_t left = 0, right = values.size(); left < right; ++left) {
        --right;
        if (left >= right) {
            break;
        }

        const int temporary = values[left];
        values[left] = values[right];
        values[right] = temporary;
    }
}

int main() {
    std::vector<int> values{1, 2, 3, 4, 5};
    reverse_array(values);
    assert((values == std::vector<int>{5, 4, 3, 2, 1}));

    std::vector<int> empty;
    reverse_array(empty);
    assert(empty.empty());

    std::vector<int> single_value{42};
    reverse_array(single_value);
    assert((single_value == std::vector<int>{42}));

    std::cout << "All reverse_array tests passed.\n";
}
