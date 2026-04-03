# Databases

## The Big Idea

A **database** is an organized system for storing, retrieving, and managing large amounts of data. Every major application — social media, banking, e-commerce — relies on databases.

---

## Why Not Just Use Files?

Files work for small amounts of data. But for large-scale applications:
- Files are slow to search
- Multiple programs can't safely edit them at once
- No support for complex queries (like "find all users over 25 who signed up last month")
- Hard to ensure consistency when something fails

Databases solve all of these.

---

## Relational Databases (SQL)

The most common type. Data is organized into **tables** with rows and columns — like a spreadsheet. Tables are linked through **relationships**.

**SQL (Structured Query Language)** is the language you use to interact with relational databases.

```
Table: users
+----+---------+----------------------+-----+
| id | name    | email                | age |
+----+---------+----------------------+-----+
|  1 | Alice   | alice@example.com    |  25 |
|  2 | Bob     | bob@example.com      |  30 |
|  3 | Carol   | carol@example.com    |  22 |
+----+---------+----------------------+-----+
```

### Basic SQL Queries

```sql
-- Get all users
SELECT * FROM users;

-- Get specific columns
SELECT name, email FROM users;

-- Filter with WHERE
SELECT * FROM users WHERE age > 25;

-- Sort results
SELECT * FROM users ORDER BY name;

-- Count
SELECT COUNT(*) FROM users;

-- Insert new data
INSERT INTO users (name, email, age) VALUES ('Dave', 'dave@example.com', 28);

-- Update
UPDATE users SET age = 26 WHERE name = 'Alice';

-- Delete
DELETE FROM users WHERE id = 3;
```

---

## Using SQLite with Python

**SQLite** is a simple database that's built into Python — no setup required:

```python
import sqlite3

# Connect to a database (creates it if it doesn't exist)
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
""")

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
conn.commit()   # Save changes

# Query
cursor.execute("SELECT * FROM users WHERE age > 24")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
```

---

## NoSQL Databases

Not all data fits neatly into tables. **NoSQL** databases use flexible formats:

| Type | Examples | Best for |
|------|---------|---------|
| Document | MongoDB, Firestore | JSON-like documents |
| Key-Value | Redis | Caching, sessions |
| Column | Cassandra | Time series, analytics |
| Graph | Neo4j | Social networks, recommendations |

---

## 📺 Watch These

1. **SQL Basics** — freeCodeCamp
   👉 [https://www.youtube.com/watch?v=HXV3zeQKqGY](https://www.youtube.com/watch?v=HXV3zeQKqGY)

2. **SQLite in Python** — Tech With Tim
   👉 [https://www.youtube.com/watch?v=byHcYRpMgI4](https://www.youtube.com/watch?v=byHcYRpMgI4)

---

## Key Takeaways

- Databases store large amounts of structured data reliably and efficiently
- **Relational databases** use tables and SQL — the most widely used
- SQLite is built into Python and is perfect for learning and small apps
- SQL's main operations: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `WHERE`

---

*Next up → [Web Development Basics](./02_web_basics.md)*
