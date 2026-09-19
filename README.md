# Sentiment Analysis Web App

> Full project blog: https://adityap-blogs07.blogspot.com/2026/09/sentiment-analysis-using-textblob.html

A simple web application that analyzes the sentiment of user-provided text using Python, Flask, and TextBlob. The app accepts a sentence, paragraph, or any text input, evaluates whether it is positive, negative, or neutral, and displays both the sentiment classification and the underlying polarity and subjectivity scores.

This project is designed to be beginner-friendly while still showing the core concepts behind a real sentiment analysis web app.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage Guide](#usage-guide)
- [Understanding the Results](#understanding-the-results)
- [Frontend Behavior](#frontend-behavior)
- [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Project Overview

This project is a lightweight sentiment analysis application built with:

- Python
- Flask for the web framework
- TextBlob for natural language processing
- HTML, CSS, and JavaScript for the frontend

The application processes input text through TextBlob's sentiment engine and returns:

- Polarity: a score between -1 and 1
- Subjectivity: a score between 0 and 1
- Classification: Positive, Negative, or Neutral

The goal is to help users quickly understand whether a piece of text has a positive or negative emotional tone and how subjective or objective the text appears to be.

This is a lexicon-based sentiment analysis approach, which means it uses predefined word sentiment scores rather than training a machine learning model from scratch.

---

## Features

- Accepts text input from a textarea in the browser
- Analyzes sentiment using TextBlob
- Displays the sentiment classification
- Shows polarity and subjectivity values
- Handles empty input safely without analyzing blank text
- Uses a simple, clean web interface
- Includes a theme toggle with multiple themes
- Stores the selected theme in browser localStorage
- Runs locally in a development server for easy testing

---

## Technology Stack

### Backend
- Python 3
- Flask
- TextBlob

### Frontend
- HTML
- CSS
- JavaScript

### Core Logic
- `TextBlob(text).sentiment` from TextBlob's built-in sentiment analysis engine

### Why these technologies?

- Flask is simple and beginner-friendly for building web apps in Python.
- TextBlob makes sentiment analysis easy without requiring heavy model training.
- HTML/CSS/JS provide a responsive and interactive user experience.

---

## Project Structure

```text
Sentiment_Analysis/
├── main.py
├── requirements.txt
├── LICIENCE
├── README.md
├── frontend/
│   ├── webpage.html
│   ├── script.js
│   ├── dark.css
│   ├── light.css
│   └── darkblue.css
└── __pycache__/   (generated after running Python)
```

### File descriptions

- `main.py`: Contains the Flask app, sentiment analysis logic, and route definitions.
- `requirements.txt`: Lists the required Python dependencies.
- `frontend/webpage.html`: The main HTML page for the interface.
- `frontend/script.js`: Handles theme switching and browser theme persistence.
- `frontend/*.css`: Styling files for the interface themes.
- `LICIENCE`: Project licensing information.

---

## How It Works

### 1. Flask App Setup
The app is created with:

```python
app = Flask(__name__, template_folder='frontend', static_folder='frontend', static_url_path='/static')
```

This tells Flask to use the `frontend` directory for:

- HTML templates
- CSS files
- JavaScript files

### 2. Sentiment Function
The logic for sentiment analysis is implemented in `get_sentiment(text)`.

```python
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
```

TextBlob calculates:

- `polarity`: how positive or negative the text is
- `subjectivity`: how opinionated or factual the text is

Then the application classifies the text as:

```python
if polarity > 0:
    classification = "Positive"
elif polarity < 0:
    classification = "Negative"
else:
    classification = "Neutral"
```

### 3. Route Handling
The app exposes the home route:

```python
@app.route('/', methods=['GET', 'POST'])
def index():
```

- On a `GET` request, the page loads with no results.
- On a `POST` request, the user submits text from the textarea.
- The app reads the submitted text using `request.form.get('text', '')`.
- If the text is not empty, it calls `get_sentiment()`.
- The result is passed into the template to render in the frontend.

### 4. Rendering the Output
The HTML template checks whether `result` exists and prints:

- Sentiment classification
- Polarity score
- Subjectivity score

If no result is available, it shows a placeholder message.

---

## Installation

### Prerequisites

Before running the app, make sure you have:

- Python 3 installed
- `pip` available
- Internet access to install the required package(s)

### Create a virtual environment (recommended)

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

The project currently requires:

```text
Flask
TextBlob
```

---

## Running the Project

From the project root, start the application with:

```bash
python main.py
```

Then open the browser and visit:

```text
http://127.0.0.1:5000/
```

If everything is working correctly, the web interface should load and allow you to enter text for sentiment analysis.

---

## Usage Guide

1. Open the app in your browser.
2. Type a sentence or paragraph into the textarea.
3. Click the Analyze button.
4. The app will evaluate the sentiment and display:
   - Classification (Positive / Negative / Neutral)
   - Polarity score
   - Subjectivity score
5. Use the theme button to switch between available visual themes.

### Example inputs

- "I love this product! It works perfectly."
- "This is a terrible experience and I am disappointed."
- "The meeting started at 10 AM."

### Example output

```text
Sentiment: Positive
Polarity: 0.8
Subjectivity: 0.7
```

---

## Understanding the Results

### Polarity

Polarity measures how positive or negative the sentiment is.

- Values close to `1`: strongly positive
- Values close to `-1`: strongly negative
- Value around `0`: neutral or balanced

Example ranges:

- `0.5` to `1.0` → Positive
- `-1.0` to `-0.5` → Negative
- `0.0` → Neutral

### Subjectivity

Subjectivity measures how opinion-based the sentence is.

- `0.0` → very objective / factual
- `1.0` → highly subjective / opinionated

Example:

- "The weather is cloudy today." → likely low subjectivity
- "I absolutely love this product." → higher subjectivity

### Classification

The app uses this simple rule:

- `polarity > 0` → Positive
- `polarity < 0` → Negative
- `polarity == 0` → Neutral

This is intentionally straightforward and easy to understand for a beginner project.

---

## Frontend Behavior

The frontend is stored in the `frontend` folder and includes:

- `webpage.html`: page layout
- `script.js`: theme handling and localStorage logic
- CSS files: visual styling for different themes

### Theme system
The JavaScript file cycles through three theme styles:

```javascript
let themes = ["/static/dark.css", "/static/light.css", "/static/darkblue.css"];
```

It keeps the current theme in local storage:

```javascript
localStorage.setItem("sentimentTheme", String(currentTheme));
```

This means the selected theme remains active when the page reloads.

---

## Common Issues and Troubleshooting

### 1. ModuleNotFoundError: No module named 'flask' or 'textblob'
This means the dependencies are not installed.

Run:

```bash
pip install -r requirements.txt
```

### 2. The page does not load
Check whether the Flask app is running:

```bash
python main.py
```

Then open:

```text
http://127.0.0.1:5000/
```

### 3. Empty input is being analyzed
The app checks for blank text before analysis:

```python
if user_text.strip():
```

This prevents empty strings from being processed.

### 4. Browser loads but no results appear
Make sure the form posts to the correct route:

```html
<form method="POST" action="/">
```

The backend route is configured to handle POST requests on `/`.

### 5. Theme does not switch properly
Make sure JavaScript is loaded correctly and the static path is accessible. The page includes:

```html
<script src="{{ url_for('static', filename='script.js') }}" defer></script>
```

---

## Future Improvements

This project can be expanded in many ways, including:

- Adding support for multiple languages
- Improving sentiment accuracy with a trained model
- Adding a REST API endpoint for programmatic use
- Displaying a sentiment meter or chart
- Saving previous analyses in a database
- Supporting file upload for bulk text analysis
- Adding user authentication and history tracking
- Packaging the app with Docker for easier deployment

---

## License

This project includes a license file named `LICIENCE`. Please review that file for usage, redistribution, and modification terms.

---

## Summary

This project demonstrates a complete beginner-friendly sentiment analysis application built with Flask and TextBlob. It accepts user text, classifies the sentiment, and presents simplified results in a clean browser interface.

It is a good example of how to combine:

- a Python backend
- a simple web form
- a natural language processing library
- a straightforward frontend interface

If you want to learn how a basic AI-powered text analysis app works in practice, this project is a solid starting point.
