import json
import requests
import csv
import sys

def user_info(user_id):
    todo_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    req = requests.get(todo_url)
    results = json.loads(req.text)

    completed_tasks = []
    user_name = ''

    for result in results:
        if result['completed'] == True:
            completed_tasks.append(result)

        if not user_name:
            users = requests.get(f'https://jsonplaceholder.typicode.com/users/{result["userId"]}')
            user = json.loads(users.text)
            user_name = user['name']

    print(f'Employee {user_name} is done with tasks ({len(completed_tasks)}/{len(results)}):')

    for task in completed_tasks:
        print(f'\t{task["title"]}')

    # Write the tasks to a CSV file
    if completed_tasks:
        with open(f'{user_id}.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in completed_tasks:
                csv_writer.writerow([user_id, user_name, task['completed'], task['title'])

try:
    user_id = int(sys.argv[1])
    user_info(user_id)
except FileNotFoundError:
    print("CSV file not found.")
