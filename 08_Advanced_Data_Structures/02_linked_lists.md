# Linked Lists

## The Big Idea

A **linked list** is a sequence of **nodes**, where each node stores a value and a **pointer** (reference) to the next node. Unlike arrays/lists, the nodes don't need to be in contiguous memory — they're scattered around and linked together.

```
[1] → [2] → [3] → [4] → [5] → None
```

---

## Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    # Points to the next node (or None if last)
```

---

## Linked List Class

```python
class LinkedList:
    def __init__(self):
        self.head = None    # Points to the first node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # Traverse to the end
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head   # Point to current head
        self.head = new_node        # Update head

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next   # Skip the node
                return
            current = current.next

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " → ".join(nodes) + " → None"


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
print(ll)          # 0 → 1 → 2 → 3 → None
ll.delete(2)
print(ll)          # 0 → 1 → 3 → None
```

---

## Linked List vs Python List

| Operation | Linked List | Python List (array) |
|-----------|------------|---------------------|
| Access by index | O(n) | O(1) |
| Insert at front | O(1) | O(n) |
| Insert at end | O(n) | O(1) amortized |
| Delete from front | O(1) | O(n) |
| Search | O(n) | O(n) |
| Memory | More (stores pointers) | Less (contiguous) |

Python lists are better for most tasks. Linked lists are worth knowing for:
- Understanding how data structures work internally
- Interviews
- Implementing stacks, queues, and other structures

---

## Classic Linked List Problems

### Reverse a Linked List
```python
def reverse(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next    # Save next
        current.next = prev         # Reverse pointer
        prev = current              # Move prev forward
        current = next_node         # Move current forward
    self.head = prev
```

### Find the Middle
```python
def find_middle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
        slow = slow.next           # Moves 1 step
        fast = fast.next.next      # Moves 2 steps
    return slow.data   # When fast reaches end, slow is at middle
```

The "slow and fast pointer" technique is a classic interview pattern!

### Detect a Cycle
```python
def has_cycle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True   # They meet → cycle exists
    return False
```

---

## 📺 Watch These

1. **Linked Lists in Python** — CS Dojo
   👉 [https://www.youtube.com/watch?v=JlMyYuY1aXU](https://www.youtube.com/watch?v=JlMyYuY1aXU)

2. **Linked List Interview Problems** — NeetCode
   👉 [https://www.youtube.com/watch?v=G0_I-ZF0S38](https://www.youtube.com/watch?v=G0_I-ZF0S38)

---

## Key Takeaways

- A linked list is made of **nodes** connected by pointers
- O(1) insertion at the front; O(n) access by index
- Three classic patterns: reverse (three-pointer), find middle (slow/fast), detect cycle (slow/fast)
- Python lists (arrays) are more useful in practice — but linked lists teach you to think about memory and pointers

---

*Next up → [Trees](./03_trees.md)*
