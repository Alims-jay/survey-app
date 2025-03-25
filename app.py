from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Connect to local MongoDB with credentials from .env
mongo_username = os.getenv('MONGODB_USERNAME')
mongo_password = os.getenv('MONGODB_PASSWORD')
mongo_host = os.getenv('MONGODB_HOST', 'localhost')  # Default: localhost
mongo_port = os.getenv('MONGODB_PORT', '27017')  # Default: 27017

# Construct MongoDB URI for local connection
mongo_uri = f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/"
client = MongoClient(mongo_uri)
db = client['survey_db']  # Database name
collection = db['users']  # Collection name


@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        total_income = request.form['total_income']

        expenses = {}
        categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
        for category in categories:
            if request.form.get(f"{category}_check"):
                amount = request.form.get(f"{category}_amount", 0)
                expenses[category.replace('_', ' ')] = float(amount) if amount else 0.0

        user_data = {
            'Age': int(age),
            'Gender': gender,
            'Total Income': float(total_income),
            'Expenses': expenses
        }
        collection.insert_one(user_data)
        return redirect(url_for('survey'))
    return render_template('survey.html')


if __name__ == '__main__':
    app.run(debug=True)