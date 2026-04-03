# Input & Output

## The Big Idea

Programs are useful because they can communicate: they take **input** from the user and produce **output**. In Python, this is simpler than you'd think.

---

## Output with `print()`

`print()` displays values to the screen:

```python
print("Hello!")                     # Hello!
print(42)                           # 42
print(3.14)                         # 3.14
print(True)                         # True
print("I am", 17, "years old")      # I am 17 years old
```

### Formatting Output

```python
name = "Alice"
score = 95.5

# Method 1: f-strings (recommended)
print(f"Name: {name}, Score: {score}")

# Method 2: .format()
print("Name: {}, Score: {}".format(name, score))

# Method 3: old-style % formatting (you'll see this in old code)
print("Name: %s, Score: %.1f" % (name, score))
```

### `print()` options

```python
# end= changes what gets printed at the end (default is newline \n)
print("Hello", end=" ")
print("World")          # Prints: Hello World (on one line)

# sep= changes the separator between multiple items (default is space)
print("A", "B", "C", sep="-")   # A-B-C
```

---

## Input with `input()`

`input()` pauses the program and waits for the user to type something:

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

> ⚠️ **Remember**: `input()` always returns a **string**. Convert it if you need a number:

```python
age = int(input("How old are you? "))
height = float(input("What is your height in meters? "))
```

---

## A Complete Example

```python
# A simple calculator
print("=== Simple Calculator ===")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2:.2f}")
else:
    print("Cannot divide by zero!")
```

(Don't worry about the `if` statement yet — that's Module 3!)

---

## Special Characters in Strings

Some characters can't be typed directly into a string. Use **escape sequences**:

```python
print("She said, \"Hello!\"")    # She said, "Hello!"
print("Line 1\nLine 2")          # Two separate lines
print("Tab\there")               # Tab space
print("Backslash: \\")           # Backslash: \
```

| Escape | Meaning |
|--------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote inside a double-quoted string |
| `\'` | Single quote inside a single-quoted string |

---

## Multi-line Strings

Use triple quotes for strings that span multiple lines:

```python
message = """
Dear Alice,

Thank you for your interest.
We'll be in touch soon.

Regards,
The Team
"""
print(message)
```

---

## 📺 Watch These

1. **Python print() Function** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=k9TUPpGqYTo](https://www.youtube.com/watch?v=k9TUPpGqYTo)

2. **Python User Input** — Tech With Tim
   👉 [https://www.youtube.com/watch?v=I9h1c-121Uk](https://www.youtube.com/watch?v=I9h1c-121Uk)

---

## Key Takeaways

- `print()` outputs to the screen; use f-strings for clean formatting
- `input()` reads text from the user — **always returns a string**
- Convert input with `int()` or `float()` when you need numbers
- Escape sequences (`\n`, `\t`) let you include special characters in strings

---

*Next up → [Practice Questions](./questions.md)*
