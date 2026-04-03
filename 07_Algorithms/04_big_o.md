# Big-O Notation

## The Big Idea

**Big-O notation** describes how the *time* (or *memory*) an algorithm needs grows as the *input size* grows. It lets us compare algorithms independently of hardware or implementation details.

Think of it as asking: "If I double the input size, how much longer does this take?"

---

## Why We Need It

Two algorithms both solve the same problem correctly. But:
- Algorithm A takes 1 second for 1,000 items, 2 seconds for 2,000 items
- Algorithm B takes 1 second for 1,000 items, 1,000 seconds for 2,000 items

Big-O helps us see this difference *before* we run the code.

---

## Common Complexities

### O(1) — Constant Time
The operation takes the same time regardless of input size.

```python
def get_first(lst):
    return lst[0]   # Always 1 step, no matter how big the list
```

Accessing a list by index, or a dict by key = O(1).

---

### O(log n) — Logarithmic Time
Each step halves the problem. Doubling input adds only 1 more step.

```python
# Binary search: eliminates half the search space each time
```

If n = 1,000,000 → only ~20 steps. This is extremely fast!

---

### O(n) — Linear Time
Work grows directly with input size.

```python
def find_max(lst):
    max_val = lst[0]
    for item in lst:   # Must look at every item
        ...
```

Double the input → double the work.

---

### O(n log n) — "n log n" Time
Common for efficient sorting algorithms.

```python
# Merge sort, Python's built-in sort
```

Faster than O(n²) for large n, but slower than O(n).

---

### O(n²) — Quadratic Time
Nested loops over the same data.

```python
def has_duplicate(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):   # Nested loop!
            if i != j and lst[i] == lst[j]:
                return True
    return False
```

Double the input → 4× the work. Slows down fast!

---

### O(2ⁿ) — Exponential Time
Each new input element doubles the work. Extremely slow.

```python
# Naive recursive Fibonacci — recalculates the same values over and over
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)   # 2^n calls for large n
```

---

## Growth Rate Comparison

For n = 1,000:

| Complexity | Operations |
|-----------|-----------|
| O(1) | 1 |
| O(log n) | ~10 |
| O(n) | 1,000 |
| O(n log n) | ~10,000 |
| O(n²) | 1,000,000 |
| O(2ⁿ) | 10^301 (unreachable!) |

---

## How to Calculate Big-O

**Rule 1**: Drop constants
```python
O(2n) → O(n)
O(500) → O(1)
```

**Rule 2**: Drop smaller terms
```python
O(n² + n) → O(n²)    # n² dominates
O(n + log n) → O(n)  # n dominates
```

**Rule 3**: Each loop multiplies
```python
# One loop
for i in range(n):          # O(n)

# Two nested loops
for i in range(n):
    for j in range(n):      # O(n²)

# Loop + binary search inside
for i in range(n):
    binary_search(...)      # O(n log n)
```

---

## Space Complexity

Big-O also applies to **memory usage**:

```python
def double_list(lst):
    return [x * 2 for x in lst]   # Creates new list → O(n) space

def double_in_place(lst):
    for i in range(len(lst)):
        lst[i] *= 2               # Modifies in place → O(1) space
```

---

## 📺 Watch These

1. **Big-O Notation in 100 Seconds** — Fireship
   👉 [https://www.youtube.com/watch?v=g2o22C3CRfU](https://www.youtube.com/watch?v=g2o22C3CRfU)

2. **Big O Notation Full Course** — CS Dojo
   👉 [https://www.youtube.com/watch?v=v4cd1O4zkGw](https://www.youtube.com/watch?v=v4cd1O4zkGw)

3. **Big O Explained Simply** — NeetCode
   👉 [https://www.youtube.com/watch?v=BgLTDT03QtU](https://www.youtube.com/watch?v=BgLTDT03QtU)

---

## Key Takeaways

- Big-O describes how **runtime grows with input size** — it's about scale, not exact time
- O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- Loops are usually O(n); nested loops are usually O(n²)
- Drop constants and smaller terms — only the dominant term matters
- Always think about both **time** and **space** complexity

---

*Next up → [Practice Questions](./questions.md)*
