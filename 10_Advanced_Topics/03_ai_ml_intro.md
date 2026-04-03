# AI & Machine Learning — Introduction

## The Big Idea

**Artificial Intelligence (AI)** is the broad field of making computers perform tasks that normally require human intelligence — recognizing images, understanding language, making decisions.

**Machine Learning (ML)** is the main approach to AI today: instead of programming explicit rules, you give the computer *data* and let it *learn* the patterns.

---

## Traditional Programming vs Machine Learning

**Traditional programming**:
```
Rules + Data → Output
```
You write: "If the email contains 'you've won a million dollars', mark as spam."

**Machine Learning**:
```
Data + Output → Rules (learned automatically)
```
You show thousands of spam and non-spam emails, the model learns what spam looks like.

---

## Types of Machine Learning

### Supervised Learning
Train on labeled data (input-output pairs):
- **Classification**: "Is this email spam?" (yes/no)
- **Regression**: "What will this house sell for?" (a number)

Examples: spam detection, image recognition, loan approval

### Unsupervised Learning
Find patterns in unlabeled data:
- **Clustering**: Group similar customers together
- **Dimensionality reduction**: Compress high-dimensional data

Examples: customer segmentation, anomaly detection

### Reinforcement Learning
An agent learns by trial and error, getting rewards for good actions:
- Examples: playing chess/Go, training robots, self-driving cars

---

## How a Simple Model Works — Linear Regression

**Problem**: Predict a house price from its size (in sqft).

1. You have training data: `[(1000, $200k), (1500, $300k), (2000, $400k)]`
2. The model finds a line: `price = 200 × sqft`
3. For a new house (1750 sqft), predict: `200 × 1750 = $350k`

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
X = np.array([[1000], [1500], [2000]])  # sizes
y = np.array([200000, 300000, 400000]) # prices

model = LinearRegression()
model.fit(X, y)

# Predict
prediction = model.predict([[1750]])
print(f"Predicted price: ${prediction[0]:,.0f}")   # ~$350,000
```

---

## Neural Networks & Deep Learning

A **neural network** is loosely inspired by the human brain — layers of interconnected "neurons" that transform inputs into outputs.

**Deep learning** = neural networks with many layers. It powers:
- Image recognition (is this a cat or a dog?)
- Language models (ChatGPT, Claude)
- Voice assistants (Siri, Alexa)
- Self-driving cars

The math behind it involves linear algebra, calculus, and probability — topics you'll learn in later math courses.

---

## Key Python Libraries for ML

| Library | Purpose |
|---------|---------|
| `numpy` | Fast numerical arrays |
| `pandas` | Data manipulation (like Excel in Python) |
| `matplotlib` | Data visualization |
| `scikit-learn` | Classical ML algorithms |
| `tensorflow` | Deep learning (Google) |
| `pytorch` | Deep learning (Facebook) |

---

## A Taste: Your First ML Model

```python
# Classify flowers by petal measurements
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.1%}")
# Usually prints ~95% accuracy!
```

---

## 📺 Watch These

1. **Machine Learning for Everybody** — freeCodeCamp
   👉 [https://www.youtube.com/watch?v=i_LwzRVP7bg](https://www.youtube.com/watch?v=i_LwzRVP7bg)

2. **But what is a Neural Network?** — 3Blue1Brown (stunning visuals, deep insight)
   👉 [https://www.youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk)

3. **How Large Language Models Work** — Andrej Karpathy
   👉 [https://www.youtube.com/watch?v=zjkBMFhNj_g](https://www.youtube.com/watch?v=zjkBMFhNj_g)

---

## Key Takeaways

- ML learns patterns from data instead of following hand-coded rules
- Three types: supervised (labeled data), unsupervised (pattern finding), reinforcement (trial & error)
- Python + scikit-learn makes it easy to build your first models
- Deep learning (neural networks) powers the most impressive modern AI
- You need linear algebra, statistics, and calculus to go deep — this course gives you the CS foundation

---

*Next up → [Where to Go Next](./04_next_steps.md)*
