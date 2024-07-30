#!/usr/bin/python3
"""
    Placeholder
"""
import json
import requests
import sys


def get_employee_tasks(employee_id):
    """Fetches employee tasks from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee's name and a list of tasks.
               Each task is a dictionary with keys 'completed' and 'title'.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        raise ValueError("Invalid employee ID")
    user_data = user_response.json()
    employee_name = user_data['name']

    all_tasks_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if all_tasks_response.status_code != 200:
        raise ValueError("Error fetching tasks")
    all_tasks = all_tasks_response.json()

    return employee_name, all_tasks


def export_to_json(employee_id, employee_name, tasks):
    """Exports tasks to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        tasks (list): A list of tasks dictionaries.
    """
    filename = f"{employee_id}.json"
    data = {
        str(employee_id): [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            } for task in tasks
        ]
    }
    with open(filename, mode='w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    try:
        name, tasks = get_employee_tasks(employee_id)
    except ValueError as e:
        print(e)
        sys.exit(1)

    export_to_json(employee_id, name, tasks)
    print(f"Data exported to {employee_id}.json")
