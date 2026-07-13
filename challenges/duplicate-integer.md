# Contains Duplicate

**Difficulty:** Easy
**Pattern:** Arrays & Hashing

## Challenge

Given a sequence of integers, determine whether any value occurs more than once.
Return `true` when a duplicate exists and `false` when every value is unique.

## Examples

```text
[4, 9, 4]    -> true
[2, 5, 8]    -> false
[7]          -> false
[-3, 1, -3]  -> true
```

## Warm-up

Before coding, write down your answers:

1. What is the smallest meaningful input?
2. With a brute-force approach, which pairs are compared for `[2, 5, 8]`?
3. If the input size doubles, how does the number of pair comparisons change?
4. Which additional edge cases should your tests cover?

## Function contract

Implement exactly this function:

```cpp
#include <vector>

bool contains_duplicate(const std::vector<int>& values);
```

The provided harness at `tests/neetcode150/duplicate-integer_test.cpp` supplies
`main()` and the core tests. Answer the warm-up before inspecting it. You may add
one extra edge case to the harness after forming your own expectations.

## Build

Create this standalone C++20 exercise:

```text
exercises/neetcode150/duplicate-integer.cpp
```

Define the function above; do not add `main()`. Make automatically links the
provided test harness, whose exit code reports whether every test passed.

Use this command as often as needed while working:

```sh
make run EXERCISE=neetcode150/duplicate-integer
```

When the session is over, verify and record it once:

```sh
make finish PROBLEM=duplicate-integer
```

## Optional reference

https://neetcode.io/problems/duplicate-integer
