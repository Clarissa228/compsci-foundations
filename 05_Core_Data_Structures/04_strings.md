# Strings — Deep Dive

## The Big Idea

Strings might seem simple, but Python gives you incredibly powerful tools to work with text. Since almost all programs deal with text in some form, mastering strings pays off immediately.

---

## Strings are Sequences

Strings behave like lists of characters — you can index, slice, and loop over them:

```python
s = "Hello, World!"

print(s[0])       # 'H'
print(s[-1])      # '!'
print(s[0:5])     # 'Hello'
print(s[7:])      # 'World!'
print(s[::-1])    # '!dlroW ,olleH'  (reversed!)
print(len(s))     # 13
```

---

## Strings are Immutable

Unlike lists, you **cannot** modify a string in place:

```python
s = "hello"
s[0] = "H"   # ❌ TypeError — strings are immutable
```

Instead, create a new string:
```python
s = "H" + s[1:]
print(s)   # "Hello"
```

---

## Essential String Methods

```python
s = "  Hello, World!  "

# Case manipulation
print(s.lower())         # "  hello, world!  "
print(s.upper())         # "  HELLO, WORLD!  "
print(s.title())         # "  Hello, World!  "
print(s.capitalize())    # "  hello, world!  " → first char uppercased

# Whitespace
print(s.strip())         # "Hello, World!"    — removes leading/trailing whitespace
print(s.lstrip())        # "Hello, World!  "  — left only
print(s.rstrip())        # "  Hello, World!"  — right only

# Search
print("World" in s)              # True
print(s.find("World"))           # 9    (index of start; -1 if not found)
print(s.count("l"))              # 3    (how many times 'l' appears)
print(s.startswith("  Hello"))   # True
print(s.endswith("  "))          # True

# Replace
print(s.replace("World", "Python"))   # "  Hello, Python!  "
```

---

## Splitting and Joining

```python
# split() — string → list
sentence = "apple,banana,cherry"
fruits = sentence.split(",")
print(fruits)   # ["apple", "banana", "cherry"]

words = "Hello World".split()   # default splits on whitespace
print(words)   # ["Hello", "World"]

# join() — list → string
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))    # "apple, banana, cherry"
print(" | ".join(fruits))   # "apple | banana | cherry"
print("".join(fruits))      # "applebananacherry"
```

---

## String Formatting

### f-strings (Modern — Recommended)
```python
name = "Alice"
score = 95.678

print(f"Name: {name}")
print(f"Score: {score:.2f}")    # 2 decimal places → 95.68
print(f"Score: {score:8.2f}")   # Width 8, 2 decimals →    95.68
print(f"{'center':^20}")        # Centered in 20 chars
print(f"{'right':>20}")         # Right-aligned
print(f"{'left':<20}|")         # Left-aligned
```

---

## Checking String Content

```python
s = "Hello123"

print(s.isalpha())    # False — contains digits
print(s.isdigit())    # False — contains letters
print(s.isalnum())    # True  — only letters and digits
print("   ".isspace())   # True — only whitespace
print("hello".islower()) # True — all lowercase
print("HELLO".isupper()) # True — all uppercase
```

---

## Raw Strings and Escape Characters

```python
# Regular string
path = "C:\\Users\\Alice\\Documents"   # Need to escape backslashes
print(path)   # C:\Users\Alice\Documents

# Raw string — backslashes are literal
path = r"C:\Users\Alice\Documents"
print(path)   # C:\Users\Alice\Documents

# Useful for regular expressions and file paths
```

---

## 📺 Watch These

1. **Python Strings** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=k9TUPpGqYTo](https://www.youtube.com/watch?v=k9TUPpGqYTo)

2. **Python String Methods** — Programming with Mosh
   👉 [https://www.youtube.com/watch?v=4c8UjHxFCto](https://www.youtube.com/watch?v=4c8UjHxFCto)

---

## Key Takeaways

- Strings are **immutable sequences** — index and slice like lists, but can't modify in place
- `split()` turns a string into a list; `join()` turns a list into a string
- Learn: `.lower()`, `.upper()`, `.strip()`, `.replace()`, `.find()`, `.count()`
- f-strings are the best way to format strings — learn the `:.2f` and `:>10` width syntax
- `isalpha()`, `isdigit()`, `isalnum()` help validate user input

---

*Next up → [Practice Questions](./questions.md)*
