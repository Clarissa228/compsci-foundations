# Module 9 — Practice Questions

---

## Section A: Memory

1. In your own words, explain the difference between RAM and a hard drive/SSD. What gets stored in each?

2. What is the difference between a **shallow copy** and a **deep copy** in Python? Give an example where it matters.

3. What happens in Python's memory when you run this code?
   ```python
   a = [1, 2, 3]
   b = a
   b[0] = 99
   print(a)
   ```
   Explain why `a` changes. Draw a diagram if it helps.

4. What is the call stack? What happens to it when you call a function, and when the function returns?

5. What is **garbage collection**? How does Python decide when to free memory?

---

## Section B: Operating Systems

6. What are the five core responsibilities of an operating system? Describe each in one sentence.

7. What is the difference between a **process** and a **thread**?

8. Open your terminal and run the following commands (or look them up if you're on Windows). Describe what each outputs:
   - `pwd` (Mac/Linux) or `cd` with no args (Windows)
   - `ls` (Mac/Linux) or `dir` (Windows)
   - `python --version`

9. When you double-click a Python script to run it, describe in sequence what the OS and Python runtime do.

10. What is **virtual memory**? Why might your computer slow down when RAM is full?

---

## Section C: Networking

11. What is an IP address? What is the difference between IPv4 and IPv6?

12. Explain what DNS does using an analogy (not the phonebook one — come up with your own).

13. What is the difference between HTTP and HTTPS? Why does HTTPS matter?

14. Match the HTTP status codes to their meanings:
    - `404`
    - `200`
    - `500`
    - `301`

    Meanings: Success / Not Found / Server Error / Redirect

15. You're building a video streaming app. Should you use TCP or UDP? Explain your reasoning.

---

## Section D: Applied

16. Using Python's `requests` library (install with `pip install requests`), write a small program that:
    - Fetches the GitHub API: `https://api.github.com/users/torvalds` (Linus Torvalds' GitHub profile)
    - Prints his login, name, number of public repos, and followers

17. Explain what happens at the network level, step by step, when you type `https://www.google.com` into your browser and press Enter. Be as detailed as you can.

18. What is the purpose of **ports**? Why does a web server typically listen on port 443 for HTTPS?

---

## Section E: Reflection

19. Of the topics in this module (memory, OS, networking), which do you find most interesting? Why?

20. If your Python program crashes with `RecursionError: maximum recursion depth exceeded`, what does that tell you about the call stack? How would you fix it?

---

## Answers

<details>
<summary>Q3 — Click to reveal</summary>

When you write `b = a`, you're not copying the list — you're making `b` point to the **same list object** in memory. So when you modify `b[0]`, you're modifying the underlying list that both `a` and `b` reference.

To avoid this: `b = a.copy()` or `b = list(a)` makes a new independent list.

</details>

<details>
<summary>Q14 — Click to reveal</summary>

- `404` → Not Found
- `200` → Success
- `500` → Server Error
- `301` → Redirect

</details>

<details>
<summary>Q16 — Sample code</summary>

```python
import requests

response = requests.get("https://api.github.com/users/torvalds")
data = response.json()

print(f"Login: {data['login']}")
print(f"Name: {data['name']}")
print(f"Public repos: {data['public_repos']}")
print(f"Followers: {data['followers']}")
```

</details>
