# G11 Queue Lab — 完成版教学包

**配套文件：** `queue_lab.py`（可运行答案版，已用 Python 3.13 实际运行验证）

---

## 0. 课前 60 秒检查（学生端）

1. 下载 `G11 queue_lab - Finish me, then Turn in.py`（不要直接在浏览器里预览）。
2. 右键文件 → **Open with / Edit with IDLE**。
3. 先按 **Ctrl + S** 保存到自己的文件夹（例如 Desktop\CS）。
4. 按 **F5**，或菜单 **Run → Run Module**。
5. 如果看到下面 5 行，就说明环境正常，可以开始：

```text
PART 1
rice
soup
juice
5
```

6. **如果 IDLE 打不开 / 没有显示：** 打开 <https://trinket.io/python>，把代码粘贴进去，点 Run。输出和提交内容完全一样。
7. 做完后：Ctrl + S 保存 → Classroom → 上传 `.py` 文件 → **Turn in**。

> 常见坑：直接双击 `.py` 会弹出一个黑色窗口，程序跑完立刻关闭，看起来像“没运行”。一定用 IDLE 打开后按 F5。

---

## 1. 每个 TODO 的完整代码（可直接投屏）

### PART 1：先预测，再运行

| 表达式 | 答案 | 讲解点 |
|---|---|---|
| `snacks[0]` | `rice` | 第一个索引是 **0**，不是 1 |
| `snacks[2]` | `soup` | 0=rice, 1=noodles, 2=soup |
| `snacks[-1]` | `juice` | 负数从末尾数，-1 是最后一个 |
| `len(snacks)` | `5` | len 数“有几项”，不是“最大索引” |

---

### TODO 2a：把 `"salad"` 加到末尾

```python
snacks.append("salad")
print(snacks)
```

运行后这一行输出：

```text
['milk', 'rice', 'noodles', 'fruit', 'juice', 'bread', 'salad']
```

---

### TODO 2b：用 for 循环逐行打印

```python
for snack in snacks:
    print(snack)
```

**注意：** `print(snack)` 前面必须是 **4 个空格**，不能顶格，也不能和 `for` 对齐。

---

### TODO 2c：故意触发元组错误，再把 `#` 放回

先临时去掉 `#`：

```python
days[1] = "Sat"
```

按 F5 后会看到（这是**预期**结果，不是学生写错了）：

```text
TypeError: 'tuple' object does not support item assignment
```

然后把 `#` 放回去，让程序恢复可运行：

```python
# days[1] = "Sat"
```

**讲解：** 元组 `( )` 创建后不能修改；列表 `[ ]` 可以修改。`days[1]` 能读，但不能赋值。

---

### TODO 3a：S01、S02、S03 加入队列

```python
queue.append("S01")
queue.append("S02")
queue.append("S03")
```

此时：

```python
print("Waiting:", queue)
```

输出：

```text
Waiting: ['S01', 'S02', 'S03']
```

---

### TODO 3b：S04 迟到，加到队尾

```python
queue.append("S04")
```

现在队列是 `['S01', 'S02', 'S03', 'S04']`，但**不要再打印 Waiting**，否则会和预期输出不一致。

---

### TODO 3c：服务队首（S01）

```python
served = queue.pop(0)
print("Served:", served)
```

输出：

```text
Served: S01
```

**讲解：** `pop()` 默认删最后一个（像栈）；`pop(0)` 删第一个（像排队）。队列是 FIFO：先来先服务。

---

### TODO 3d：还有几个人在等

```python
print("Still waiting:", len(queue))
```

输出：

```text
Still waiting: 3
```

**讲解：** 原来 4 人，S01 被服务后剩 3 人。注意这里有两个不同的“3”：3a 之后打印的是 **3 个等待者**；3d 打印的是 **服务后剩 3 人**，数字一样但含义不同。

---

### TODO 3e：S03 还在队列里吗

```python
print("S03" in queue)
```

输出：

```text
True
```

**讲解：** `in` 返回布尔值 `True` / `False`。S03 还没被服务，所以是 True。

---

### 退出条（Exit Ticket）参考答案

```python
# 1. snacks[-1] gives the LAST item.
# 2. I used a TUPLE for MENU because the menu is fixed and must never change.
# 3. I used a LIST for queue because people join and leave, so it must change.
```

中文意思：

1. `snacks[-1]` 给出**最后一个**元素。
2. MENU 用元组，因为菜单是**固定的**，程序运行中不应该被修改。
3. queue 用列表，因为队列**会变化**：有人加入、有人被服务离开。

---

## 2. 最终程序的全部预期输出（已实际验证）

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

**逐行对照：**

| 行 | 来自 | 说明 |
|---|---|---|
| `PART 1` | Part 1 | 标题 |
| `rice` / `soup` / `juice` / `5` | Part 1 四个 print | 预测答案 |
| `['milk', ... 'bread']` | Part 2 引导代码 | insert 到队首、remove soup、append bread |
| `['milk', ... 'salad']` | TODO 2a | append salad |
| `milk` … `salad`（7 行） | TODO 2b | for 循环逐行打印 |
| `Tue` | `days[1]` | 元组可以读 |
| `Waiting: ['S01', 'S02', 'S03']` | TODO 3a 后 | 此时 S04 还没来 |
| `Served: S01` | TODO 3c | pop(0) |
| `Still waiting: 3` | TODO 3d | 4 - 1 = 3 |
| `True` | TODO 3e | S03 仍在队列中 |

---

## 3. 7 个最常见错误 + 快速修复

