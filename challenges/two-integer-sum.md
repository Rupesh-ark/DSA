# Two Sum

**Difficulty:** Easy
**Pattern:** Arrays & Hashing

## Challenge

Given a sequence of integers and a target, return the indices of two distinct
elements whose values add to the target. Assume one valid pair exists.

## Examples

```text
[3, 8, 4], target 12   -> [1, 2]
[5, 1, 7], target 6    -> [0, 1]
[-2, 9, 3], target 7   -> [0, 1]
[4, 4], target 8       -> [0, 1]
```

## Warm-up

Before coding, write down your answers:

1. Which index pairs would brute force inspect for three elements?
2. Why must the two indices be distinct even when their values are equal?
3. After reading a value `x`, which companion value would complete the target?
4. If the input doubles, how does checking every pair affect the amount of work?

## Function contract

Implement exactly this function:

```cpp
#include <vector>

std::vector<int> two_sum(const std::vector<int>& values, int target);
```

The provided harness at `tests/neetcode150/two-integer-sum_test.cpp` supplies
`main()` and the core tests. Answer the warm-up before inspecting it. You may add
one extra edge case to the harness after forming your own expectations.

## Build

Create this standalone C++20 exercise:

```text
exercises/neetcode150/two-integer-sum.cpp
```

Define the function above; do not add `main()`. Make automatically links the
provided test harness, whose exit code reports whether every test passed.

Use this command as often as needed while working:

```sh
make run EXERCISE=neetcode150/two-integer-sum
```

When the session is over, verify and record it once:

```sh
make finish PROBLEM=two-integer-sum
```

## Optional reference

https://neetcode.io/problems/two-integer-sum
