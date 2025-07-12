from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = os.path.join(os.getcwd(), 'model', 'linear_model.pkl')
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        experience = float(request.form['experience'])
        predicted_salary = model.predict(np.array([[experience]]))[0]
        salary = round(float(predicted_salary), 2)
        return render_template('result.html', experience=experience, salary=salary)
    except Exception as e:
        return f"Error during prediction: {e}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
