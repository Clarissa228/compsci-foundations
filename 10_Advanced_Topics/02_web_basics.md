# Web Development Basics

## The Big Idea

The web is everywhere. Understanding how it's built — even at a basic level — opens up a huge range of what you can create.

---

## Frontend vs Backend

Every web application has two sides:

**Frontend** (what you see):
- HTML — structure of the page
- CSS — styling (colors, layout, fonts)
- JavaScript — interactivity

**Backend** (the server):
- Processes requests
- Talks to the database
- Returns data (usually as JSON or HTML)

Python is primarily used for **backend** development.

---

## HTML — The Skeleton of a Page

HTML (HyperText Markup Language) defines the structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
    <a href="https://google.com">Click me</a>
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
  </body>
</html>
```

Save this as `index.html` and open it in a browser — you've built a webpage!

---

## CSS — The Styling

```css
/* style.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

h1 {
    color: #333;
    text-align: center;
}

p {
    font-size: 16px;
    line-height: 1.6;
}
```

---

## JavaScript — The Behavior

```javascript
// Add interactivity
document.querySelector("button").addEventListener("click", function() {
    alert("You clicked me!");
});
```

---

## Python Web Frameworks

For building backend web apps, Python has popular frameworks:

**Flask** — lightweight, great for learning
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, World!</h1>"

@app.route("/api/users")
def get_users():
    users = [{"name": "Alice"}, {"name": "Bob"}]
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
```

**Django** — full-featured, batteries included (used by Instagram, Pinterest)

**FastAPI** — modern, fast, great for building APIs

---

## APIs (Application Programming Interfaces)

An **API** is a way for programs to talk to each other. Web APIs send data (usually JSON) over HTTP.

```python
import requests

# Call a public API
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&current_weather=true")
data = response.json()
print(data["current_weather"]["temperature"], "°C")
```

Most apps you use (Spotify, Twitter, Google Maps) expose APIs that developers can use.

---

## 📺 Watch These

1. **HTML & CSS Crash Course** — Traversy Media
   👉 [https://www.youtube.com/watch?v=UB1O30fR-EE](https://www.youtube.com/watch?v=UB1O30fR-EE)

2. **Flask Tutorial for Beginners** — Tech With Tim
   👉 [https://www.youtube.com/watch?v=Z1RJmh_OqeA](https://www.youtube.com/watch?v=Z1RJmh_OqeA)

3. **What is an API?** — MuleSoft
   👉 [https://www.youtube.com/watch?v=s7wmiS2mSXY](https://www.youtube.com/watch?v=s7wmiS2mSXY)

---

## Key Takeaways

- Web = frontend (HTML/CSS/JS in the browser) + backend (server, database)
- Python excels at backend development via Flask, Django, or FastAPI
- APIs let programs communicate over HTTP — you'll use them in almost every real project
- HTML/CSS are not programming languages — they're markup/styling languages, but worth knowing basics

---

*Next up → [AI & Machine Learning Intro](./03_ai_ml_intro.md)*
