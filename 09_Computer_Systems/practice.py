# ============================================================
#  Module 9 — Computer Systems: Practice File
# ============================================================
# Topics: Memory, OS, networking
# ============================================================

# --- Exercise 1: References vs Copies ---
# Predict what prints, then run to verify
a = [1, 2, 3]
b = a
b.append(99)
# print(a)    # Uncomment — what do you expect?

# Fix it so b is an independent copy:


# --- Exercise 2: Deep vs Shallow Copy ---
import copy
nested = [[1, 2], [3, 4]]
shallow = copy.copy(nested)
deep = copy.deepcopy(nested)

shallow[0][0] = 999
# What does nested[0][0] print? What about deep[0][0]?
# Uncomment and check:
# print(nested[0][0])
# print(deep[0][0])


# --- Exercise 3: Recursion and the Stack ---
# This function has infinite recursion — add a base case to fix it:
# def countdown(n):
#     print(n)
#     countdown(n - 1)   # ← Fix me!


# --- Exercise 4: Networking (requires pip install requests) ---
# Uncomment and run if you have the requests library installed
# import requests
# response = requests.get("https://api.github.com/users/torvalds")
# data = response.json()
# print(f"Name: {data['name']}")
# print(f"Public repos: {data['public_repos']}")
# print(f"Followers: {data['followers']}")


# --- Exercise 5: File I/O ---
# Write a Python program that:
#   1. Creates a file called "notes.txt"
#   2. Writes 3 lines of text to it
#   3. Reads it back and prints each line


# --- Sandbox ---

