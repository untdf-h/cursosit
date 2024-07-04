import json
from faker import Faker
from random import randint, choice
from datetime import datetime, timedelta

fake = Faker()

fixture = []

# Generate Users
for i in range(1, 11):
    fixture.append({
        "model": "auth.user",
        "pk": i,
        "fields": {
            "username": fake.user_name(),
            "password": " ",
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name()
        }
    })
# Write the fixture to a file
with open('user_fixture.json', 'w') as f:
    json.dump(fixture, f, indent=2)