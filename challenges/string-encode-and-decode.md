# Encode and Decode Strings

**Difficulty:** Medium
**Pattern:** Arrays & Hashing

## Challenge

Design one operation that converts a list of strings into a single string and a
second operation that reconstructs the exact original list. Strings may be empty
or contain characters that might otherwise be used as separators.

## Examples

```text
["red", "blue"]       -> encode -> decode -> ["red", "blue"]
["a:b", "", "x y"]   -> encode -> decode -> ["a:b", "", "x y"]
[]                    -> encode -> decode -> []
["same", "same"]      -> encode -> decode -> ["same", "same"]
```

## Warm-up

Before coding, write down your answers:

1. Why can a separator character by itself be ambiguous?
2. What information would let the decoder find each string boundary exactly?
3. What invariant must remain true after every encode/decode round trip?
4. Which tests cover empty strings, separator characters, and duplicate strings?

## Function contract

Implement exactly these functions:

```cpp
#include <string>
#include <vector>

std::string encode(const std::vector<std::string>& values);
std::vector<std::string> decode(const std::string& encoded);
```

The provided harness at
`tests/neetcode150/string-encode-and-decode_test.cpp` supplies `main()` and the
core round-trip tests. Answer the warm-up before inspecting it. You may add one
extra edge case to the harness after forming your own expectations.

## Build

Create this standalone C++20 exercise:

```text
exercises/neetcode150/string-encode-and-decode.cpp
```

Define both functions above; do not add `main()`. Make automatically links the
provided round-trip test harness.

Use this command as often as needed while working:

```sh
make run EXERCISE=neetcode150/string-encode-and-decode
```

When the session is over, verify and record it once:

```sh
make finish PROBLEM=string-encode-and-decode
```

## Optional reference

https://neetcode.io/problems/string-encode-and-decode
