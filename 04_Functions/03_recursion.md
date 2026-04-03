# Recursion

## The Big Idea

**Recursion** is when a function calls *itself*. It's a powerful technique for solving problems that can be broken down into smaller versions of the same problem.

It can feel mind-bending at first. That's normal — take your time here.

---

## A Simple Example: Countdown

```python
def countdown(n):
    if n <= 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)   # Function calls itself with a smaller input

countdown(5)
```
Output:
```
5
4
3
2
1
Go!
```

Every recursive function has two essential parts:
1. **Base case** — the stopping condition (when `n <= 0` here)
2. **Recursive case** — the function calling itself with a *smaller* input

---

## The Two Rules of Recursion

> **Rule 1**: Every recursive function must have a base case.
> Without it, the function calls itself forever → `RecursionError: maximum recursion depth exceeded`

> **Rule 2**: Each recursive call must move *closer* to the base case.
> If it doesn't, you'll never reach the base case.

---

## Classic Example: Factorial

The **factorial** of a number `n` (written `n!`) is:
- `5! = 5 × 4 × 3 × 2 × 1 = 120`
- `n! = n × (n-1)!` ← this is naturally recursive!

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))   # 120
print(factorial(0))   # 1
```

Let's trace through `factorial(4)`:
```
factorial(4)
  = 4 * factorial(3)
  = 4 * 3 * factorial(2)
  = 4 * 3 * 2 * factorial(1)
  = 4 * 3 * 2 * 1
  = 24
```

---

## Classic Example: Fibonacci

The Fibonacci sequence: `1, 1, 2, 3, 5, 8, 13, 21, ...`
Each number is the sum of the two before it.

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")
# 0 1 1 2 3 5 8 13
```

⚠️ This recursive Fibonacci is elegant but *slow* for large `n` — it recalculates the same values many times. We'll fix this with **memoization** in Module 7.

---

## Recursion vs Iteration

Most recursive functions can also be written with a loop:

```python
# Recursive
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

Both produce the same result. Use whichever makes the problem *clearer*. Some problems (like traversing trees or folder structures) are naturally recursive.

---

## Visualizing the Call Stack

When a function calls itself, each call gets added to a **call stack**:

```
factorial(4)          ← on top
  calls factorial(3)
    calls factorial(2)
      calls factorial(1)  ← returns 1
    returns 2 * 1 = 2
  returns 3 * 2 = 6
returns 4 * 6 = 24
```

Each level waits for the one below to return before it can finish.

---

## 📺 Watch These

1. **What is Recursion?** — CS50 Harvard (excellent explanation)
   👉 [https://www.youtube.com/watch?v=mz6tAJMVmfM](https://www.youtube.com/watch?v=mz6tAJMVmfM)

2. **Recursion in Python** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=ngCos392W4w](https://www.youtube.com/watch?v=ngCos392W4w)

3. **5 Simple Steps to Solve Any Recursive Problem** — Reducible
   👉 [https://www.youtube.com/watch?v=ngCos392W4w](https://www.youtube.com/watch?v=ngCos392W4w)

---

## Key Takeaways

- Recursion = a function that calls itself
- Must have a **base case** (stops recursion) and **recursive case** (gets closer to base)
- Great for problems with a naturally recursive structure (trees, fractals, mathematical sequences)
- Every recursive solution can be rewritten iteratively (and vice versa)
- Watch out for infinite recursion — always verify your base case

---

*Next up → [Practice Questions](./questions.md)*
