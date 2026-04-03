# Scope & Return Values

## What is Scope?

**Scope** determines where in your program a variable can be accessed. Python has two main scopes:

- **Local scope** — variables defined *inside* a function
- **Global scope** — variables defined *outside* all functions

```python
x = 10  # Global variable

def my_function():
    y = 20  # Local variable
    print(x)  # ✅ Can access global variables
    print(y)  # ✅ Can access local variables

my_function()
print(x)  # ✅ Works — x is global
print(y)  # ❌ NameError! y only exists inside my_function
```

---

## Why Local Variables are Destroyed

When a function finishes running, all its local variables are **deleted from memory**. This is by design — it prevents functions from accidentally interfering with each other.

```python
def count():
    total = 0
    for i in range(5):
        total += i
    return total

result = count()
print(result)   # 10
# total no longer exists here
```

---

## The `global` Keyword

If you really need to modify a global variable inside a function, use `global`:

```python
count = 0

def increment():
    global count
    count += 1

increment()
increment()
print(count)   # 2
```

⚠️ Use `global` sparingly — it makes code harder to reason about. It's usually better to pass values in as parameters and return the modified value.

---

## Multiple Return Values

Python can return multiple values at once using tuples:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([5, 2, 8, 1, 9])
print(lo, hi)   # 1 9
```

---

## Returning Early

`return` exits a function immediately — useful for short-circuiting logic:

```python
def is_positive(n):
    if n <= 0:
        return False   # Exits here if n <= 0
    return True

def safe_divide(a, b):
    if b == 0:
        return None    # Guard clause
    return a / b
```

This pattern (checking for invalid cases early and returning) is called a **guard clause** and keeps code clean.

---

## Functions Are Objects

In Python, functions are **first-class objects** — you can assign them to variables, pass them as arguments, and return them from other functions:

```python
def say_hello():
    print("Hello!")

# Assign function to a variable
greet = say_hello
greet()   # → Hello!

# Pass a function as an argument
def run_twice(func):
    func()
    func()

run_twice(say_hello)   # → Hello! Hello!
```

This might seem abstract now, but it becomes very powerful later (especially with `map()`, `filter()`, and decorators).

---

## Lambda Functions (Anonymous Functions)

A **lambda** is a small, one-line function — useful for simple operations:

```python
# Normal function
def square(x):
    return x * x

# Lambda equivalent
square = lambda x: x * x

print(square(5))   # 25

# Often used inline
numbers = [1, 5, 2, 8, 3]
numbers.sort(key=lambda x: -x)   # Sort in descending order
print(numbers)   # [8, 5, 3, 2, 1]
```

---

## 📺 Watch These

1. **Python Variable Scope** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=QVdf0LgmICw](https://www.youtube.com/watch?v=QVdf0LgmICw)

2. **Python Lambda Functions** — Tech With Tim
   👉 [https://www.youtube.com/watch?v=KR22jigJLok](https://www.youtube.com/watch?v=KR22jigJLok)

---

## Key Takeaways

- Local variables exist only inside their function; global variables are accessible everywhere
- Use `return` to send values back — functions can return multiple values at once
- Prefer passing values in/out over using `global`
- Functions are objects in Python — they can be passed around like any value
- Lambdas are compact, inline functions — useful for quick operations

---

*Next up → [Recursion](./03_recursion.md)*
