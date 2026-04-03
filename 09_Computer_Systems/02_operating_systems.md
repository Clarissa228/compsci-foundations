# Operating Systems

## What is an Operating System?

An **operating system (OS)** is software that manages all of a computer's hardware and software resources. It sits between your applications and the physical hardware.

Without an OS, every program would have to directly manage RAM, talk to the keyboard, draw pixels — it would be chaos.

Common OSes:
- **Windows** — desktop, servers
- **macOS** — Apple computers
- **Linux** — servers, Android, embedded systems
- **iOS / Android** — mobile

---

## Core Responsibilities of an OS

### 1. Process Management
A **process** is a running program. The OS:
- Starts and stops processes
- Gives each process its own memory space (so programs can't crash each other)
- Schedules CPU time across multiple processes using a **scheduler**

Even if you have one CPU core, you can have hundreds of processes — the OS rapidly switches between them, giving the illusion of parallelism.

### 2. Memory Management
- Allocates RAM to each process
- Implements **virtual memory** (uses disk as overflow when RAM is full)
- Protects each process's memory from others

### 3. File System Management
- Organizes data as files and directories
- Handles reading/writing to disks
- Manages permissions (who can read/write which files)

### 4. I/O Management
- Provides a unified way to communicate with keyboards, mice, screens, network cards via **device drivers**

### 5. Security & Permissions
- Users have accounts with different levels of access
- System files are protected from modification by regular users

---

## Processes vs Threads

| | Process | Thread |
|--|---------|--------|
| What it is | A full running program | A mini-task within a process |
| Memory | Own isolated memory | Shared memory within process |
| Creation cost | Heavy | Light |
| Example | Chrome.exe | Each Chrome tab |

In Python, the `threading` and `multiprocessing` modules let you create threads and processes:

```python
import threading

def task(name):
    print(f"Task {name} running")

t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))
t1.start()
t2.start()
```

---

## The Command Line / Terminal

The **terminal** (or command line) lets you interact with the OS by typing text commands — faster and more powerful than a GUI for many tasks.

### Essential Commands

```bash
# Navigate
pwd              # Print working directory (where am I?)
ls               # List files in current directory
cd Documents     # Change directory
cd ..            # Go up one level

# Files
mkdir new_folder         # Create directory
touch file.txt           # Create empty file
cp source.txt dest.txt   # Copy
mv old.txt new.txt       # Rename/move
rm file.txt              # Delete file (careful!)

# Python
python script.py         # Run a Python file
python --version         # Check Python version
pip install package      # Install a package
```

---

## What Happens When You Run a Python Script

```
You type: python hello.py
     ↓
OS finds the python binary on your PATH
     ↓
OS creates a new process for Python
     ↓
Python reads hello.py and compiles it to bytecode
     ↓
Python Virtual Machine (PVM) executes the bytecode
     ↓
Output appears in your terminal
     ↓
Process exits, OS reclaims memory
```

---

## 📺 Watch These

1. **Operating Systems Overview** — CrashCourse Computer Science
   👉 [https://www.youtube.com/watch?v=26QPDBe-NB8](https://www.youtube.com/watch?v=26QPDBe-NB8)

2. **Command Line Crash Course** — Traversy Media
   👉 [https://www.youtube.com/watch?v=uwAqEzhyjtw](https://www.youtube.com/watch?v=uwAqEzhyjtw)

---

## Key Takeaways

- An OS manages processes, memory, files, I/O, and security
- **Process**: isolated running program. **Thread**: lightweight task within a process
- The terminal lets you control the OS with text commands — learn the basics!
- When you run Python, the OS creates a process, Python interprets your code

---

*Next up → [Networking Basics](./03_networking.md)*
