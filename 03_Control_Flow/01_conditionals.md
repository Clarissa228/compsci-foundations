# Conditionals (If / Elif / Else)

## The Big Idea

Programs need to make **decisions**. Should we show an error or proceed? Is the user old enough? Did the player win or lose? **Conditionals** let your code branch into different paths based on whether something is `True` or `False`.

---

## The `if` Statement

```python
age = 18

if age >= 18:
    print("You can vote!")
```

The code inside the `if` block **only runs if the condition is `True`**. Notice the **colon** (`:`) and the **indentation** (4 spaces or 1 tab) — these are required in Python.

---

## `if` / `else`

```python
temperature = 15

if temperature > 25:
    print("It's warm outside!")
else:
    print("Bring a jacket.")
```

The `else` block runs when the condition is `False`.

---

## `if` / `elif` / `else`

Use `elif` ("else if") to check multiple conditions:

```python
score = 78

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

Python checks conditions **top to bottom** and stops at the first one that's `True`.

---

## Nested Conditionals

You can put `if` statements inside other `if` statements:

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Welcome to the concert!")
    else:
        print("You need a ticket.")
else:
    print("You must be 18 or older.")
```

However, be careful with too much nesting — it gets hard to read. Often you can simplify with `and`/`or`.

---

## Combining Conditions

```python
age = 20
has_ticket = True

# Same as the nested example above — cleaner!
if age >= 18 and has_ticket:
    print("Welcome to the concert!")
elif age < 18:
    print("You must be 18 or older.")
else:
    print("You need a ticket.")
```

---

## Truthy and Falsy Values

In Python, things that aren't technically `True` or `False` can still be used in conditions:

```python
# These are "falsy" — treated as False in conditions
0
""           # empty string
[]           # empty list
None

# These are "truthy" — treated as True
1  (or any non-zero number)
"hello"      # non-empty string
[1, 2, 3]    # non-empty list
```

Example:
```python
name = ""

if name:
    print(f"Hello, {name}!")
else:
    print("No name provided.")   # This runs — empty string is falsy
```

---

## The Ternary Operator (One-liner if/else)

For simple assignments, Python has a shorthand:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult
```

---

## 📺 Watch These

1. **Python If Statements** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=DZwmZ8Usvnk](https://www.youtube.com/watch?v=DZwmZ8Usvnk)

2. **Python Conditionals** — CS Dojo
   👉 [https://www.youtube.com/watch?v=f4KOjWS_KZs](https://www.youtube.com/watch?v=f4KOjWS_KZs)

---

## Key Takeaways

- `if` / `elif` / `else` controls which code paths run
- Python uses **indentation** (not curly braces) to define code blocks
- `elif` lets you check multiple conditions in sequence
- Combine conditions with `and`, `or`, `not`
- Empty values (`""`, `0`, `[]`, `None`) are **falsy**

---

*Next up → [Loops](./02_loops.md)*
