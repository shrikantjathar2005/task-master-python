from flask import Flask, render_template, request, redirect
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

app = Flask(__name__)

# --- THE ML BRAIN ---
# 1. We give it some initial examples to learn from
train_data = [
    ("buy milk", "Home"), ("buy eggs", "Home"), ("clean room", "Home"),
    ("fix bug", "Work"), ("write code", "Work"), ("meeting", "Work"),
    ("gym", "Health"), ("run", "Health"), ("doctor", "Health"),
    ("movie", "Leisure"), ("game", "Leisure")
]

# Separate sentences (X) and tags (y)
X_train = [x[0] for x in train_data]
y_train = [x[1] for x in train_data]

# 2. Convert text to numbers (Computers only understand numbers)
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)

# 3. Train the Classifier (Naive Bayes is great for text)
clf = MultinomialNB()
clf.fit(X_train_counts, y_train)

# --- APP DATA ---
# Each task is now a dictionary: {'text': 'Buy milk', 'tag': 'Home'}
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        # 4. PREDICT: Ask the ML model what category this task belongs to
        task_vector = vectorizer.transform([task_text])
        prediction = clf.predict(task_vector)[0]
        
        # Add task + the predicted tag
        tasks.append({'text': task_text, 'tag': prediction})
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)