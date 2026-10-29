# G11 Queue Labs — Lists, Functions & Testing

Two complete, runnable answer keys for the G11 Computer Science canteen queue labs (Unit 3).

**Lab 1** covers list indexing, `append`, `insert`, `remove`, `for` loops, tuples vs. lists, and a FIFO queue built with `pop(0)`.

**Lab 2** puts the queue inside functions (`join`, `serve`, `position`, `order`) and uses a `check()` test harness to find and fix three bugs.

## Lab 1 — Lists & Ordered Collections

Requires Python 3.8+ (verified with Python 3.13). No third-party packages.

```bash
python queue_lab.py
```

The exact output is saved in [`expected_output.txt`](expected_output.txt).

## Files

| File | Description |
|---|---|
| `queue_lab.py` | Lab 1 complete program — all TODOs filled, exit ticket answered |
| `expected_output.txt` | Lab 1 exact output produced by `queue_lab.py` |
| `queue_lab_2.py` | Lab 2 complete program — three bugs fixed, student tests and refinement included |
| `expected_output_lab2.txt` | Lab 2 exact output produced by `queue_lab_2.py` |
| `TEACHER_GUIDE.md` | Teaching guide for Lab 1 (Chinese): per-TODO code, full output, 7 common errors, extension tasks, submission checklist |

## Lab 1 expected output

```text
PART 1
rice
soup
juice
5

PART 2
['milk', 'rice', 'noodles', 'fruit', 'juice', 'bread']
['milk', 'rice', 'noodles', 'fruit', 'juice', 'bread', 'salad']
milk
rice
noodles
fruit
juice
bread
salad
Tue

PART 3
Waiting: ['S01', 'S02', 'S03']
Served: S01
Still waiting: 3
True
```

## Lab 2 — Test, Critique, Refine

```bash
python queue_lab_2.py
```

The three intentional bugs are fixed:

- `serve([])` returns `None` instead of raising `IndexError`.
- `join()` ignores a student who is already in the queue.
- `position()` returns a 1-based place (`1` = first).

The answer key also includes three student-written tests and one refinement: `order()` now ignores capitalization and extra spaces, so `"Soup"` and `" soup "` both return `"OK"`.

## Lab 2 expected output

```text
PART 1
PASS 1 normal: join three
PASS 2 normal: serve first
PASS 3 normal: position of S03
PASS 4 boundary: serve empty queue
PASS 5 unexpected: join twice
PASS 6 normal: menu item
PASS 7 unexpected: not on menu
PART 3
PASS 8 boundary: position of the first student
PASS 9 unexpected: position of someone not in line
PASS 10 my test: serve the only student
PASS 11 refine: order ignores case and spaces

Passed: 11  Failed: 0
```

## Teaching notes

- `snacks[0]` is `rice`: the first index is **0**, not 1.
- `MENU` is a tuple because the menu is fixed; `queue` is a list because people join and leave.
- `queue.pop(0)` serves the first person (FIFO). `pop()` without an index would serve the last person (LIFO).
- The line `# days[1] = "Sat"` is intentionally commented out. Uncomment it, run, and students will see `TypeError: 'tuple' object does not support item assignment`; then comment it again.
- `print("Waiting:", queue)` runs after S01–S03 join but before S04 arrives, so it prints 3 people. The later `Still waiting: 3` is after S01 has been served — same number, different meaning.
- In Lab 2, tests 3, 4, and 5 expose bugs C, A, and B respectively.
- Lab 2 test 10 checks `serve()` with a single student, and test 11 checks the `order()` refinement.

## Run in class

Open `queue_lab.py` or `queue_lab_2.py` in IDLE and press **F5** (`Run > Run Module`). If IDLE is unavailable, paste the code into <https://trinket.io/python> and press **Run**.

> `TEACHER_GUIDE.md` is written in Chinese. The Python code and all program output are in English, matching the lab handout.
