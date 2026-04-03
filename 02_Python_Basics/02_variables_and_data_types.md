# Variables & Data Types

## What is a Variable?

A **variable** is a named container that stores a value. Think of it like a labeled box — you put something inside and can retrieve it later by using the label.

```python
name = "Alice"
age = 17
height = 5.6
```

Here, `name`, `age`, and `height` are variables. The `=` sign means "assign this value to this variable" (not "is equal to" the way it means in math).

---

## The Four Core Data Types

### 1. `int` — Integers (whole numbers)
```python
score = 100
year = 2024
temperature = -5
```

### 2. `float` — Floating-point numbers (decimals)
```python
pi = 3.14159
price = 9.99
gpa = 3.7
```

### 3. `str` — Strings (text)
```python
name = "Alice"
greeting = 'Hello!'       # single or double quotes both work
sentence = "I'm learning Python"
```

### 4. `bool` — Booleans (True or False)
```python
is_raining = True
has_passed = False
is_logged_in = True
```

Booleans are used for decisions — you'll use them constantly in control flow.

---

## Checking Types

Use `type()` to see what type a value is:

```python
x = 42
print(type(x))        # <class 'int'>

y = "hello"
print(type(y))        # <class 'str'>

z = 3.14
print(type(z))        # <class 'float'>
```

---

## Type Conversion

You can convert between types:

```python
# String to integer
age_text = "17"
age_number = int(age_text)   # → 17

# Integer to string
score = 95
score_text = str(score)      # → "95"

# Integer to float
x = float(10)                # → 10.0

# Float to integer (truncates — doesn't round)
y = int(3.9)                 # → 3
```

This is important when reading user input — `input()` always returns a *string*, so you need to convert if you want a number:

```python
age = int(input("Enter your age: "))
```

---

## Variable Naming Rules

```python
# ✅ Valid names
my_name = "Alice"
score1 = 100
_private = True
totalStudents = 30

# ❌ Invalid names
1score = 100        # Can't start with a number
my-name = "Alice"   # Hyphens not allowed
class = "Math"      # 'class' is a reserved keyword
```

**Convention**: Python programmers use `snake_case` (words separated by underscores) for variable names.

---

## Multiple Assignment

```python
x, y, z = 1, 2, 3
print(x, y, z)    # 1 2 3

# Swap two variables
a, b = 10, 20
a, b = b, a
print(a, b)       # 20 10
```

---

## 📺 Watch These

1. **Python Variables** — CS Dojo
   👉 [https://www.youtube.com/watch?v=Z1Yd7upQsXY](https://www.youtube.com/watch?v=Z1Yd7upQsXY)

2. **Python Data Types** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=khKv-8q7YmY](https://www.youtube.com/watch?v=khKv-8q7YmY)

---

## Key Takeaways

- Variables store values and are named with `=`
- The four core types: `int`, `float`, `str`, `bool`
- Use `type()` to check what type something is
- `int()`, `str()`, `float()` convert between types
- `input()` always gives back a string — convert it if you need a number

---

*Next up → [Operators](./03_operators.md)*
