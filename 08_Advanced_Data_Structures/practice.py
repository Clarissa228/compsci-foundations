# ============================================================
#  Module 8 — Advanced Data Structures: Practice File
# ============================================================
# Topics: Stacks, queues, linked lists, trees, graphs (BFS/DFS)
# ============================================================

# --- Exercise 1: Stack ---
# Implement a Stack class using a Python list
# Methods: push, pop, peek, is_empty, size


# --- Exercise 2: Balanced Brackets ---
# Use your Stack to check if a string's brackets are balanced
# "({[]})" → True, "([)]" → False


# --- Exercise 3: Queue ---
# Implement a Queue using collections.deque
# Methods: enqueue, dequeue, front, is_empty, size
from collections import deque


# --- Exercise 4: Linked List ---
# Implement a singly linked list with:
#   append, prepend, delete, __str__, __len__


# --- Exercise 5: Binary Search Tree ---
# Implement a BST with insert and search
# Then print the in-order traversal (should be sorted)


# --- Exercise 6: Graph BFS ---
# Given this graph, implement BFS starting from "A"
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


# --- Sandbox ---

