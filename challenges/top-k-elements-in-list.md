# Top K Frequent Elements

**Difficulty:** Medium
**Pattern:** Arrays & Hashing

## Challenge

Given a sequence of integers and a number `k`, return the `k` distinct values
that occur most frequently. Result ordering does not matter.

## Examples

```text
[1, 1, 1, 2, 2, 3], k 2       -> [1, 2]
[4, 4, 5, 5, 5, 6, 6, 6, 6], k 1 -> [6]
[-1, -1, 2, 3, 3], k 2         -> [-1, 3]
[9], k 1                        -> [9]
```

## Warm-up

Before coding, write down your answers:

1. Build the frequency table for the first example by hand.
2. If the input has `n` values, how many distinct values can it contain at most?
3. What is the cost of sorting every distinct value by frequency?
4. Which edge case occurs when `k` equals the number of distinct values?

## Function contract

Implement exactly this function:

```cpp
#include <vector>

std::vector<int> top_k_frequent(const std::vector<int>& values, int k);
```

The provided harness at `tests/neetcode150/top-k-elements-in-list_test.cpp`
supplies `main()` and the core tests. Answer the warm-up before inspecting it.
You may add one extra edge case to the harness after forming your own
expectations.

## Build

Create this standalone C++20 exercise:

```text
exercises/neetcode150/top-k-elements-in-list.cpp
```

Define the function above; do not add `main()`. Make automatically links the
provided order-insensitive test harness.

Use this command as often as needed while working:

```sh
make run EXERCISE=neetcode150/top-k-elements-in-list
```

When the session is over, verify and record it once:

```sh
make finish PROBLEM=top-k-elements-in-list
```

## Optional reference

https://neetcode.io/problems/top-k-elements-in-list
