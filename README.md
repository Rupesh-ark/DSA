# DSA Learning Project

This repository is a place to practise data structures and algorithms in C++20.
Each exercise is a small, standalone program so that the algorithm, tests, and
complexity analysis stay together while the project is young.

## Requirements

- A C++ compiler with C++20 support
- GNU Make

## Commands

See all project commands:

```sh
make help
```

List the available exercises:

```sh
make list
```

Build or run an exercise by its path below `exercises/`, without the `.cpp`
extension:

```sh
make build EXERCISE=arrays/reverse_array
make run EXERCISE=arrays/reverse_array
```

Remove generated programs:

```sh
make clean
```

## Suggested workflow

1. Restate the problem and work through a small example by hand.
2. Write a straightforward solution before trying to optimise it.
3. Add normal and edge-case tests.
4. Record the time and space complexity.
5. Explain why an improved solution is correct.

## Learning roadmap

1. Arrays and strings
2. Linked lists
3. Stacks and queues
4. Hash tables
5. Recursion and backtracking
6. Trees and heaps
7. Graphs
8. Sorting and searching
9. Dynamic programming
