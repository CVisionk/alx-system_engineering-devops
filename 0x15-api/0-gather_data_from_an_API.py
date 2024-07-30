#!/usr/bin/python3
"""
    Placeholder
"""
import requests
import sys


def get_employee_tasks(employee_id):
    """Fetches employee tasks from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee name, number of completed tasks
               total number of tasks, and a list of completed task titles.
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

    completed_tasks = [
        task['title'] for task in all_tasks if task['completed']]

    return employee_name, len(completed_tasks), len(all_tasks), completed_tasks


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    try:
        name, completed, total, tasks = get_employee_tasks(employee_id)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print(f"Employee {name} is done with tasks({completed}/{total}):")
    for task in tasks:
        print(f"\t {task}")
