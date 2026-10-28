# Queue Lab: Lists and Ordered Collections
# G11 Computer Science, Unit 3, Mr. Ermanno
# How to run: Run > Run Module (or press F5). Save first with Ctrl + S.
# RUNNABLE VERSION (all TODOs completed; teacher answer key)

# ===== PART 1: What is a list? (read, predict, run) =====
# A list keeps items IN ORDER. Each item has an index. The first index is 0.
snacks = ["rice", "noodles", "soup", "fruit", "juice"]

print("PART 1")
print(snacks[0])        # rice   (first item, index 0)
print(snacks[2])        # soup   (third item: 0, 1, 2)
print(snacks[-1])       # juice  (-1 means the LAST item)
print(len(snacks))      # 5      (how many items)

# ===== PART 2: Change a list (guided) =====
print()
print("PART 2")
snacks.append("bread")          # add to the END
snacks.insert(0, "milk")        # add at index 0 (the FRONT)
snacks.remove("soup")           # remove by value
print(snacks)

# TODO 2a: append "salad" to the end of snacks, then print snacks
snacks.append("salad")
print(snacks)

# TODO 2b: print every snack on its own line with a for loop
for snack in snacks:
    print(snack)

# A TUPLE is also ordered, but it can NOT change. Use ( ) not [ ].
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(days[1])                  # Tue

# TODO 2c: remove the # on the next line, run, read the error, then put the # back
# days[1] = "Sat"
# Expected error: TypeError: 'tuple' object does not support item assignment
# A tuple is immutable (cannot be changed), so we must put the # back.

# ===== PART 3: Canteen queue (build it) =====
print()
print("PART 3")
MENU = ("rice", "noodles", "soup")   # fixed choices: a tuple
queue = []                           # people waiting: a list

# TODO 3a: 3 students join the queue. Use append to add "S01", "S02", "S03".
queue.append("S01")
queue.append("S02")
queue.append("S03")

print("Waiting:", queue)             # Waiting: ['S01', 'S02', 'S03']

# TODO 3b: S04 is late. Add "S04" to the END of the queue.
queue.append("S04")

# TODO 3c: Serve the first person. pop(0) removes index 0 and gives it back.
served = queue.pop(0)
print("Served:", served)             # Served: S01

# TODO 3d: Print how many people are still waiting (use len).
print("Still waiting:", len(queue))  # Still waiting: 3

# TODO 3e: Is "S03" still in the queue? print("S03" in queue)
print("S03" in queue)                # True

# ===== EXIT TICKET: answer in the comments =====
# 1. snacks[-1] gives the LAST item.
# 2. I used a TUPLE for MENU because the menu is fixed and must never change.
# 3. I used a LIST for queue because people join and leave, so it must change.
