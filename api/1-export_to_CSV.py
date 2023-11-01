import json
import requests
import csv
import sys

todo_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'

req = requests.get(todo_url)
results = json.loads(req.text)

task = 0
completed_task_title = []
user_name = ''
user_id = sys.argv[1]

# Create a list to store the tasks
tasks = []

for result in results:
    if result['completed'] == True:
        task = task + 1
        completed_task_title.append(result['title'])

    users = requests.get(f'https://jsonplaceholder.typicode.com/users/{result["userId"]}')
    user = json.loads(users.text)
    user_name = user['name']

    # Append task data to the tasks list
    tasks.append([user_id, user_name, result['completed'], result['title']])

print(f'Employee {user_name} is done with tasks({task}/{len(results)}):')
for finished_task in completed_task_title:
    print(f'\t{finished_task}')

# Export the tasks to a CSV file
csv_file_name = f'{user_id}.csv'
with open(csv_file_name, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    csv_writer.writerows(tasks)

print(f'Tasks data has been exported to {csv_file_name}')
