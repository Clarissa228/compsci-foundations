# Operators

## The Big Idea

**Operators** are symbols that perform operations on values. You already know most of them from math — Python just adds a few extras.

---

## Arithmetic Operators

```python
a = 10
b = 3

print(a + b)    # 13  — addition
print(a - b)    # 7   — subtraction
print(a * b)    # 30  — multiplication
print(a / b)    # 3.333... — division (always returns float)
print(a // b)   # 3   — floor division (rounds DOWN, returns int)
print(a % b)    # 1   — modulo (remainder after division)
print(a ** b)   # 1000 — exponentiation (a to the power of b)
```

### The Modulo Operator `%`
Modulo is extremely useful — it gives you the **remainder** after division:

```python
10 % 3 = 1    (10 = 3 × 3 + 1)
15 % 5 = 0    (15 is evenly divisible by 5)
7 % 2 = 1     (7 is odd — odd numbers have remainder 1 when divided by 2)
```

Classic use: checking if a number is even or odd:
```python
number = 8
print(number % 2 == 0)  # True → number is even
```

---

## Comparison Operators

These return a **boolean** (`True` or `False`):

```python
x = 10
y = 20

print(x == y)   # False — equal to
print(x != y)   # True  — not equal to
print(x < y)    # True  — less than
print(x > y)    # False — greater than
print(x <= 10)  # True  — less than or equal to
print(x >= 10)  # True  — greater than or equal to
```

> ⚠️ Common mistake: `=` assigns a value. `==` compares two values. They are completely different!

---

## Logical Operators

Used to combine boolean expressions:

```python
age = 17
has_id = True

# and — both must be True
print(age >= 18 and has_id)   # False (age is not >= 18)

# or — at least one must be True
print(age >= 16 or has_id)    # True (has_id is True)

# not — flips True/False
print(not has_id)             # False
```

---

## Assignment Operators (Shortcuts)

Instead of writing `x = x + 5`, you can write `x += 5`:

```python
score = 100

score += 10     # score = score + 10  → 110
score -= 5      # score = score - 5   → 105
score *= 2      # score = score * 2   → 210
score //= 3     # score = score // 3  → 70
score **= 2     # score = score ** 2  → 4900
```

---

## String Operators

Strings support some arithmetic-style operators:

```python
first = "Hello"
second = " World"

# Concatenation (joining strings)
print(first + second)     # "Hello World"

# Repetition
print("ha" * 3)           # "hahaha"

# String formatting (f-strings) — the modern way
name = "Alice"
age = 17
print(f"My name is {name} and I am {age} years old.")
# → "My name is Alice and I am 17 years old."
```

**F-strings** are your best friend — memorize this syntax!

---

## Order of Operations (PEMDAS)

Python follows standard math order:

1. `**` (exponents)
2. `*`, `/`, `//`, `%` (multiplication/division)
3. `+`, `-` (addition/subtraction)

```python
print(2 + 3 * 4)      # 14  (not 20!)
print((2 + 3) * 4)    # 20  (parentheses first)
```

When in doubt, use parentheses to be explicit.

---

## 📺 Watch These

1. **Python Operators** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=v5MR5JnKcZI](https://www.youtube.com/watch?v=v5MR5JnKcZI)

2. **Python f-strings** — Tech With Tim
   👉 [https://www.youtube.com/watch?v=nghuHvKLhJA](https://www.youtube.com/watch?v=nghuHvKLhJA)

---

## Key Takeaways

- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=` — return `True`/`False`
- Logical: `and`, `or`, `not`
- `=` assigns, `==` compares — don't mix them up!
- **f-strings** (`f"Hello {name}"`) are the cleanest way to build strings

---

*Next up → [Input & Output](./04_input_output.md)*
