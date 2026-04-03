# Defining Functions

## The Big Idea

**Functions** are reusable blocks of code that do a specific job. Instead of copy-pasting the same code over and over, you write it once as a function and call it whenever you need it.

Think of a function like a microwave: you put something in (input), press a button (call the function), and get a result out (output).

---

## Defining and Calling a Function

```python
# Define the function
def greet():
    print("Hello, world!")

# Call the function
greet()   # → Hello, world!
greet()   # → Hello, world!  (call it as many times as you want)
```

Key parts:
- `def` — keyword that starts a function definition
- `greet` — the function's name
- `()` — parentheses (for parameters — more on that next)
- `:` — colon to start the function body
- Indented block — the function's body (what it does)

---

## Functions with Parameters

**Parameters** are variables that let you pass data into a function:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # → Hello, Alice!
greet("Bob")     # → Hello, Bob!
```

You can have multiple parameters:

```python
def add(a, b):
    print(a + b)

add(3, 5)    # → 8
add(10, 20)  # → 30
```

---

## The `return` Statement

A function can **return** a value back to whoever called it:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # → 8

# You can use the return value directly
print(add(10, 20) * 2)  # → 60
```

Without `return`, the function returns `None`:

```python
def no_return():
    x = 5  # Does something but returns nothing

result = no_return()
print(result)   # → None
```

---

## Default Parameter Values

You can give parameters a default value:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # → Hello, Alice!
greet("Bob", "Hey")         # → Hey, Bob!
greet("Carol", "Howdy")     # → Howdy, Carol!
```

Default parameters must come **after** non-default ones.

---

## Why Functions Matter

Without functions:
```python
# Messy, repetitive code
area1 = 5 * 3
print(f"Area: {area1}")

area2 = 7 * 4
print(f"Area: {area2}")

area3 = 10 * 2
print(f"Area: {area3}")
```

With functions:
```python
def print_area(width, height):
    area = width * height
    print(f"Area: {area}")

print_area(5, 3)
print_area(7, 4)
print_area(10, 2)
```

The function version is shorter, clearer, and if you need to change the logic, you only change it **once**.

---

## 📺 Watch These

1. **Python Functions** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=9Os0o3wzS_I](https://www.youtube.com/watch?v=9Os0o3wzS_I)

2. **Python Functions for Beginners** — CS Dojo
   👉 [https://www.youtube.com/watch?v=NSbOtYzIQI0](https://www.youtube.com/watch?v=NSbOtYzIQI0)

---

## Key Takeaways

- `def name(params):` defines a function; calling `name(args)` runs it
- Parameters let you pass data in; `return` sends data back out
- Default parameters make arguments optional
- Functions make code **reusable**, **readable**, and easier to **test**

---

*Next up → [Parameters, Return Values & Scope](./02_scope_and_return.md)*
