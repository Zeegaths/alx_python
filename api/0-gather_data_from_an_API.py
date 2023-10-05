import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Define the endpoint URLs for employee details and TODO items
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        # Fetch employee details
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")

        # Fetch TODO items for the employee
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Calculate the number of completed tasks and total tasks
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for todo in todo_data if todo["completed"])

        # Display employee's TODO list progress
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

        # Display titles of completed tasks
        for todo in todo_data:
            if todo["completed"]:
                print(f"    {todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
