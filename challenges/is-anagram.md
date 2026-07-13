# Valid Anagram

**Difficulty:** Easy
**Pattern:** Arrays & Hashing

## Challenge

Given two strings, determine whether they contain exactly the same characters
with the same number of occurrences. Character order may differ.

## Examples

```text
"listen", "silent"  -> true
"rat", "car"        -> false
"aab", "abb"        -> false
"x", "x"            -> true
```

## Warm-up

Before coding, write down your answers:

1. What can you conclude immediately when the string lengths differ?
2. What character inventory does each side of `"aab"` have?
3. If you repeatedly search the second string for each character in the first,
   how does the work grow as the strings get longer?
4. Which tests expose mistakes involving repeated characters?

## Function contract

Implement exactly this function:

```cpp
#include <string>

bool is_anagram(const std::string& left, const std::string& right);
```

The provided harness at `tests/neetcode150/is-anagram_test.cpp` supplies `main()`
and the core tests. Answer the warm-up before inspecting it. You may add one extra
edge case to the harness after forming your own expectations.

## Build

Create this standalone C++20 exercise:

```text
exercises/neetcode150/is-anagram.cpp
```

Define the function above; do not add `main()`. Make automatically links the
provided test harness, whose exit code reports whether every test passed.

Use this command as often as needed while working:

```sh
make run EXERCISE=neetcode150/is-anagram
```

When the session is over, verify and record it once:

```sh
make finish PROBLEM=is-anagram
```

## Optional reference

https://neetcode.io/problems/is-anagram
