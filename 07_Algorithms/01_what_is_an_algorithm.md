# What is an Algorithm?

## The Big Idea

An **algorithm** is a precise, step-by-step procedure for solving a problem. Every program you've written so far contains algorithms — you just haven't called them that.

The study of algorithms is about asking: "Given a problem, what's the *best* way to solve it?"

---

## Properties of a Good Algorithm

1. **Correctness** — It produces the right answer for all valid inputs
2. **Efficiency** — It uses time and memory wisely
3. **Clarity** — It can be understood and maintained
4. **Finiteness** — It always terminates (doesn't run forever)

---

## A Simple Example: Finding the Maximum

**Problem**: Given a list of numbers, find the largest one.

**Algorithm**:
1. Assume the first number is the maximum
2. Look at each remaining number
3. If it's larger than the current maximum, update the maximum
4. After all numbers are checked, return the maximum

```python
def find_max(numbers):
    if not numbers:
        return None

    max_val = numbers[0]        # Step 1: assume first is max
    for num in numbers[1:]:     # Step 2: check each remaining
        if num > max_val:       # Step 3: update if larger
            max_val = num
    return max_val              # Step 4: return result

print(find_max([3, 7, 1, 9, 4]))   # 9
```

This is a simple but complete algorithm.

---

## Why Efficiency Matters

Imagine you need to find a name in a phone book with 1 million entries.

**Option A — Linear search**: Check every name from the start until you find it.
- Worst case: 1,000,000 checks

**Option B — Binary search**: Open to the middle, eliminate half the book, repeat.
- Worst case: ~20 checks (log₂(1,000,000) ≈ 20)

Same correct result. One takes *50,000× less work*.

When your data is large, choosing the right algorithm is the most powerful optimization you can make.

---

## Algorithm Design Strategies

CS researchers have identified a few key approaches:

| Strategy | Description | Example |
|----------|-------------|---------|
| **Brute Force** | Try all possibilities | Trying every key on a lock |
| **Divide and Conquer** | Split problem, solve parts, combine | Binary search, merge sort |
| **Greedy** | Always take the locally best choice | Making change with minimum coins |
| **Dynamic Programming** | Cache subproblem solutions | Fibonacci with memoization |
| **Backtracking** | Try, fail, undo, try again | Solving a maze or Sudoku |

---

## 📺 Watch These

1. **What is an Algorithm?** — TED-Ed
   👉 [https://www.youtube.com/watch?v=6hfOvs8pY1k](https://www.youtube.com/watch?v=6hfOvs8pY1k)

2. **Introduction to Algorithms** — MIT OpenCourseWare
   👉 [https://www.youtube.com/watch?v=HtSuA80QTyo](https://www.youtube.com/watch?v=HtSuA80QTyo)

---

## Key Takeaways

- An algorithm is a precise sequence of steps to solve a problem
- Good algorithms are **correct**, **efficient**, and **clear**
- The right algorithm can make a task 50,000× faster — it matters
- Key strategies: brute force, divide and conquer, greedy, dynamic programming

---

*Next up → [Searching Algorithms](./02_searching.md)*
