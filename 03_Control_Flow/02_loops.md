# Loops

## The Big Idea

Computers are great at **repetition**. If you need to do something 1,000 times, you don't write 1,000 lines of code — you write a **loop**. Python has two kinds: `for` loops and `while` loops.

---

## `for` Loops

A `for` loop repeats code **for each item in a sequence**:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
cherry
```

The variable `fruit` takes each value from the list, one at a time.

---

## Looping with `range()`

`range()` generates a sequence of numbers — perfect for when you want to loop a specific number of times:

```python
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4  (starts at 0 by default!)

for i in range(1, 6):
    print(i)
# 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)
# 0, 2, 4, 6, 8  (step of 2)
```

`range(start, stop, step)` — `stop` is **not included**.

---

## Looping Over Strings

Strings are sequences too, so you can loop over them character by character:

```python
word = "Hello"

for char in word:
    print(char)
# H, e, l, l, o
```

---

## `while` Loops

A `while` loop repeats **as long as a condition is True**:

```python
count = 0

while count < 5:
    print(count)
    count += 1
# 0, 1, 2, 3, 4
```

⚠️ Be careful: if the condition never becomes `False`, you get an **infinite loop** — the program runs forever! Always make sure the loop variable changes each iteration.

---

## When to Use `for` vs `while`

| Situation | Use |
|-----------|-----|
| You know how many times to loop | `for` with `range()` |
| Looping over a list or string | `for` |
| You loop until something happens | `while` |
| Waiting for user input | `while` |

---

## `break` and `continue`

### `break` — Exit the loop immediately
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Prints 0, 1, 2, 3, 4 — stops when i is 5
```

### `continue` — Skip to the next iteration
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Prints 1, 3, 5, 7, 9 — skips even numbers
```

---

## Nested Loops

Loops inside loops — useful for grids, tables, and combinations:

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()  # New line after each row
```
Output:
```
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
```

---

## `enumerate()` — Loop with Index

When you need both the index and the value:

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
```

---

## A Classic Example: Multiplication Table

```python
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")
```

---

## 📺 Watch These

1. **Python For Loops** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=6iF8Xb7Z3wQ](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ)

2. **Python While Loops** — Tech With Tim
   👉 [https://www.youtube.com/watch?v=D0Nb2Fs3Q8c](https://www.youtube.com/watch?v=D0Nb2Fs3Q8c)

---

## Key Takeaways

- `for` loops iterate over a sequence (list, string, `range`)
- `while` loops run until a condition is `False`
- `break` exits a loop; `continue` skips to the next iteration
- `range(start, stop, step)` generates number sequences
- `enumerate()` gives you both the index and value while looping

---

*Next up → [Nested Logic & Combining Control Flow](./03_nested_logic.md)*
