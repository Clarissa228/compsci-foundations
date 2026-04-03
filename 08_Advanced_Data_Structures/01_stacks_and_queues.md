# Stacks & Queues

## Stacks — Last In, First Out (LIFO)

A **stack** is a collection where the last item you add is the first one you remove — like a stack of plates.

**Operations**:
- **push** — add to the top
- **pop** — remove from the top
- **peek** — view the top without removing it

Real-world uses: browser back button, undo in a text editor, function call stack, expression evaluation.

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items) + " ← top"


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)          # [1, 2, 3] ← top
print(s.pop())    # 3  (last in, first out)
print(s.peek())   # 2
```

> Python's list is already a stack — use `.append()` to push and `.pop()` to pop.

---

## Classic Stack Problem: Balanced Brackets

Check if brackets in a string are balanced:
`"([]{})"` → True, `"([)]"` → False

```python
def is_balanced(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(is_balanced("({[]})"))   # True
print(is_balanced("([)]"))     # False
```

---

## Queues — First In, First Out (FIFO)

A **queue** is a collection where the first item added is the first one removed — like a line at a store.

**Operations**:
- **enqueue** — add to the back
- **dequeue** — remove from the front
- **front** — view the front without removing

Real-world uses: print queue, task scheduling, BFS graph traversal, message queues.

```python
from collections import deque   # Use Python's efficient deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)        # Add to back

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.popleft()    # Remove from front (O(1) with deque)

    def front(self):
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


q = Queue()
q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Carol")
print(q.dequeue())   # Alice  (first in, first out)
print(q.dequeue())   # Bob
```

> Use `collections.deque` not a plain list for queues — `popleft()` is O(1) vs O(n) for `list.pop(0)`.

---

## Stack vs Queue

| Feature | Stack | Queue |
|---------|-------|-------|
| Order | LIFO | FIFO |
| Add | push (top) | enqueue (back) |
| Remove | pop (top) | dequeue (front) |
| Use cases | Undo, DFS, call stack | Print queue, BFS, scheduling |

---

## 📺 Watch These

1. **Stack Data Structure** — CS Dojo
   👉 [https://www.youtube.com/watch?v=Gj5qBheGOEo](https://www.youtube.com/watch?v=Gj5qBheGOEo)

2. **Queue Data Structure** — CS Dojo
   👉 [https://www.youtube.com/watch?v=XuCbpw6Bj1U](https://www.youtube.com/watch?v=XuCbpw6Bj1U)

---

## Key Takeaways

- **Stack**: LIFO — last in, first out. Use Python list `.append()`/`.pop()`
- **Queue**: FIFO — first in, first out. Use `collections.deque` for efficiency
- Both have O(1) operations for their core add/remove
- Stacks are used everywhere: function calls, expression parsing, undo systems

---

*Next up → [Linked Lists](./02_linked_lists.md)*
