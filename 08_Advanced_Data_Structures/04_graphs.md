# Graphs

## The Big Idea

A **graph** is a collection of **nodes (vertices)** connected by **edges**. Trees are actually a special kind of graph (acyclic, connected). Graphs are the most general and powerful data structure in CS.

Real-world graphs:
- Social networks (people = nodes, friendships = edges)
- Maps (cities = nodes, roads = edges)
- The internet (websites = nodes, links = edges)
- Dependency systems (packages, build steps)

---

## Types of Graphs

- **Directed** — edges have direction (A→B doesn't mean B→A). Like Twitter follows.
- **Undirected** — edges go both ways. Like Facebook friends.
- **Weighted** — edges have values (e.g., distances). Like a map.
- **Cyclic** — contains cycles (loops). **Acyclic** — no loops. A tree is an acyclic graph.

---

## Graph Representation

### 1. Adjacency List (Most Common)
A dictionary mapping each node to its neighbors:

```python
# Undirected graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}
```

### 2. Adjacency Matrix
A 2D array where `matrix[i][j] = 1` means there's an edge from i to j:

```python
# 0=A, 1=B, 2=C
matrix = [
    [0, 1, 1],   # A connects to B and C
    [1, 0, 0],   # B connects to A
    [1, 0, 0]    # C connects to A
]
```

Adjacency list is preferred for sparse graphs (most real-world graphs).

---

## BFS — Breadth-First Search

**Idea**: Explore all neighbors at the current level before going deeper. Uses a **queue**. Great for finding shortest path.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

print(bfs(graph, "A"))   # ['A', 'B', 'C', 'D', 'E', 'F']
```

---

## DFS — Depth-First Search

**Idea**: Go as deep as possible along each branch before backtracking. Uses a **stack** (or recursion). Great for detecting cycles, topological sort, maze solving.

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs(graph, "A")   # A B D E F C (depth-first)
```

---

## BFS vs DFS

| | BFS | DFS |
|--|-----|-----|
| Structure | Queue | Stack / Recursion |
| Finds | Shortest path | Any path |
| Memory | More (wide frontier) | Less (deep stack) |
| Best for | Shortest path, levels | Cycle detection, topological sort |

---

## Shortest Path with BFS

```python
def shortest_path(graph, start, end):
    visited = {start: None}   # node → how we got here
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = node
                queue.append(neighbor)

    # Reconstruct path
    if end not in visited:
        return None
    path = []
    node = end
    while node:
        path.append(node)
        node = visited[node]
    return list(reversed(path))

print(shortest_path(graph, "A", "F"))   # ['A', 'C', 'F']
```

---

## 📺 Watch These

1. **Graph Data Structure** — William Fiset
   👉 [https://www.youtube.com/watch?v=eQYTnv9GDys](https://www.youtube.com/watch?v=eQYTnv9GDys)

2. **BFS and DFS Explained** — CS Dojo
   👉 [https://www.youtube.com/watch?v=TtcL4lSSzpQ](https://www.youtube.com/watch?v=TtcL4lSSzpQ)

3. **Graph Algorithms for Technical Interviews** — freeCodeCamp
   👉 [https://www.youtube.com/watch?v=tWVWeAqZ0WU](https://www.youtube.com/watch?v=tWVWeAqZ0WU)

---

## Key Takeaways

- Graphs have **nodes** (vertices) and **edges** — the most general data structure
- Represent as **adjacency lists** (dict of lists) for most problems
- **BFS**: uses queue, finds shortest paths, explores level by level
- **DFS**: uses stack/recursion, goes deep first, good for cycle detection
- Graphs are everywhere: social networks, maps, the web, dependency resolution

---

*Next up → [Practice Questions](./questions.md)*
