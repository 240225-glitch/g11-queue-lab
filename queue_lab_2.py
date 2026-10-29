# Queue Lab 2: Test, Critique, Refine
# G11 Computer Science - Canteen Queue
# COMPLETE VERSION (teacher answer key)
# How to run: python queue_lab_2.py
#
# The queue is now inside functions. The original worksheet had three bugs:
#   Bug A: serve() crashed on an empty queue.
#   Bug B: join() allowed the same student to join twice.
#   Bug C: position() returned a zero-based index instead of a 1-based place.

MENU = ("rice", "noodles", "soup", "juice")   # tuple: the menu never changes


def join(queue, student):
    """Add a student to the END of the queue. A student can only be in the queue once."""
    if student not in queue:
        queue.append(student)
    return queue


def serve(queue):
    """Remove and return the FIRST student. If the queue is empty, return None."""
    if not queue:
        return None
    return queue.pop(0)


def position(queue, student):
    """Return the student's place in the line: 1 = first. Return 0 if not in the queue."""
    if student in queue:
        return queue.index(student) + 1
    return 0


def order(item):
    """Return 'OK' if the item is on the menu, otherwise 'Not on menu'."""
    if isinstance(item, str) and item.strip().lower() in MENU:
        return "OK"
    return "Not on menu"


# ---------------------------------------------------------------
# TEST TOOL - do not change
passed = 0
failed = 0


def check(name, actual, expected):
    global passed, failed
    if actual == expected:
        passed = passed + 1
        print("PASS", name)
    else:
        failed = failed + 1
        print("FAIL", name, "| expected:", expected, "| got:", actual)


def safe_serve(queue):
    # runs serve() but catches a crash, so the other tests still run
    try:
        return serve(queue)
    except Exception as error:
        return "CRASH: " + type(error).__name__


# ---------------------------------------------------------------
# PART 1 - Run the tests. Read every FAIL.
print("PART 1")
q = []
join(q, "S01")
join(q, "S02")
join(q, "S03")
check("1 normal: join three", q, ["S01", "S02", "S03"])
check("2 normal: serve first", safe_serve(q), "S01")
check("3 normal: position of S03", position(q, "S03"), 2)
check("4 boundary: serve empty queue", safe_serve([]), None)
join(q, "S02")
check("5 unexpected: join twice", q, ["S02", "S03"])
check("6 normal: menu item", order("soup"), "OK")
check("7 unexpected: not on menu", order("pizza"), "Not on menu")

# ---------------------------------------------------------------
# PART 2 - The three bugs are fixed in the functions above.
#   Bug A: serve([]) returned a crash; it now returns None.
#   Bug B: join() now ignores a student who is already in the queue.
#   Bug C: position() now adds 1, so the first student is at position 1.

# ---------------------------------------------------------------
# PART 3 - Three student-written tests.
print("PART 3")
q2 = ["S10", "S11"]
check("8 boundary: position of the first student", position(q2, "S10"), 1)
check("9 unexpected: position of someone not in line", position(q2, "S99"), 0)
check("10 my test: serve the only student", safe_serve(["S12"]), "S12")

# ---------------------------------------------------------------
# PART 4 - Peer critique.
# Partner: one thing that works well: ____________________________
# Partner: one thing to improve:      ____________________________

# ---------------------------------------------------------------
# PART 5 - Refine: order() now ignores capitalization and extra spaces.
# What I changed and why:
# I changed order() to use item.strip().lower(). Students may type "Soup"
# or " soup ", and both should be accepted as the same menu item.
check("11 refine: order ignores case and spaces", order(" Soup "), "OK")

# ---------------------------------------------------------------
# EXIT TICKET - answer in the comments (keep the #)
# 1. A boundary test checks an edge case such as an empty queue, the first
#    item, or the last item because bugs often appear at the limits.
# 2. The bug that was hardest to find was the duplicate-join bug. The test
#    that showed it was test 5 ("join twice").
# 3. My partner's feedback changed my code by making order() accept different
#    capitalization and extra spaces.

print()
print("Passed:", passed, " Failed:", failed)
