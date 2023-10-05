import requests
import sys

def get_employee_info(employee_id):
    """
    Retrieve and display information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    try:
        # Fetch employee details
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data.get('name')

        # Fetch employee's TODO list
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Calculate TODO list progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for task in todos_data if task.get('completed'))

        # Display progress
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

        # Display completed task titles with "Task X: TASK_TITLE" format
        task_number = 1
        for task in todos_data:
            if task.get('completed'):
                print(f"    Task {task_number}: {task.get('title')}")
                task_number += 1

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
