# G11 Queue Lab — Lists & Ordered Collections

A complete, runnable answer key for the G11 Computer Science queue lab (Unit 3). It covers list indexing, `append`, `insert`, `remove`, `for` loops, tuples vs. lists, and a FIFO queue built with `pop(0)`.

## Run it

Requires Python 3.8+ (verified with Python 3.13). No third-party packages.

```bash
python queue_lab.py
```

The exact output is saved in [`expected_output.txt`](expected_output.txt).

## Files

| File | Description |
|---|---|
| `queue_lab.py` | Complete runnable program — all TODOs filled, exit ticket answered |
| `expected_output.txt` | Exact output produced by `queue_lab.py` |
| `TEACHER_GUIDE.md` | Teaching guide (Chinese): per-TODO code, full output, 7 common errors, extension tasks, submission checklist |

## Expected output

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

## Teaching notes

- `snacks[0]` is `rice`: the first index is **0**, not 1.
- `MENU` is a tuple because the menu is fixed; `queue` is a list because people join and leave.
- `queue.pop(0)` serves the first person (FIFO). `pop()` without an index would serve the last person (LIFO).
- The line `# days[1] = "Sat"` is intentionally commented out. Uncomment it, run, and students will see `TypeError: 'tuple' object does not support item assignment`; then comment it again.
- `print("Waiting:", queue)` runs after S01–S03 join but before S04 arrives, so it prints 3 people. The later `Still waiting: 3` is after S01 has been served — same number, different meaning.

## Run in class

Open `queue_lab.py` in IDLE and press **F5** (`Run > Run Module`). If IDLE is unavailable, paste the code into <https://trinket.io/python> and press **Run**.

> `TEACHER_GUIDE.md` is written in Chinese. The Python code and all program output are in English, matching the lab handout.
