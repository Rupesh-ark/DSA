# NeetCode 150 Learning Project

This repository turns the NeetCode 150 into a focused daily C++ practice system.
It chooses the next problem, schedules reviews, and tracks consistency without
hiding progress in an external service.

## Requirements

- A C++ compiler with C++20 support
- GNU Make
- Python 3.11 or newer (standard library only)

## Start a session

See today's local challenge, warm-up, source path, and due reviews:

```sh
make today
```

Use `make run` repeatedly while implementing. At the end of the session, verify
the local tests and record the result together:

```sh
make run EXERCISE=neetcode150/duplicate-integer
make finish PROBLEM=duplicate-integer
```

`make finish` gets the test result from the executable. It asks only about help,
complexity, focused time, and your takeaway. Use `make log` as a manual fallback
for a session that has no local C++ exercise.

Check overall progress:

```sh
make stats
```

The progress log is stored in `data/progress.json`. Commit it with completed
exercise code to build a visible history of consistent practice.

## Work with C++ exercises

List existing exercises, or build and run one by its path below `exercises/`
without the `.cpp` extension:

```sh
make list
make build EXERCISE=arrays/reverse_array
make run EXERCISE=arrays/reverse_array
```

Verify the tracker and every completed exercise:

```sh
make check
```

See every available command with `make help`. Generated programs live in
`build/` and can be removed with `make clean`.

## Daily workflow

1. Run `make today` and read the local challenge card.
2. Work through examples and a straightforward approach before coding.
3. Use the stuck ladder in `ROADMAP.md` instead of immediately viewing a solution.
4. Use `make run` while coding and explain the final time and space complexity.
5. Run `make finish` once, then commit the solution and progress record.

The next challenge unlocks only after the current exercise passes locally and is
reported as independently solved. A failing or helped solution remains the main
quest for the next focused session.

The first three Arrays & Hashing problems are also a diagnostic. They reveal
whether extra C++ or Big-O practice is useful without delaying progress through
the NeetCode 150.

See `ROADMAP.md` for the 90-minute routine, XP rules, review schedule, learning
levels, and coaching agreement.
