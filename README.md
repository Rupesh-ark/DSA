# DSA Practice

C++17 problem-solving workspace with a Makefile-driven workflow.

## Create a New Problem

```bash
make new P=arrays/two_sum
```

This creates a self-contained problem folder:

```
arrays/
└── two_sum/
    ├── sol.cpp        # solution (copied from template)
    ├── input.txt      # test input
    └── output.txt     # expected output
```

Edit `input.txt` with your test case and `output.txt` with the expected result.

## Run a Solution

```bash
make run P=arrays/two_sum
```

If `input.txt` exists, it is automatically fed as stdin. Otherwise runs interactively.

## Test Against Expected Output

```bash
make test P=arrays/two_sum
```

Runs the solution with `input.txt` and diffs actual output against `output.txt`. Prints **PASSED** or **FAILED** with a diff.

## Run with Debug Mode

Compiles with AddressSanitizer and UndefinedBehaviorSanitizer to catch memory bugs and undefined behavior. Also auto-uses `input.txt` if present.

```bash
make debug P=arrays/two_sum
```

## Topics

| Directory | Topics Covered |
|---|---|
| `arrays/` | Prefix sums, Kadane's, merge intervals |
| `strings/` | Pattern matching, anagrams, palindromes |
| `linked_lists/` | Reversal, cycle detection, merge |
| `stacks_queues/` | Monotonic stack, BFS, min stack |
| `trees/` | BST, traversals, LCA |
| `graphs/` | BFS, DFS, Dijkstra, topological sort |
| `heaps/` | Top-K, median finding, merge K lists |
| `hashing/` | Frequency maps, two sum variants |
| `sorting/` | Quick sort, merge sort, custom comparators |
| `searching/` | Binary search and variants |
| `backtracking/` | Permutations, subsets, N-queens |
| `dynamic_programming/` | Knapsack, LIS, grid paths |
| `greedy/` | Activity selection, Huffman |
| `bit_manipulation/` | XOR tricks, power of 2, bitmasks |
| `sliding_window/` | Fixed/variable window problems |
| `two_pointers/` | Sorted array pairs, container with water |
| `tries/` | Prefix search, word dictionaries |
