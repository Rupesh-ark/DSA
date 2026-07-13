# NeetCode 150 Learning Project

This repository turns the NeetCode 150 into a focused daily C++ practice system.
It chooses the next problem, schedules reviews, and tracks consistency without
hiding progress in an external service.

## Requirements

- A C++ compiler with C++20 support
- GNU Make
- Python 3.11 or newer (standard library only)

## Start a session

See today's new problem and due reviews:

```sh
make today
```

After the focused session, record the result interactively:

```sh
make log
```

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

1. Run `make today` and open the suggested problem.
2. Work through examples and a straightforward approach before coding.
3. Use the stuck ladder in `ROADMAP.md` instead of immediately viewing a solution.
4. Test the implementation and explain its time and space complexity.
5. Run `make log`, then commit the solution and progress record.

The first three Arrays & Hashing problems are also a diagnostic. They reveal
whether extra C++ or Big-O practice is useful without delaying progress through
the NeetCode 150.

See `ROADMAP.md` for the 90-minute routine, XP rules, review schedule, learning
levels, and coaching agreement.
