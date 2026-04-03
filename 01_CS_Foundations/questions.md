# Module 1 — Practice Questions

Try to answer these *without* looking back at the notes first. Then check your answers.

---

## Section A: Short Answer

1. In your own words, what is the difference between *computer science* and *programming*?

2. Name the four main hardware components of a computer and describe what each one does in one sentence.

3. What is an operating system? Give two examples.

4. Why do computers use binary (base 2) instead of decimal (base 10)?

5. What is a bit? What is a byte? How many bits are in a byte?

---

## Section B: Binary Conversions

Convert the following **decimal numbers to binary**:

6. 5
7. 10
8. 23
9. 64
10. 100

Convert the following **binary numbers to decimal**:

11. `0101`
12. `1010`
13. `11111111`
14. `10000000`
15. `11001100`

---

## Section C: Think About It

16. A pixel on a screen is described by three values: red, green, and blue — each between 0 and 255. How many bits does it take to store one pixel?

17. A plain text file containing the word `"Cat"` — how many bytes does it take to store that word? (Hint: think about how many characters there are.)

18. Your computer has 8 GB of RAM. Roughly how many bytes is that? Write out the number.

19. What layer does Python sit on in the "layers of a computer system" model from the notes?

20. **Challenge**: Convert the decimal number `200` to binary by hand. Then verify your answer using Python:
    ```python
    print(bin(200))
    ```

---

## Section D: Reflection

21. Before reading this module, what did you think computer science was? Has your understanding changed? Write 2–3 sentences.

22. What part of this module was most confusing? Write down your question — you can research it or ask someone.

---

## Answers (Try first before peeking!)

<details>
<summary>Click to reveal answers for Section B</summary>

**Decimal → Binary:**
- 5 = `101`
- 10 = `1010`
- 23 = `10111`
- 64 = `1000000`
- 100 = `1100100`

**Binary → Decimal:**
- `0101` = 5
- `1010` = 10
- `11111111` = 255
- `10000000` = 128
- `11001100` = 204

</details>

<details>
<summary>Click to reveal answers for Section C</summary>

16. Each of R, G, B requires 8 bits (to store 0–255). So one pixel = **24 bits** = 3 bytes.

17. "Cat" has 3 characters → **3 bytes** (in ASCII).

18. 8 GB = 8 × 1,024 × 1,024 × 1,024 = **8,589,934,592 bytes** (about 8.6 billion bytes).

19. Python programs sit at **Layer 4 (Applications)**.

20. 200 in binary = `11001000`
    Check: 128 + 64 + 8 = 200 ✓

</details>
