#!/usr/bin/python3
"""
    Placeholder
"""
import json
import requests

# Define the API endpoints
users_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'

# Fetch data from the API
users_response = requests.get(users_url)
todos_response = requests.get(todos_url)

# Parse the JSON responses
users = users_response.json()
todos = todos_response.json()

# Create a dictionary to store all tasks per user
all_tasks = {}

# Populate the dictionary with tasks for each user
for user in users:
    user_id = user['id']
    username = user['username']
    all_tasks[user_id] = []

    for todo in todos:
        if todo['userId'] == user_id:
            task_info = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            all_tasks[user_id].append(task_info)

# Save the data to a JSON file
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(all_tasks, json_file, indent=4)

print("Data has been exported to todo_all_employees.json")
