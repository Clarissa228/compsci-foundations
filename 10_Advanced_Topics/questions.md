# Module 10 — Practice Questions & Final Projects

---

## Section A: Databases

1. Create a SQLite database called `students.db` with a table `students` (id, name, grade, score). Insert 5 students, then:
   - Select all students with a score above 80
   - Update one student's score
   - Delete one student
   - Count how many students have grade "A"

2. What is the difference between `SELECT *` and `SELECT name, score`? Why might you prefer the second?

3. What does a **primary key** do in a database table? Why is it important?

---

## Section B: Web

4. Create an HTML file for a simple personal portfolio page that includes:
   - Your name as a heading
   - A short paragraph about yourself
   - A list of 3 skills you've learned in this course
   - A link to somewhere you like on the web

5. Using Python's `requests` library, write a program that:
   - Fetches weather data from the Open-Meteo API (free, no API key): `https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true`
   - Prints the current temperature and wind speed

6. What is a **REST API**? What does "stateless" mean in the context of HTTP?

---

## Section C: AI/ML

7. What is the difference between supervised and unsupervised learning? Give a real-world example of each.

8. Why might a model have high accuracy on training data but perform poorly on new data? (This is called **overfitting**.)

9. Run the Iris classification example from the notes. Try changing the model from `DecisionTreeClassifier` to `KNeighborsClassifier` (also in scikit-learn). Does accuracy improve or get worse?

---

## Section D: Final Projects

Choose one of these projects to complete. They'll combine skills from multiple modules.

---

### Project A: Contact Manager (Beginner–Intermediate)

Build a command-line contact manager that:
- Stores contacts in a SQLite database (name, phone, email)
- Supports: add contact, search by name, list all, delete contact
- Uses OOP — create a `Contact` class and a `ContactBook` class
- Handles errors gracefully (e.g., contact not found)

---

### Project B: Text Analyzer (Intermediate)

Build a tool that:
- Reads a `.txt` file (try a book from [Project Gutenberg](https://gutenberg.org))
- Reports: word count, unique word count, top 20 most common words, average word length, longest sentence
- Optionally: plots a bar chart of top words using `matplotlib`

Skills used: file I/O, strings, dictionaries, sorting, functions

---

### Project C: Number Guessing Game with Leaderboard (Intermediate)

Build a number guessing game that:
- Uses binary search internally to track the minimum guesses needed
- Saves high scores (fewest guesses) to a SQLite database with player names
- Shows the leaderboard at the end
- Times how long each game takes

Skills used: loops, functions, databases, OOP

---

### Project D: Mini Search Engine (Advanced)

Build a simple search engine that:
- Reads a folder of `.txt` files
- Builds an **inverted index**: `{word: [file1, file3, ...]}` (which files contain each word)
- Accepts a search query and returns which files contain all the query words
- Ranks results by how many query words they contain

Skills used: file I/O, dictionaries, sets, algorithms

---

### Project E: Simple Web Server with Flask (Advanced)

Build a to-do list web app:
- Flask backend with routes: GET `/tasks`, POST `/tasks`, DELETE `/tasks/<id>`
- SQLite database to store tasks
- Simple HTML frontend (no framework needed)
- Tasks persist between sessions

Skills used: web, databases, HTTP, OOP, functions

---

## Reflection Questions

10. Which module in this course did you find the most challenging? What helped you get through it?

11. What's one thing you want to build that you now feel capable of starting?

12. What topic do you want to go deeper on next? Look it up and find one resource (book, course, or video) you want to try.

---

*Congratulations on completing the course! → [Next Steps](./04_next_steps.md)*
