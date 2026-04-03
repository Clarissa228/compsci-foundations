# Binary & Number Systems

## The Big Idea

Computers only understand two things: **on** and **off**. These are represented as **1** and **0**. Every piece of information in a computer — text, images, video, code — is ultimately stored as a sequence of 1s and 0s.

This system is called **binary** (base 2).

---

## Why Binary?

Computers are built from billions of tiny switches called **transistors**. A transistor can only be in one of two states: **on (1)** or **off (0)**. This makes binary the natural language of hardware.

Trying to store 10 values in a transistor would require 10 voltage levels — messy and error-prone. Two values (on/off) is simple, reliable, and fast.

---

## Counting in Binary

You already know base 10 (decimal). In decimal, each digit represents a power of 10:

```
  3   4   7
  ↓   ↓   ↓
300 + 40 + 7 = 347
(10²)(10¹)(10⁰)
```

In binary (base 2), each digit represents a power of **2**:

```
  1   0   1   1
  ↓   ↓   ↓   ↓
  8 + 0 + 2 + 1 = 11
(2³)(2²)(2¹)(2⁰)
```

So `1011` in binary = **11** in decimal.

---

## Converting Decimal → Binary

Divide the number by 2 repeatedly, note the remainders, then read them bottom to top:

```
13 ÷ 2 = 6  remainder 1
 6 ÷ 2 = 3  remainder 0
 3 ÷ 2 = 1  remainder 1
 1 ÷ 2 = 0  remainder 1
                ↑ read upward
13 in binary = 1101
```

Check: `1×8 + 1×4 + 0×2 + 1×1 = 8 + 4 + 0 + 1 = 13` ✓

---

## Bits and Bytes

- A **bit** is a single binary digit: `0` or `1`
- A **byte** is 8 bits: e.g. `10110011`
- A byte can represent 2⁸ = **256** different values (0–255)

| Unit | Size |
|------|------|
| 1 Bit | 0 or 1 |
| 1 Byte | 8 bits |
| 1 Kilobyte (KB) | 1,024 bytes |
| 1 Megabyte (MB) | 1,024 KB |
| 1 Gigabyte (GB) | 1,024 MB |

---

## How Text is Stored in Binary

Every character has a number assigned to it via a standard called **ASCII** (and its modern extension, Unicode):

- `'A'` = 65 = `01000001` in binary
- `'a'` = 97 = `01100001` in binary
- `'0'` = 48 = `00110000` in binary

When you type "Hello", the computer actually stores: `72 101 108 108 111` — and each of those is a byte of binary data.

---

## Hexadecimal (Bonus)

Programmers often use **hexadecimal (base 16)** as a shorthand for binary, because it's much more compact. Hex digits go: 0–9, then A=10, B=11, C=12, D=13, E=14, F=15.

```
Binary:  1111 1111
Hex:       F    F   (= #FF in color codes!)
Decimal: 255
```

You'll see hex a lot in colors (`#FF5733`), memory addresses, and error codes.

---

## Try It in Python

```python
# Python can convert between bases for you
print(bin(13))    # → 0b1101  (binary)
print(hex(255))   # → 0xff    (hexadecimal)
print(int('1101', 2))  # → 13  (binary string to decimal)
```

---

## 📺 Watch These

1. **Binary Numbers and Base Systems** — Khan Academy
   👉 [https://www.youtube.com/watch?v=sXxwr66Y79Y](https://www.youtube.com/watch?v=sXxwr66Y79Y)

2. **How Computers Store Data in Binary** — Computerphile
   👉 [https://www.youtube.com/watch?v=wgbV6DLVezo](https://www.youtube.com/watch?v=wgbV6DLVezo)

3. **Binary, Hexadecimal, Decimal, and ASCII** — Professor Messer
   👉 [https://www.youtube.com/watch?v=nBIVe7k6Wb8](https://www.youtube.com/watch?v=nBIVe7k6Wb8)

---

## Key Takeaways

- Computers store everything as **1s and 0s** (binary)
- Binary is base 2; each digit represents a power of 2
- A **bit** is one binary digit; a **byte** is 8 bits
- Text, images, and video are all just numbers stored as binary
- **Hex** is a compact way to write binary used throughout CS

---

*Next up → [Practice Questions](./questions.md)*