| # | 屏幕上的报错（IDLE） | 真正原因 | 10 秒修复 | 本实验位置 |
|---|---|---|---|---|
| 1 | `IndentationError: expected an indented block` / `unexpected indent` | `for` 下面那行没有缩进，或空格数量不一致 | 选中 `print(snack)`，按一次 **Tab**（=4 空格）；全文只用空格，不要混用 Tab | TODO 2b |
| 2 | `NameError: name 'snacks' is not defined` | 变量名拼错、大小写不对，或还没定义就使用 | 检查拼写 `snacks`；Python 区分大小写，`Snacks` ≠ `snacks` | Part 1 / 2 |
| 3 | `SyntaxError: expected ':'` | `for` / `if` 行末漏了冒号 | 在 `for snack in snacks` 末尾加 `:` | TODO 2b |
| 4 | `IndexError: list index out of range` | 索引超过最后一项。5 项的最大索引是 **4**，不是 5 | 用 `snacks[-1]` 或 `snacks[len(snacks)-1]` | Part 1 |
| 5 | `ValueError: list.remove(x): x not in list` | `remove()` 的值不在列表里：拼错，或已经被删过一次 | 先 `print(snacks)` 看列表，再删一个确实存在的值 | Part 2 |
| 6 | `TypeError: 'tuple' object does not support item assignment` | 试图修改元组：`days[1] = "Sat"` | **这是故意触发的**；把 `#` 放回去。要能修改就用列表 | TODO 2c |
| 7 | 没有报错，但黑窗口一闪而过 / 看不到输出 | 双击运行 `.py`，程序结束窗口就关闭 | 用 IDLE 打开后按 F5；或在文件最后加 `input("Press Enter to close...")` | 运行方式 |

**附加提醒（第 6 条的亲戚）：** 如果写 `MENU.append("pizza")`，会得到 `AttributeError: 'tuple' object has no attribute 'append'`。MENU 是元组，不能 append；要加东西请加到 `queue` 这个列表。

---

## 4. 扩展任务（给提前完成的学生）

> 用法：把代码加在实验文件**最后**（Part 3 之后），按 F5；或在 IDLE Shell 里逐行输入。变量 `snacks`、`queue`、`MENU` 已经在内存里。

### 扩展 1：菜单查询（`input` + `in`）— 约 5 分钟

```python
choice = input("What do you want? ")
if choice in MENU:
    print(choice, "is on the menu.")
else:
    print(choice, "is NOT on the menu.")
```

测试：输入 `rice` → `rice is on the menu.`；输入 `pizza` → `pizza is NOT on the menu.`

**教学点：** `in` 对列表和元组都能用；`input()` 拿到的是字符串。

---

### 扩展 2：再服务两个人（循环 + `pop(0)`）— 约 5 分钟

```python
for i in range(2):
    print("Served:", queue.pop(0))
print("Still waiting:", len(queue))
print(queue)
```

预期输出：

```text
Served: S02
Served: S03
Still waiting: 1
['S04']
```

**教学点：** 每 `pop` 一次列表就少一项；`range(2)` 让循环执行两次。

---

### 扩展 3：转圈——把队首移到队尾（一行代码）— 约 3 分钟

```python
queue.append(queue.pop(0))
print(queue)
```

预期输出：

```text
['S03', 'S04', 'S02']
```

**教学点：** `pop(0)` 会**返回**被删掉的值，`append` 正好把它接到末尾。这就是“轮转队列”。

---

### 扩展 4：切片、排序、计数 — 约 5 分钟

```python
print(snacks[1:4])
print(sorted(snacks))
print(snacks.count("rice"))
```

预期输出：

```text
['rice', 'noodles', 'fruit']
['bread', 'fruit', 'juice', 'milk', 'noodles', 'rice', 'salad']
1
```

**教学点：** 切片 `[1:4]` **含头不含尾**（索引 1、2、3）；`sorted()` 返回新列表，不改变原列表；`count()` 数某个值出现几次。

---

### 扩展 5：随机午餐 + 元组转列表 — 约 5–8 分钟

```python
import random

menu_list = list(MENU)
random.shuffle(menu_list)
print("Today's order:", menu_list)
print("Today's pick:", random.choice(MENU))
```

示例输出（每次不同）：

```text
Today's order: ['soup', 'rice', 'noodles']
Today's pick: rice
```

**教学点：** 元组本身不能改，但 `list(MENU)` 可以复制成列表再打乱；`random.choice()` 可以直接从元组里取一项。

---

### 扩展 6（挑战）：S03 前面还有几个人？— 约 3 分钟

```python
print(queue.index("S03"))
```

预期输出（主程序运行完后）：

```text
1
```

**教学点：** `index()` 返回值所在的位置，从 0 开始数。S02 在 0，S03 在 1。

---

## 5. 收作业检查清单

- [ ] PART 1 的 4 个预测已写在纸上/注释里：rice、soup、juice、5
- [ ] TODO 2a：`snacks.append("salad")` + `print(snacks)`
- [ ] TODO 2b：for 循环已取消注释，`print` 缩进 4 空格
- [ ] TODO 2c：见过 `TypeError`，并且已把 `#` 放回
- [ ] TODO 3a：S01、S02、S03 依次 `append`
- [ ] TODO 3b：S04 `append` 到队尾
- [ ] TODO 3c：`queue.pop(0)`，输出 `Served: S01`
- [ ] TODO 3d：`len(queue)`，输出 `Still waiting: 3`
- [ ] TODO 3e：`print("S03" in queue)`，输出 `True`
- [ ] 退出条 3 题已用英文/中文填写
- [ ] Ctrl + S 保存，文件名为 `G11 queue_lab - Finish me, then Turn in.py`
- [ ] Classroom 上传 → **Turn in**
