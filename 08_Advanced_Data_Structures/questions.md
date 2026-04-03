# Module 8 — Practice Questions

---

## Section A: Stacks & Queues

1. Implement a stack that also supports a `get_min()` operation that returns the minimum element in O(1) time. (Hint: use a second "min stack".)

2. Use a stack to evaluate a simple **postfix expression** (also called Reverse Polish Notation):
   - `"3 4 +"` → 7
   - `"5 1 2 + 4 * + 3 -"` → 14
   - Rules: when you see a number, push it; when you see an operator, pop two numbers, apply the operator, push the result.

3. Implement a **queue using two stacks**. It should have `enqueue(x)` and `dequeue()`.
   - Hint: one stack for incoming items, one for outgoing.

4. What's the difference between `list.pop()` and `deque.popleft()` in terms of time complexity? Why does it matter?

---

## Section B: Linked Lists

5. Implement a linked list with these operations:
   - `append(data)` — add to end
   - `prepend(data)` — add to front
   - `delete(data)` — remove first occurrence
   - `__len__` — number of nodes
   - `__str__` — print as "1 → 2 → 3 → None"

6. Write a function `reverse_linked_list(head)` that reverses a linked list in place. Return the new head.

7. Write a function `find_kth_from_end(head, k)` that finds the kth node from the end of the list in **one pass** (no using len or two passes). Hint: use two pointers, k steps apart.

8. Write a function `remove_duplicates(head)` that removes duplicate values from an **unsorted** linked list. Use a set to track seen values.

---

## Section C: Trees

9. Build a BST by inserting these values in order: `[8, 3, 10, 1, 6, 14, 4, 7, 13]`. Draw the resulting tree (on paper or in a comment), then verify by printing the in-order traversal — it should give sorted output.

10. Write a function `tree_height(node)` that returns the height of a binary tree recursively.

11. Write a function `count_nodes(node)` that counts the total number of nodes in a binary tree.

12. Write a function `is_bst(node, min_val=float('-inf'), max_val=float('inf'))` that returns `True` if a binary tree is a valid BST.

13. Write a function `level_order(root)` that returns a list of lists, where each inner list contains the values at that level of the tree:
    ```
    Tree:      10
              /  \
             5    15
            / \
           3   7

    Output: [[10], [5, 15], [3, 7]]
    ```
    Hint: use BFS with a queue.

---

## Section D: Graphs

14. Represent this graph as an adjacency list:
    ```
    A -- B -- D
    |    |
    C -- E
    ```

15. Implement BFS on your graph from Q14. Starting from A, what order do nodes get visited?

16. Write a function `has_path(graph, start, end)` that returns `True` if there's any path between `start` and `end` in an undirected graph.

17. Write a function `count_components(graph)` that counts how many **connected components** an undirected graph has. (A connected component is a group of nodes all reachable from each other.)

18. Write `is_bipartite(graph)` — a graph is bipartite if you can color every node with one of two colors such that no two adjacent nodes share a color. Use BFS. (This is equivalent to: the graph has no odd-length cycles.)

---

## Section E: Challenges

19. **Clone a linked list with random pointers**: Each node has `next` and `random` (points to any node or None). Clone the full list.

20. **Serialize and deserialize a BST**: Write `serialize(root)` → string, and `deserialize(s)` → tree. The round-trip should preserve the structure.

21. **Word Ladder**: Given a start word, end word, and a list of valid words, find the shortest transformation sequence where each step changes exactly one letter. (BFS problem — each word is a node, edges connect words that differ by one letter.)

---

## Answers

<details>
<summary>Q3 — Queue using two stacks hint</summary>

```python
class QueueFromStacks:
    def __init__(self):
        self.inbox = []    # Stack 1: for enqueue
        self.outbox = []   # Stack 2: for dequeue

    def enqueue(self, x):
        self.inbox.append(x)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()
```

</details>

<details>
<summary>Q13 — Level-order hint</summary>

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.data)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

</details>
