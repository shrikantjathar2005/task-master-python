#  AI-Powered Task Master

A smart to-do list application that uses **Machine Learning** to automatically categorize tasks as you type them. Built with Python, Flask, and Scikit-Learn.

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![ML](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Live](https://img.shields.io/badge/Status-Live-red)

##  Live Demo
**[Click here to view the deployed app](https://YOUR-APP-NAME.onrender.com)** *(Note: Since this is on a free tier, it may take 30 seconds to wake up initially.)*

## 💡 Key Features
* **Smart Auto-Tagging:** Uses a **Naive Bayes Classifier (MultinomialNB)** to analyze task text and predict categories (e.g., "Buy milk" → *Home*, "Fix bug" → *Work*).
* **Real-time Interaction:** Instant task addition and deletion.
* **Responsive Design:** Clean, minimal UI that works on mobile and desktop.
* **RESTful Architecture:** Built using standard HTTP methods (GET/POST).

## 🛠️ Tech Stack
* **Backend:** Python 3, Flask
* **Machine Learning:** Scikit-Learn (CountVectorizer, Naive Bayes)
* **Frontend:** HTML5, CSS3, Jinja2 Templating
* **Deployment:** Render (Cloud Hosting), Gunicorn (WSGI Server)

##  How the AI Works
The application trains a lightweight ML model every time it starts:
1.  **Training Data:** It loads a dataset of labeled tasks (Work, Home, Health, Leisure).
2.  **Vectorization:** It converts text into numerical vectors using `CountVectorizer`.
3.  **Classification:** It uses `MultinomialNB` to calculate the probability of a new task belonging to a specific category.

## 💻 Local Setup (Mac/Linux)

If you want to run this project locally:

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/task-master-python.git](https://github.com/YOUR_USERNAME/task-master-python.git)
   cd task-master-python
