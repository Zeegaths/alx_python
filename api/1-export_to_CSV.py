import csv
import json
import requests
import sys

# Function to write data to CSV
def write_to_csv(user_id, user_name, tasks):
    filename = f'{user_id}.csv'
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            csv_writer.writerow([user_id, user_name, task["completed"], task["title"]])

if len(sys.argv) != 2:
    print("Usage: python3 1-export_to_CSV.py <USER_ID>")
    sys.exit(1)

user_id = sys.argv[1]
todo_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

req = requests.get(todo_url)
results = json.loads(req.text)

completed_task_title = []
user_name = results[0]['userId']  # Initialize user_name with the first user's ID
tasks = []

for result in results:
    if result['completed']:
        completed_task_title.append(result['title'])

    if result['userId'] != user_name:
        # Write the tasks of the previous user to CSV
        write_to_csv(user_name, user_name, tasks)
        user_name = result['userId']
        tasks = []

    tasks.append(result)

# Write the tasks of the last user to CSV
write_to_csv(user_name, user_name, tasks)

print(f'Employee {user_name} is done with tasks({len(completed_task_title)}/{len(results)}):')
for finished_task in completed_task_title:
    print('\t', finished_task)
