import requests
import sys

def gather_data_from_an_API(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data["name"]
        done_tasks = 0
        completed_tasks_titles = []

        for todo in todos_data:
            if todo["completed"]:
                done_tasks += 1
                completed_tasks_titles.append(f"Task {todo['id']} Formatting: OK")

        total_tasks = len(todos_data)

        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for title in completed_tasks_titles:
            print(title)
    else:
        print(f"Error: Unable to retrieve data for employee with ID {employee_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        gather_data_from_an_API(employee_id)