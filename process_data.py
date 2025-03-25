import csv
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

    def to_csv_row(self):
        categories = ['utilities', 'entertainment', 'school fees', 'shopping', 'healthcare']
        return {
            'Age': self.age,
            'Gender': self.gender,
            'Total Income': self.total_income,
            **{cat: self.expenses.get(cat, 0) for cat in categories}
        }


# Connect to local MongoDB
mongo_username = os.getenv('MONGODB_USERNAME')
mongo_password = os.getenv('MONGODB_PASSWORD')
mongo_host = os.getenv('MONGODB_HOST', 'localhost')
mongo_port = os.getenv('MONGODB_PORT', '27017')

mongo_uri = f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/"
client = MongoClient(mongo_uri)
db = client['survey_db']
users_data = list(db.users.find({}, {'_id': 0}))

# Generate CSV
with open('user_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=[
        'Age', 'Gender', 'Total Income',
        'utilities', 'entertainment', 'school fees', 'shopping', 'healthcare'
    ])
    writer.writeheader()
    for data in users_data:
        user = User(
            data['Age'],
            data['Gender'],
            data['Total Income'],
            data['Expenses']
        )
        writer.writerow(user.to_csv_row())