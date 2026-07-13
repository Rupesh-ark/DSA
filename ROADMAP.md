# NeetCode 150 Roadmap

## Goal and pace

The target is all 150 problems with enough delayed review to recall the patterns
without assistance. Six new problems each week gives a realistic 25-to-28-week
campaign, with Sundays reserved for consolidation.

The local catalogue is a metadata snapshot of the official NeetCode 150 taken on
2026-07-13. It contains titles and links, not copied problem statements or
solutions.

## The 90-minute loop

Monday through Saturday:

1. 20 minutes for due reviews.
2. 55 minutes for one new problem.
3. 15 minutes for complexity, one takeaway, and the progress log.

Sunday:

1. 60 minutes for reviews and weak patterns.
2. 20 minutes for a boss fight: explain or reimplement an older problem.
3. 10 minutes to record takeaways and prepare for the next week.

A difficult day can use a 15-minute minimum session. Missing a day ends the
displayed streak but never removes XP or completed work.

## Stuck ladder

Do not spend the whole session staring at an empty editor:

1. At 15 minutes, construct another example by hand.
2. At 30 minutes, ask for one conceptual hint.
3. At 45 minutes, study the explanation or solution.
4. Close the solution and implement the idea from memory.

Using help is recorded honestly and carries no penalty. The review system will
bring the problem back until it can be solved independently.

Use `make run EXERCISE=...` as often as needed while coding. Run
`make finish PROBLEM=...` once when ending the session; it compiles and runs the
exercise before recording the result.

## Progress states and reviews

A problem moves through these useful states:

```text
Unseen -> Attempted -> Solved with help -> Solved independently -> Mastered
```

After the first independent solution, the tracker schedules:

1. A recall review after 1 day.
2. An implementation review after 7 days.
3. A full independent solution after 21 days.

Four independent successes in total mark the problem as mastered. An attempted
or assisted review returns the problem the following day without resetting prior
successes.

The next catalogue problem unlocks only when the current problem both passes its
local tests and is completed without a hint or solution. Compilation failures,
test failures, and helped solutions remain the main quest. Explaining complexity
earns XP but does not control unlocking.

## XP

XP rewards the learning process rather than difficulty:

| Action | XP |
| --- | ---: |
| First logged activity of the day | 10 |
| Honest attempt | 20 |
| Tests pass | 20 |
| Time and space complexity explained | 10 |
| Scheduled review solved independently | 20 |

XP is derived from the append-only session history in `data/progress.json`.

## Campaign levels

| Level | Patterns | Problems |
| --- | --- | ---: |
| 1: Foundations | Arrays, two pointers, sliding window, stack, binary search, linked lists | 44 |
| 2: Recursive structures | Trees, heaps, backtracking, tries | 35 |
| 3: Graph explorer | Graphs and advanced graphs | 19 |
| 4: DP campaign | 1-D and 2-D dynamic programming | 23 |
| 5: Final stretch | Greedy, intervals, math, geometry, bit manipulation | 29 |

Each completed category should end with an unfamiliar or deliberately forgotten
problem attempted under interview conditions.

## Coaching agreement

When working together:

- You attempt the problem before receiving a complete solution.
- I give progressive hints and explain why a pattern applies.
- We review correctness, edge cases, C++ choices, and complexity.
- Your implementation remains yours; I do not silently replace it.
- We finish with one concise takeaway and the next review date.
