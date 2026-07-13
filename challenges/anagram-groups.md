# Group Anagrams

**Difficulty:** Medium
**Pattern:** Arrays & Hashing

## Challenge

Given a list of strings, collect strings into groups when they contain the same
characters with the same occurrence counts. The order of groups and strings
inside each group does not matter.

## Examples

```text
["eat", "tea", "tan", "ate", "nat", "bat"]
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

["abc", "cab", "foo"]
-> [["abc", "cab"], ["foo"]]

["a"]
-> [["a"]]
```

## Warm-up

Before coding, write down your answers:

1. What fact makes two strings belong to the same group?
2. How much pairwise comparison work is needed for `n` strings?
3. What stable description could identify a whole anagram group?
4. Which cases test repeated letters, single strings, and duplicate strings?

## Function contract

Implement exactly this function:

```cpp
#include <string>
#include <vector>

std::vector<std::vector<std::string>> group_anagrams(
    const std::vector<std::string>& values
);
```

The provided harness at `tests/neetcode150/anagram-groups_test.cpp` supplies
`main()` and the core tests. Answer the warm-up before inspecting it. You may add
one extra edge case to the harness after forming your own expectations.

## Build

Create this standalone C++20 exercise:

```text
exercises/neetcode150/anagram-groups.cpp
```

Define the function above; do not add `main()`. Make automatically links the
provided order-insensitive test harness.

Use this command as often as needed while working:

```sh
make run EXERCISE=neetcode150/anagram-groups
```

When the session is over, verify and record it once:

```sh
make finish PROBLEM=anagram-groups
```

## Optional reference

https://neetcode.io/problems/anagram-groups
